#!/usr/bin/env python

import sys

for line in sys.stdin:
    #print line
    fields = line.rstrip("\r\n").split("\t")
    print "\t".join([">", fields[0], fields[1]])
    print fields[2].replace("-","")