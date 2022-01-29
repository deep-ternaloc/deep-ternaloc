import matplotlib.pyplot as plt 
import numpy as np


class Plotify():
    def __init__(self):
        self.fig = plt.figure(figsize = (16, 12))
        self.ax = self.fig.add_subplot(111)
        self.loc_list_x = []
        self.loc_list_y = []



    def plot_contour_map(self,data_array):
        plt.contour(data_array, cmap = "viridis", 
                    levels = list(range(0, 2598, 100)))
        
        plt.title("Elevation Contours of Eastern Anatolia")
        cbar = plt.colorbar()
        plt.gca().set_aspect('equal', adjustable='box')  
        plt.imsave(r'deep-ternaloc\Studies\emre\data\eastern-anatolia.png',data_array)



    def find_x_y_position(self,received_data,data_array):
        
        x_pos = (int(received_data.split(",")[0].split(".")[0])/(13000/3600))
        y_pos = 3600-(int(received_data.split(",")[1].split(".")[0])/(13000/3600))
        
        
        self.loc_list_y.append(y_pos)
        self.loc_list_x.append(x_pos)
        
        
        self.live_plot(data_array)
        #print(y_pos,x_pos)
        #plt.plot(x_pos, y_pos, color=(0, 0, 0), marker='o', markersize=10)
        
        #plt.show()
        
    def live_plot(self,data_array):
        
        plt.contour(data_array, cmap = "viridis", 
                    levels = list(range(0, 2598, 100)))
        
        plt.title("Elevation Contours of BOLU ANKARA")
        cbar = plt.colorbar()
        plt.gca().set_aspect('equal', adjustable='box')   
        plt.plot(self.loc_list_x, self.loc_list_y, c=(0, 0, 0), marker='o', markersize=10)
            

            
        plt.show()