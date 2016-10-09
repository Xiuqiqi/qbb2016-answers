#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

myfile=open(sys.argv[1])

x = [] ##    A1


while True:
    line = myfile.readline().rstrip("\r\n")
    if line == "":
        break
    if line.startswith("C"):
        continue
        
    fields=line.split("\t")
    
    #x1.append(fields[4])
    #x2.append(fields[6])

    sum = float(fields[4])+float(fields[6])
    freq = float(fields[4])/sum
    x.append(freq)

#print x

plt.hist(x, bins=60)
plt.xlabel("SNPs")
plt.ylabel("Significance of Association")
plt.title("Allele Frequency")
#plt.show()
plt.savefig("AllelFreq.png")