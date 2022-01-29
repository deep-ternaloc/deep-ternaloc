
from osgeo import gdal,ogr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

src_filename = r'C:\Users\emrea\Desktop\deep-ternaloc\deep-ternaloc\Studies\emre\n38_e038_1arc_v3.dt2'
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)
data_array = src_ds.ReadAsArray()
data_array=data_array.astype(int)[:,:]
print("max {}".format(np.amax(data_array)))  
#print(data_array[0,1])

#print(len(data_array))
#data_array.tofile("dted.csv", sep=",",format="%d")
#print(data_array[5,20],data_array[6,21])

fig = plt.figure(figsize = (16, 12))
ax = fig.add_subplot(111)
plt.contour(data_array, cmap = "viridis", 
            levels = list(range(0, 2598, 105)))


#print(abo)

#plt.plot(data_array[5,20], data_array[6,21], "ro")
#plt.plot(data_array[107,20], data_array[93,670], "ro")
plt.title("Elevation Contours of BOLU ANKARA")
cbar = plt.colorbar()
plt.gca().set_aspect('equal', adjustable='box')


plt.show()