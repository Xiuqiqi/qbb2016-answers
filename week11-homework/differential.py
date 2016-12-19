#!/usr/bin/env python

import sys
import scipy.cluster.hierarchy as hy
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel


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
## 0 is CFU
## 4 is mys

## 1 is poly
## 2 is unk
enriched=[]
regulated=[]
for index, row in enumerate(matrix):
    #print row[0,1]
    a = (row[0,0]+row[0,4])/2
    b = (row[0,1]+row[0,2])/2
    ratio = b/a
    if ratio>2 or ratio <0.5:
        enriched.append(index)
        regulated.append(ratio)
#print enriched
#print regulated
sigEnrich=[]
sigRegulated=[]

for number,t in enumerate(enriched):
    a = [matrix[number,0],matrix[number,4]]
    b = [matrix[number,1],matrix[number,2]]
    p = ttest_rel(a,b)
    if p[1] < 0.05:
         sigEnrich.append(genes[number])
         sigRegulated.append(enriched[number])
         
#t, p = ttest_rel([np.float32(x) for x in matrix[:,1]],[np.float32(x) for x in matrix[:,0]])

for i in sigEnrich:
    print i
print
print
ratios = np.array(regulated)
#print ratios
index_max = np.argmax(ratios)
print sigEnrich[index_max]
# for index,label in enumerate(p):
#     if p[index] <0.05:
#         print(genes[index])
#print p
#print t
