#!/usr/bin/env python

import sys
import h5py
import numpy
import hifive

file = h5py.File("Out2.heat",'r')


file.keys()
[u'0.counts', u'0.expected', u'0.positions', u'regions']


counts = file['0.counts'][...]
expected = file['0.expected'][...]
posi = file['0.positions'][...]

#print counts.shape
default=-10

enrichment = numpy.zeros((counts.shape), dtype=numpy.float32) + default
nonzeros = numpy.zeros((counts.shape), dtype=numpy.float32)


where = numpy.where(counts > 0)

enrichment[where] = numpy.log(counts[where] / expected[where])
nonzeros[where] = 1

#print enrichment



ctcf_file=open("ctcf_peaks.tsv")
ctcf_posi=[]
while True:
    line = ctcf_file.readline().rstrip("\r\n")
    if line == "":
        break
    if line.startswith("#"):
        continue
        
    fields=line.split("\t")

    if fields[0] == "chrX":
        ctcf_posi.append(int(fields[1]))

ctcf_posi.sort()

posi_min = posi[0][0]
posi_max = posi[-1][1]
ctcf_peaks=[]

for i in range(0,len(ctcf_posi)):
    if ctcf_posi[i] < posi_min:
        continue
    if ctcf_posi[i] > posi_max:
        continue
    
    position=ctcf_posi[i]/10000-posi_min/10000    
    ctcf_peaks.append(position)

print "#1st fragment"+"\t"+"2nd fragment"
for i in ctcf_peaks:
    for j in ctcf_peaks:
        if enrichment[i,j]==max(enrichment[i,ctcf_peaks]):
            if max(enrichment[i,ctcf_peaks]) == default:
                continue
            print str(posi[i])+"\t"+str(posi[j])


#print posi
#print ctcf_posi



#if line.startswith("C"):


