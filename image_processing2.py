import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Instead of context manager (with):
sns.set_style('dark')

import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation

# Load an example phase image.
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

# Show the image.
plt.imshow(phase_im, cmap=plt.cm.viridis)
plt.show()

#We're doing this stuff to deal with illumination uneveness
# Apply a |Gaussian!!! blur to the image.
im_blur = skimage.filters.gaussian(phase_im, 50.0)
plt.imshow(im_blur, cmap = plt.cm.viridis)
#Background subtraction:
#Convert phase image to float:
phase_float = skimage.img_as_float(phase_im)
#Do subtraction
phase_sub = phase_float - im_blur

#Show em
plt.close()
plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('original')

plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtracted')

#Plot otsu threshold
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh

#Label em
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)
plt.close()
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)

#plt.imshow(seg_lab==6)

# Compute the region properties and extract area of each object.
ip_dist = 0.063 #microns per pixel
props = skimage.measure.regionprops(seg_lab)

#props[0].area

# Get the areas as an array:
areas = np.array([prop.area for prop in props])
cutoff = 300

# Copy to preserve original data (something about array)
im_cells = np.copy(seg_lab) > 0
for i, _ in enumerate(areas):
    if areas[i] < cutoff:
        #Sets these pixels to zero:
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)

plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)
