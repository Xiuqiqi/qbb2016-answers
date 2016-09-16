#!/usr/bin/env python

import sys
import fasta

reader = fasta.FASTAReader(sys.stdin)
    
while True:
    mybool, identifier, sequence=reader.next()
    print ">", identifier
    print sequence
    if mybool is False:
        break