#!/usr/bin/env python

import sys
import scipy.cluster.hierarchy as hy
import numpy as np
import matplotlib.pyplot as plt


hema_file=open("hema_data.txt")

datamap=[]
header=[]
label=[]

while True:
    line = hema_file.readline().rstrip("\r\n")
    if line == "":
        break
    if line.startswith("gene"):
        header= line.split('\t')
        continue
        
    fields=line.split("\t")
    datamap.append(line.rstrip('\n').split('\t')[1:])    

####### Clustering according to Gene Expression
matrix0 = np.matrix(datamap)
matrix = matrix0.astype(np.float)
dataMatrix=matrix
#print matrix

linkmatrix1=hy.linkage(dataMatrix,'complete')
label=header[1:]

heatmapOrder = hy.leaves_list(linkmatrix1)
orderedDataMatrix = dataMatrix[heatmapOrder,:]
# rowHeaders = np.array(label)
# orderedRowHeaders = rowHeaders[heatmapOrder,:]


###### Clustering according to Cell Type

matrix = orderedDataMatrix
dataMatrix=matrix.transpose()
linkmatrix1=hy.linkage(dataMatrix,'complete')
heatmapOrder = hy.leaves_list(linkmatrix1)
orderedDataMatrix = dataMatrix[heatmapOrder,:]

label = np.array(label)[heatmapOrder]


######## plot the Heatmatp
# Make the actual plot
plt.figure()                                 # Open a blank canvas
plt.title("Heatmap of differential expression") # Add a title to the top
plt.imshow(                                  # Treat the values like pixel intensities in a picture
	orderedDataMatrix.T,                                       # ... Using X as the values
	aspect='auto',                           # ... 'Stretch' the image to fit the canvas, so you don't get a skinny strip that is 4x150 pixels
	interpolation='nearest',                 # ... Don't use any blending between pixel values
	cmap="RdBu",                             # ... Use the Red-white-blue colormap to assign colors to your pixel values
	#vmin=-1*m,                               # ... Set the lowest value to show on the scale
	#vmax=m,                                  # ... Set the highest value to show on the scale. Since we are using a 'diverging' colormap, these should match.
	)
plt.grid(False)        # Turn of the grid lines (a feature added automatically by ggplot)
plt.xticks(            # Edit the xticks being shown
	range(orderedDataMatrix.T.shape[1]), # ... use the values centered on each column of pixels
	label,            # ... which corresponds to the indices of our labels
	rotation=50,       # ... and rotate the labels 50 degrees counter-clockwise
	)
plt.yticks([])         # Edit the ticks on the y-axis to show....NOTHING
plt.colorbar()         # Add a bar to the right side of the plot which shows the scale correlating the colors to the pixel values

#plt.savefig("1D-cluster.png")
#plt.show()
plt.savefig("2D-cluster-Heatmap.png")

# plt.subplots_adjust( # Adjust the spacing of the subplots, to help make everything fit
#     left = 0.05,     # ... the left edge of the left-most plot will be this percent of the way across the width of the plot
#     bottom = 0.15,   # ... the bottom edge of the bottom-most plot will be this percent of the way up the canvas
#     right = 1.0,     # ... the right edge of the right-most plot will be this percent of the way across the width
#     top = 0.95,      # ... the top edge of the top-most plot will be this percent of the way from the bottom
# )



