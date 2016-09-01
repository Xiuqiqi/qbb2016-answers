#!/usr/bin/env python

""""
Read sequences from a fasta file, for each sequence,
match Kmer in Query and Target acquiring the positions meanwhile.
Then each matched kmer will extend on either end to find the longest exact match.


usage: kmer_matcher.py <target.fa> <query.fa> <k>

"""

import sys
import fasta

#command line argument
target_file = open(sys.argv[1])
query_file = open(sys.argv[2])
k=int(sys.argv[3])
query={}

# Generating the query hash table.

for ident, sequence in fasta.FASTAReader(query_file):
    q_sequence = sequence.upper()
    for i in range(0,len(sequence)-k):
        kmer = q_sequence[i:i+k]
        position=i+1
        if kmer not in query:
            query[kmer]=[]
            query[kmer].append(position)
            continue
        # save position number into list
        query[kmer].append(position)


#print query
#print fasta.FASTAReader(query_file)
#q_sequence=q_sequence.upper()
#print sequence
#Search in Targe seq

qt_match={}

for ident, sequence in fasta.FASTAReader(target_file):#for each gene
    t_sequence = sequence.upper()
    #print t_sequence
    for i in range(0,len(sequence)-k): #for each target hit
        kmer_t=t_sequence[i:i+k]
        t_position=i+1
        if kmer_t in query:
            target_gene_name=ident
            #target_start=position_t
            query_start=query[kmer_t]
            #print "\t".join([target_gene_name, target_start, query_start, kmer_t])           
            for q_hit in range(0, len(query_start)): #For one target hit on each query
                q_position=query_start[q_hit] # the query start position
                match=k
                l_cursor=1
                while l_cursor:    #left side  # ensure >0?????
                    if q_position-l_cursor-1==-1 or t_position-l_cursor-1==-1:
                        break
                    if  q_sequence[q_position-l_cursor-1] == t_sequence[t_position-l_cursor-1]: 
                        l_cursor=l_cursor+1
                    else:
                        break
                match=match+l_cursor-1
                
                r_cursor=1
                while r_cursor: #right side
                    if q_position+r_cursor-1==len(q_sequence) or t_position+r_cursor-1==len(t_sequence):
                        break
                    if  q_sequence[q_position+r_cursor-1] == t_sequence[t_position+r_cursor-1]: 
                        r_cursor = r_cursor+1
                    else:
                        break
                match=match+r_cursor-1
                seed=q_sequence[q_position-1-l_cursor+1 : q_position-1+k+r_cursor]
                query_position=q_position-1-l_cursor+1+1
                target_position=t_position-1-l_cursor+1+1
                qt_match[seed]=match ##
                
                
    print target_gene_name, "\t", "10 longest seed match:"
    view = sorted(qt_match, key=qt_match.get, reverse=True)# 10 longest 
    for ii in range(0,10):
        print view[ii]


""""    
    for i, kmer in enumerate(sorted(kmer_counts, key=kmer_counts.get,reverse=True)):
        if i>=10:
            break
        print kmer, kmer_counts[kmer]
    
#for kmer in sorted(kmer_counts, key=kmer_counts.get,reverse=True):
#    print kmer, kmer_counts[kmer]
    
#for kmer, count in sorted(kmer_counts.iteritems()):    
#    print kmer, count
"""