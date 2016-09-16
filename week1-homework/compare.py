#!/usr/bin/env python

"""
Compare aa and nt sequences and add - to nt sequences according aa alignment results.

amino acid fasta file (with - ) in argument 1, nt fasta file in argument 2.
"""

import sys

aafile=open(sys.argv[1])
ntfile=open(sys.argv[2])

# aaline=aafile.readline()
# ntline=ntfile.readline()

aaseq=[]
ntseq=""
blanknt="---"

aaunit=aafile.read(1)
ntunit = "TAA"



while True:
    assert aaunit == ">"
    assert ntunit == "TAA"
    aaline=aafile.readline()
    ntline=ntfile.readline()    # both handles jump to sequence info
    aaunit=aafile.read(1)       # 1st aa n=1

    while aaunit != ">":
        if aaunit != "-":           # if aa is valid
            ntunit=ntfile.read(3)
            ntseq=ntseq+ntunit
            aaunit=aafile.read(1)
            if aaunit == "":
                break
            continue

        ntseq=ntseq+blanknt   # if aa is -, add --- to ntseq
        aaunit=aafile.read(1)
   
    ntline=ntfile.readline()
    print ntseq
    ntseq=""
    if aaunit == "":
        break

