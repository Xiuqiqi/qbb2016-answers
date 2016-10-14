#!/usr/bin/env python

import sys

myfile=open(sys.argv[1])

x = [] ##    A1


while True:
    line = myfile.readline().rstrip("\r\n")
    if line == "":
        break
        
    fields=line.split("\t")
    print "\t".join(fields[0:6])
    