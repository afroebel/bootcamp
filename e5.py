"""
a) Load in the series of images contained in the directory
 data/bacterial_growth/. Be sure that however you store them
  (a list or tuple or other object) has the frames in the proper order.
b) Segment the images to separate bacteria from background. You do
 not need to segment individual bacteria; this would likely require
  some more advanced techniques involving edge detection that we
   haven't covered in bootcamp.
c) Show a representative image from the stack (with the segmentation
 overlayed in green) of images with a 10 µm scale bar burned in.
d) Plot a growth curve for this growing colony. What values should
 be on the  yy -axis? (This is one of those times where I ask an
  open question for which there is no "right" answer.)
e) Perform a regression on this growth curve to estimate the
 time constant for the exponential growth. Be sure to check out
  the README file in the directory containing the images to get
   the appropriate metadata.
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
# Instead of context manager (with):
sns.set_style('dark')

import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation
from os import listdir

# Part A: Create a list of sorted file
#f for f part: same as saying for f in listdir,etc: if,etc: return f
mypath = 'data/bacterial_growth/'
file_list = sorted([f for f in listdir(mypath) if '.tif' in f])

# Create a list of images
im_list = []
for i in np.arange(55):
     img = skimage.io.imread('data/bacterial_growth/'+file_list[i])
     im_list.append(img)

# Get thresholds for each image:
thresh_list = []
for i in np.arange(55):
    thresh = skimage.filters.threshold_otsu(im_list[i])
    thresh_list.append(thresh)

# Apply thresholds:
filt_im_list = []
for i in np.arange(55):
    filt_im = im_list[i] > thresh_list[i]
    filt_im_list.append(filt_im)

# Compute the region properties and extract area of each object.
ip_dist = 64.5 #nm per pixel

filt_im_labs = []
num_lab_list = []
for i in np.arange(55):
    labs, num_lab = skimage.measure.label(filt_im_list[i], return_num=True, background=0)
    filt_im_labs.append(labs)
    num_lab_list.append(num_lab)

props_list = []
for i in np.arange(55):
    props = skimage.measure.regionprops(filt_im_labs[i])
    props_list.append(props)

areas_list = []
# for i in np.arange(55):
#     for n in np.arange(num_lab_list[i]):
#         area = props_list[i][n].area
#         areas_list.append(area)

for i in np.arange(55):
    area = props_list[i][0].area
    areas_list.append(area)

# Plot
x_times = np.arange(0, 821, 15)
plt.plot(x_times, areas_list, marker = '.', linestyle = 'none')
plt.show()


# Curvefit
def area(t, r, a_0):
    #A0 = props_list[0][0].are
    A0 = a_0
    A1 = A0 * np.exp(np.exp(r) * np.exp(t))
    return A1


p0 = (np.log(2), np.log(12))

scipy.optimize.curve_fit(area, x_times, areas_list, p0 = p0)



#props[0].area
