#!/usr/bin/env python

import sys

n=0
flag_1=256
#print "asb"
for line in sys.stdin:
    if line.startswith("@"):
        continue
    fields=line.rstrip("\r\n").split("\t")
    
    if fields[2]=="2L":
        if int(fields[3]) in range(10000, 20001):
            n=n+1
            #print "\t".join(fields)
    if (int(fields[1]) & flag_1):    # Take out secondary mapping (Multiple mappings)
        continue

print n