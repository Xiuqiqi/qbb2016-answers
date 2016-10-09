#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

myfile=open(sys.argv[1])

x = []

while True:
    line = myfile.readline().rstrip("\r\n")
    if line == "":
        break
    if line.startswith("\t"):
        fields1=line.split("\t")
        fields = ["FID","IID"]
        fields.extend(fields1[1:])
        print "\t".join(fields)
        continue
            
    fields1=line.split("\t")
    #print fields1
    idd = fields1[0].split("_")
    #print idd
    idd.extend(fields1[1:])
    print "\t".join(idd)
    
    