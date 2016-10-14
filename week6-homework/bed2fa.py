#!/usr/bin/env python

import sys


myfile=open(sys.argv[1])

sequences = []

while True:
    line = myfile.readline().rstrip("\r\n")
    if line == "":
        break
    if line.startswith(">"):
        continue

    sequences.append(line)

sequence = "".join(sequences)
#print sequence

mybed=open(sys.argv[2])

while True:
    line = mybed.readline().rstrip("\r\n")
    if line == "":
        break
    fields=line.split("\t")
    
    print ">"+fields[3]
    print sequence[int(fields[1]):int(fields[2])]

    


