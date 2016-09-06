#!/usr/bin/env python

import sys

n=0
flag_1=256
flag_2=16
#print "asb"
for line in sys.stdin:
    if line.startswith("@"):
        continue
    fields=line.rstrip("\r\n").split("\t")
    
    if (int(fields[1]) & flag_1):    # Take out secondary mapping (Multiple mappings)
        continue
    
    qvalue=0
    for mychar in fields[10]:
        qvalue = qvalue + ord(mychar) - 33
    qvalue=qvalue/len(fields[10])    
    
    if qvalue>30:
        n=n+1
    
print n