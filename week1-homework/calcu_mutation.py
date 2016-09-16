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

# generated codon table
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))
codon_table['GAY']="D"
codon_table['TAY']="Y"
codon_table['AAY']="N"
codon_table['RCT']="---"
codon_table['TYG']="---"
codon_table['WGG']="---"
codon_table['AAW']="---"
codon_table['CAR']="Q"
codon_table['CRC']="---"
codon_table['ACY']="T"
codon_table['RAC']="---"
codon_table['RCA']="---"
codon_table['RTG']="---"
codon_table['GCY']="A"
codon_table['YTG']="---"
codon_table['TCY']="S"
codon_table['GYA']="---"
codon_table['ARG']="---"

#print codon_table

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

#print triplet

aanum=len(triplet)    # number of aa
homonum=len(triplet[1])     # number of homologs

syn_l=[]
nonsyn_l=[]
zz=[]           # nonsyn - syn
ratio=[]        # nonsyn/syn

for i in range(1, aanum+1):    
    syn=0
    nonsyn=0
    for n in range(1,homonum):
        if triplet[i][0]=="---":    # if query is ---
            amino_acid="---"
        else:
            amino_acid=codon_table[triplet[i][0]] # take the AA for this site, homolog 1 as standard
        
        target=triplet[i][n]
        
        if target not in codon_table:  ### if target has R, Y, W... need further improvement on this line
            target="---"
        
        if amino_acid=="---":
            if target==amino_acid:
                syn=syn+1
                continue
            else:
                nonsyn=nonsyn+1
                continue
        
        if target=="---":       # if target is ---, while query is not
            nonsyn=nonsyn+1
            continue
            
        if codon_table[target]==amino_acid:
            syn=syn+1
        else:
            nonsyn=nonsyn+1    
    
    syn_l.append(syn)
    nonsyn_l.append(nonsyn)
    zz.append(nonsyn - syn)
    
    if syn==0:
        ratio.append(200)
    else:
        ratio.append(float(nonsyn/syn))
    #print syn
    #print nonsyn

#print syn_l
#print nonsyn_l

#print len(syn_l)
#print len(nonsyn_l)


import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from scipy.stats import norm
     
#print ratio
    
##
#   Z test
##

def zscore(x,average,stdev):
    return (x-average)/stdev

significant = []
sd = np.std(ratio)
for i,r in enumerate(ratio):
    z = zscore(r, 1, sd)
    #print z
    p = 1-norm.cdf(z,0,1)
    #print p
    if p < 0.05:
        significant.append([i,r])

x=list(range(0,len(ratio)))
significant = np.asarray(significant)
#print significant
#sprint significant


plt.figure()                       # Open blank canvas
plt.title("Nucleotide Positive Selection") # Add a title to the top
plt.scatter(                      # ... plot a bar of
    x,ratio,
    edgecolor='none',
    alpha=0.5                   # ... ... only the values corresponding to that species
    )


plt.scatter(significant[:,0],significant[:,1], color='r', edgecolor='none')

plt.ylabel("dN/dS")            # Label the y-axis
plt.xlabel("Nucleotide Positions")    
plt.savefig("Bar_selecton.png") # Save the figure






