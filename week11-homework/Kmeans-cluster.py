#!/usr/bin/env python

import sys
import scipy.cluster.hierarchy as hy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

hema_file=open("hema_data.txt")

datamap=[]
header=[]
label=[]
genes=[]
gene_dict={}

while True:
    line = hema_file.readline().rstrip("\r\n")
    if line == "":
        break
    if line.startswith("gene"):
        header= line.split('\t')
        continue
        
    fields=line.split("\t")
    datamap.append(line.rstrip('\n').split('\t')[1:])    
    genes.append(fields[0])
    #gene_dict(fields[0])=fields[1:]

matrix0 = np.matrix(datamap)
matrix = matrix0.astype(np.float)
#print matrix
plt.figure()

linkmatrix1=hy.linkage(matrix.transpose(),'complete')
label=header[1:]
kmeans_d = KMeans(n_clusters=7, random_state=0).fit(matrix)
labels = kmeans_d.labels_

count=0
for index,lbel in enumerate(labels):
	count=count+1
	if int(lbel) == 0:
		print(genes[index])
colors = ["g.","r.","y.","b.","m.","c.","k."]

for i in range(len(matrix)):
    plt.plot(matrix[i,0],matrix[i,1], colors[labels[i]], markersize = 5)

#plt.show()
#plt.savefig("Kmeans.png")