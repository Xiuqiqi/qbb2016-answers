#!/usr/bin/env python

import sys

for line in sys.stdin:
    #print line
    fields = line.rstrip("\r\n").split("\t")
    #print fields[6]
    if fields[5] == "1":
        if fields[6] == "10293":
            print "\t".join([fields[0], fields[2], fields[7]])
    #print fields