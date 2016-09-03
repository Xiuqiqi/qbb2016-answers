#!/usr/bin/env python

import sys

for line in sys.stdin:
    if line.startswith("\n"):
        continue
    fields=line.rstrip("\r\n").split("; ")
    for i in range(0,len(fields)):
        attri=fields[i].split(" ")
        print "\t".join(attri)
    
    #print len(fields)
    #print fields[0]
    #print fields[1]
    
#print fields[0]
#print fields[1]
#print fields[3]
#    for ele in fields:
#        attri = ele.split(" ")
#        print attri[1]
#        print attri[2]

