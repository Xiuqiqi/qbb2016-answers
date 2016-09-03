#!/usr/bin/env python

import sys

n=0
s=0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    fields=line.rstrip("\r\n").split("\t")
    if fields[2]=="*":
        continue
    if fields[4]=="255":
        continue
    s=s+int(fields[4])
    n=n+1
    
print float(s/n)