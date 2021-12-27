
from osgeo import gdal,ogr
import numpy as np
import matplotlib.pyplot as plt


src_filename = r'C:\Users\emrea\Desktop\deep-ternaloc\deep-ternaloc\Studies\emre\n40_e032_1arc_v3.dt2'
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)
data_array = src_ds.ReadAsArray().astype(np.float)
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111)
plt.contour(data_array, cmap = "viridis", 
            levels = list(range(0, 5000, 100)))
plt.title("Elevation Contours of BOLU ANKARA")
cbar = plt.colorbar()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()