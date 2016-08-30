#!/usr/bin/env python

import sys

n=0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    n=n+1
    
print n





