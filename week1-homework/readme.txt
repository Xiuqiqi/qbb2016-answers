Week1 Homework Explanations
Xiuqi Chen
2016.9.15

This file chronically describes how I did the homework, including the files I generated and the commands I used.


fasta.py & fast.pyc
	are the FASTAParser we constructed in bootcamp

week1_query.fa 
    is the query provided for BLAST in NCBI to acquire

blastn -remote -evalue 0.0001 -db nr -query week1_query.fa -outfmt "6 sseqid length pident gaps evalue qstart qend sseq"  -out out2.blst -num_alignments 1000
    The command I used to BLAST     

out2.blst 
    is the output file from BLAST.

refine_blast.py
	This script take in the raw output from BLAST and extract the name, length and sequences from each result. Sequnce in single line.

refined.blst
	The output of last script.
 
blast_nucleotides.py
    Take the refined.blst and convert the file into FASTA file.
    More importantly, this script takes out the "-" from the sequence

blast_final.fa
    is the output from last script.

transeq blast.fa AA.pep
    The command I used to convert the nucleotide info from blast.fa to AA info.

AA.pep
	is the peptide file generated from last command.

mafft AA.pep > mult-align
	is the command line I used for MAFFT alignment.

mult-align
	is the output from the last command.

refine_mult.py
	used fasta.py and convert multi-align to single line AA info.

compare.py
	this takes multi.fa & blast_final.fa and compare the two files.
	Add --- to nt seq according to one - in aa seq.

compared_nt
	is the output of compare.py. multiple single-line nt seq with --- added.

calcu_mutation.py
	takes multi.fa & blast_final.fa and compare the two files.
	add --- to nt seq according to one - in aa seq.
	build triplet dictionary and calculate mutation & plot.
