from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import pyqtSignal, QThread
from osgeo import gdal
import sys
from ui import Ui_MainWindow
from connectify.connect import UnityConnection
from objectify.object import Object
from particlefy.particle import Particle
from plotify.plot import Plotify
import time

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)



class MainWindow(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)
        

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.uc = UnityConnection()
        self.uc.establish_connection()
        self.y_list = []
        self.counter = 0
        self.particles = []
        self.src_filename = r'C:\Users\emrea\Desktop\'22 codes\deep-ternaloc\deep-ternaloc\Studies\emre\data\n38_e038_1arc_v3.dt2'




        self.contourlayout = QVBoxLayout()
        self.ui.graph_widget.setLayout(self.contourlayout)

        self.contour_map = MplCanvas(self.ui,width=6, height=5, dpi=70)
        self.contourlayout.addWidget(self.contour_map)
        self.prepare_contour_map()

        self.ui.connectbutton.clicked.connect(self.connect_to_unity)


        



        self.show()

    def read_dted(self):
        self.src_ds=gdal.Open(self.src_filename) 
        self.gt=self.src_ds.GetGeoTransform()
        self.rb=self.src_ds.GetRasterBand(1)
        self.data_array = self.src_ds.ReadAsArray()
        self.data_array=self.data_array.astype(int)[:,:]
        self.object = Object(self.data_array)
        self.plotify = Plotify()
    
    def prepare_contour_map(self):
        self.read_dted()

        self.contour_map.axes.cla()
        self.contour_map.axes.contour(self.data_array, cmap = "viridis", 
                    levels = list(range(0, 2598, 100)))
        
        
        #cbar = plt.colorbar()
        #plt.gca().set_aspect('equal', adjustable='box')   


        self.contour_map.draw()

    def connect_to_unity(self):
    

        self.data_thread = MyThread(self.uc)
        self.data_thread.coordinate_value.connect(self.find_position)
        self.data_thread.start()

    def find_position(self,data):


        x,y,height = self.object.find_position(data)

        near_points = self.object.find_nearly_heights(height)

        if self.counter == 0:
            for i in range(0,len(near_points[0]),100):
                #particle oluştur 
                self.particles += [Particle(near_points[1][i],near_points[0][i],height)]
            self.y_list.append(y)

            
            

        else:

            speed=abs(y-self.y_list[-1])



            self.y_list.append(y)
            for i in range(len(self.particles)):
                self.particles[i].move(speed)
        
        self.plotify.live_plot(x,y,self.data_array,self.particles,self.counter,self.contour_map)
        self.contour_map.draw()
        print("Drew")
        self.counter += 1

        

        
class MyThread(QThread):

    def __init__(self, vehicle, parent=None):
        super(MyThread, self).__init__(parent)
        self.mission = vehicle

    coordinate_value = pyqtSignal(str)

    def run(self):

        while True:
            
            self.coordinate_val = self.mission.receive_data()

            self.coordinate_value.emit(self.coordinate_val)

            time.sleep(10)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())