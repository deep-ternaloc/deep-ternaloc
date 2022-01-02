from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import socket
import time




class Geo():
    def __init__(self):
        self.src_filename = r'C:\Users\emrea\Desktop\deep-ternaloc\deep-ternaloc\Studies\emre\n38_e038_1arc_v3.dt2'
        
        
        
        
    def readAsArray(self):
        self.src_ds=gdal.Open(self.src_filename) 
        self.gt=self.src_ds.GetGeoTransform()
        self.rb=self.src_ds.GetRasterBand(1)
        self.data_array = self.src_ds.ReadAsArray()
        self.data_array=self.data_array.astype(int)[:,:]
        
        return self.data_array
    



class Plotting():
    def __init__(self,data_array):
        self.fig = plt.figure(figsize = (16, 12))
        self.ax = self.fig.add_subplot(111)
        self.data_array = data_array
        


    def plot_array(self):
        plt.contour(self.data_array, cmap = "viridis", 
                    levels = list(range(0, 10000, 100)))
        
        plt.title("Elevation Contours of BOLU ANKARA")
        cbar = plt.colorbar()
        plt.gca().set_aspect('equal', adjustable='box')        
        
        
    def find_nearly_point(self,received_data):

        
        received_data=1000-int(received_data)
        
        print(received_data)
        interval_X = received_data+50
        interval_Y = received_data-50
        

        
        


        
        near_points=np.where(np.logical_and(interval_Y<=self.data_array,self.data_array <=interval_X))
        print(np.where(self.data_array<=500))
        print(near_points)
        
        
        plt.plot(near_points[1], near_points[0], "ro")
        print("abo")
        plt.savefig('foo.png')
        

        
        
        
        
class UnityInteraction():
    def __init__(self):
        
        host, port = "127.0.0.1", 25002
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        
        
    def connection_loop(self):
        time.sleep(0.5) #sleep 0.5 sec


        self.sock.sendall("posString".encode("UTF-8")) #Converting string to Byte, and sending it to C#
        self.receivedData = self.sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
        self.receivedData = self.receivedData.split(".")[0]
        print(self.receivedData)
        
        return self.receivedData
        
        
if __name__ == "__main__":
    geo_object = Geo()
    data_array = geo_object.readAsArray()
    plot_object = Plotting(data_array)
    plot_object.plot_array()
    unity_object = UnityInteraction()
    while True:
        received_data=unity_object.connection_loop()
        plot_object.find_nearly_point(received_data)
        break
        
        
        

    