import rasterio
from matplotlib import pyplot as plt

dataset = rasterio.open("E:\deep-ternaloc-data\ChannelIslands\deneme.TIF")

plt.imshow(dataset.read(2),transform=dataset.transform,cmap='viridis')


plt.show()

