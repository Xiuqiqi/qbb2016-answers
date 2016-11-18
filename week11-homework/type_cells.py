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

matrix0 = np.matrix(datamap)
matrix = matrix0.astype(np.float)
#print matrix

linkmatrix1=hy.linkage(matrix.transpose(),'complete')
label=header[1:]
#print label
###### Dendrogram
plt.figure(figsize=(25, 10))
plt.title('Dendrogram of Cell Type')
plt.xlabel('Distance')
plt.ylabel('Cell type')
hy.dendrogram(
    linkmatrix1,
    leaf_rotation=0.,  # rotates the x axis labels
    leaf_font_size=20,  # font size for the x axis labels
    labels=label,
    orientation='right'
)
#plt.show()
plt.savefig('cell_type.png')
#######





