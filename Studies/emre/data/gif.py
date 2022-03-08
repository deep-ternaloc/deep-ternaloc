import imageio
import glob
import os

images = []
for filename in glob.glob(os.path.join(r"C:\Users\emrea\Desktop\'22 codes\deep-ternaloc\deep-ternaloc\Studies\emre\data\plt_files",'*.png')):
    images.append(imageio.imread(filename))
imageio.mimsave('movie4eniyi.gif', images)


