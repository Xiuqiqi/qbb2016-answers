#!/usr/bin/env python

""""
Read sequences from a fasta file, for each sequence,
match Kmer in Query and Target.
Print target seq_name, target start position, query start position and Kmer seq. separated by <TAB>
if there is more than one position in query, the positions are separated by a single space.


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
    sequence = sequence.upper()
    for i in range(0,len(sequence)-k):
        kmer = sequence[i:i+k]
        position=i+1
        if kmer not in query:
            query[kmer]=[]
            query[kmer].append(position)
            continue
        # save position number into list
        query[kmer].append(position)
    
#print query

#Search in Targe seq

for ident, sequence in fasta.FASTAReader(target_file):
    sequence = sequence.upper()
    for i in range(0,len(sequence)-k):
        kmer_t=sequence[i:i+k]
        position_t=i+1
        if kmer_t in query:
            target_gene_name=ident
            target_start=str(position_t)
            query_start=" ".join(map(str,query[kmer_t]))
            print "\t".join([target_gene_name, target_start, query_start, kmer_t])



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