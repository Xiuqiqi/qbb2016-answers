#!/usr/bin/env python

import sys

n=0
i=0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    if i>9:
        break
    fields=line.rstrip("\r\n").split("\t")
    if fields[2]=="*":
        continue
    print fields[2]
    i=i+1
    
    #print line
