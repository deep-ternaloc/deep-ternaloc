import random
import matplotlib.pyplot as plt 
import numpy as np
from tqdm import tqdm
import imageio
scale = 108000/3600

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



    def plot_object_position(self,x,y,data_array):
        

        
        self.loc_list_y.append(y)
        self.loc_list_x.append(x)
        
        
        self.live_plot(data_array)
        #print(y_pos,x_pos)
        #plt.plot(x_pos, y_pos, color=(0, 0, 0), marker='o', markersize=10)
        
        #plt.show()
        
    def live_plot(self, x,y,data_array,particles,cnt):
        
        
        if len(particles) == 0:
            return
        #self.loc_list_y.append(y)
        #self.loc_list_x.append(x)
        

        try:
            plt.clf()
        except:
            pass

        if  cnt != 0:
            plt.contour(data_array, cmap = "viridis", 
            levels = list(range(0, 2598, 100)))
        
            plt.title("Elevation Contours of ELAZIG")
            cbar = plt.colorbar()
            plt.gca().set_aspect('equal', adjustable='box')

            plt.plot(x, y, c=(0, 0, 0), marker='o', markersize=10)

            print(f"Particle len in plot {len(particles)}")

            for i in range(len(particles)):
                col = (np.random.random(), np.random.random(), np.random.random())
                #for j in particles[i].x_list:
                #    if j > 3600:
                #        continue
                #    else:
                plt.plot(particles[i].x,particles[i].y, c=col, marker='o',markersize=10)

            plt.savefig(f"C:/Users/emrea\Desktop/'22 codes/deep-ternaloc/deep-ternaloc/Studies/emre/data/plt_files/eastern-anatolia-{cnt}.png")
            print("Saved")
