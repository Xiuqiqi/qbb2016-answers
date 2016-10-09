#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

myfile=open(sys.argv[1])

x = []
y = []

while True:
    line = myfile.readline().rstrip("\r\n")
    if line == "":
        break
    if line.startswith("#"):
        continue
    
    fields=line.split(" ")
    #print fields
    x.append(fields[2])
    y.append(fields[3])
    
plt.scatter(x,y)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("2D Principle Component Analysis")
#plt.show()
plt.savefig("PCA.png")