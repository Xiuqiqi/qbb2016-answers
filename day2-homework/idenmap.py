#!/usr/bin/env python

import sys

# User-generated mapping file as first input Arg
# t_data.ctab file as second input Arg
# char a or b as third Arg to indicate ignore or print default if not found.

# There are blanks in mapping file, some without coressponding Flybase ID

#first generate Hash table for the mapping information

geneMap_handle=open(sys.argv[1])
geneMap = geneMap_handle.readlines()
# readlines will read files in lines. read will read the file in char.

geneDic = {}

ctab_handle=open(sys.argv[2])
ctab=ctab_handle.readlines()

doWhat=sys.argv[3]

for line in geneMap:
    fields=line.rstrip("\r\n").split("\t")
    geneDic[fields[0]]=fields[1]
# Generated the Hash Table

for i,line in enumerate(ctab):
    if i==0:
        continue
    fields=line.rstrip("\r\n").split("\t")
    if fields[8] not in geneDic:
        if doWhat == 'a':
            continue
        if doWhat == 'b':
            fields.append("*") 
            print "\t".join(fields)
        continue
    fields.append(geneDic[fields[8]]) 
    print "\t".join(fields)


