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

codon={             ##############finish all the codon map##############
    "UUU":"F",
    "UUC":"F"
}

triplet={}

while True:
    assert aaunit == ">"
    assert ntunit == "TAA"
    aaline=aafile.readline()
    ntline=ntfile.readline()    # both handles jump to sequence info
    aaunit=aafile.read(1)       # 1st aa n=1
    n=1
    
    while aaunit != ">":
        if aaunit != "-":           # if aa is valid
            ntunit=ntfile.read(3)
            if n not in triplet:
                triplet[n]=[ntunit]
            else:
                triplet[n].append(ntunit)
            #ntseq=ntseq+ntunit
            aaunit=aafile.read(1)   # next aa
            n=n+1
            if aaunit == "":
                break
            continue
            
        if n not in triplet:
            triplet[n]=["---"]
        else:
            triplet[n].append("---")
            
        #ntseq=ntseq+blanknt   # if aa is -, add --- to ntseq
        
        aaunit=aafile.read(1)       # next aa
        n=n+1
   
    ntline=ntfile.readline()

    #ntseq=""
    if aaunit == "":
        break
#print len(triplet[1])

#####
# Calculate 
###

aanum=len(triplet[1][1])    # number of aa
homonum=len(triplet[1])     # number of homologs



for i in range(1, aanum+1)    
    syn=0
    nonsyn=0
    for n in range(1,homonum):
        amino_acid=codon[triplet[i][0]] # take the AA for this site
        if codon[triplet[i][n]]==amino_acid:
            syn=syn+1
        else:
            nonsyn=nonsyn+1    
    ratio=nonsyn/syn
    
##
#   Z test
##







