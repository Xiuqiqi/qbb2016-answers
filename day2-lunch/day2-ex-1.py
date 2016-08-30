#!/usr/bin/env python

import sys

n=0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    fields=line.rstrip("\r\n").split("\t")
    if fields[2] == "*":
        continue
    n=n+1
    
print n





