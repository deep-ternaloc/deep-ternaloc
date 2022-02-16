from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import socket
import time
import random
from matplotlib import transforms

global counter
counter=0
class Geo():
    def __init__(self):
        self.src_filename = r'C:\Users\emrea\Desktop\'22 codes\deep-ternaloc\deep-ternaloc\Studies\emre\data\n38_e038_1arc_v3.dt2'
        
        
        
        
    def readAsArray(self):
        self.src_ds=gdal.Open(self.src_filename) 
        self.gt=self.src_ds.GetGeoTransform()
        self.rb=self.src_ds.GetRasterBand(1)
        self.data_array = self.src_ds.ReadAsArray()
        self.data_array=self.data_array.astype(int)[:,:]
        print(np.shape(self.data_array))
        print(3601*3601)
        return self.data_array
    



class Plotting():
    def __init__(self,data_array):
        self.fig = plt.figure(figsize = (16, 12))
        self.ax = self.fig.add_subplot(111)
        self.data_array = data_array
        self.loc_list_x = []
        self.loc_list_y = []


    def plot_array(self):
        plt.contour(self.data_array, cmap = "viridis", 
                    levels = list(range(0, 2598, 100)))
        
        plt.title("Elevation Contours of BOLU ANKARA")
        cbar = plt.colorbar()
        plt.gca().set_aspect('equal', adjustable='box')        
        
        
    def find_nearly_point(self,received_data):

        
        received_data=3000-int(received_data.split(",")[2].split(".")[0])
        
        print(received_data)
        interval_X = received_data+5
        interval_Y = received_data-5
        

        
        


        
        near_points=np.where(np.logical_and(interval_Y<=self.data_array,self.data_array <=interval_X))

        #print(near_points)
        
        
        col = (np.random.random(), np.random.random(), np.random.random())
        print("abo")
        if counter ==5:
            plt.contour(self.data_array, cmap = "viridis", 
            levels = list(range(0, 2598, 100)))
        
            plt.title("Elevation Contours of BOLU ANKARA")
            cbar = plt.colorbar()
            plt.gca().set_aspect('equal', adjustable='box')  
            plt.scatter(near_points[1], near_points[0], c=[col],s=50, marker='x')

            plt.show()
        else:
            plt.contour(self.data_array, cmap = "viridis", 
            levels = list(range(0, 2598, 100)))
        
            plt.title("Elevation Contours of BOLU ANKARA")
            cbar = plt.colorbar()
            plt.gca().set_aspect('equal', adjustable='box')  
            plt.scatter(near_points[1], near_points[0], c=[col])

            plt.show()
            


    def find_x_y_position(self,received_data):
        

        

        
        x_pos = (int(received_data.split(",")[0].split(".")[0])/(13000/3600))
        y_pos = 3600-(int(received_data.split(",")[1].split(".")[0])/(13000/3600))
        
        self.loc_list_y.append(y_pos)
        self.loc_list_x.append(x_pos)
        
        
        self.live_plot()
        #print(y_pos,x_pos)
        #plt.plot(x_pos, y_pos, color=(0, 0, 0), marker='o', markersize=10)
        
        #plt.show()
        
    
        
    def live_plot(self):
        
        plt.contour(self.data_array, cmap = "viridis", 
                    levels = list(range(0, 2598, 100)))
        
        plt.title("Elevation Contours of BOLU ANKARA")
        cbar = plt.colorbar()
        plt.gca().set_aspect('equal', adjustable='box')   
        plt.plot(self.loc_list_x, self.loc_list_y, c=(0, 0, 0), marker='o', markersize=10)
            

            
        plt.show()
        
        
        
        
class UnityInteraction():
    def __init__(self):
        
        host, port = "127.0.0.1", 25002
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        
        
    def connection_loop(self):
         #sleep 0.5 sec

        #print("sleep bitti")
        self.sock.sendall("posString".encode("UTF-8")) #Converting string to Byte, and sending it to C#
        #print("data yollandi")
        self.receivedData = self.sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
        #print("data alindi")
        #self.receivedData = self.receivedData.split(".")[0]
        
        #print(self.receivedData)
        
        return self.receivedData
        
        
if __name__ == "__main__":
    geo_object = Geo()
    data_array = geo_object.readAsArray()
    plot_object = Plotting(data_array)
    #plot_object.plot_array()
    unity_object = UnityInteraction()
    while counter !=6:
        received_data=unity_object.connection_loop()
        #print("datayi aldim")
        plot_object.find_nearly_point(received_data)
        #print("plotladim bitti")
        counter=counter+1
        
        
        

    