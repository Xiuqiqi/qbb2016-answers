#!/usr/bin/env python

import sys

sam = open("/Users/cmdb/data/day1-homework/Map.sam")


n=0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    n=n+1
    
print n





