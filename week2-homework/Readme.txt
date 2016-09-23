Homework for Week2
Xiuqi Chen

Kmer = 21mer

time velveth low/vel 21 -fastq -shortPaired -separate reads_low_1.fastq reads_low_2.fastq
    real    0m0.166s
    user    0m0.080s
    sys 0m0.058s

time velvetg low/vel
    real    0m0.239s
    user    0m0.175s
    sys 0m0.042s

time spades.py -1 reads_low_1.fastq -2 reads_low_2.fastq -o ./low/spa/ 
    real    0m6.125s
    user    0m8.032s
    sys 0m1.081s

contig_summary.txt
    is the summary of all four contig sets information. low_vel, low_spa, high_vel, high_spa

Sum_Contig.py
    is the python script I wrote to summary the contig set information.

./Sum_Contig.py low/vel/contigs.fa >> contig_summary.txt
./Sum_Contig.py low/spa/contigs.fasta >> contig_summary.txt 
    The two commands I used to summarize low contig sets.

time lastz low/vel/contigs.fa[multiple] reference.fasta[unmask] --chain --format=general:name1,start1,end1,size1,start2,end2,size2 > ./low_vel_data_plot.txt

real    0m4.185s
user    0m4.051s
sys 0m0.064s

time lastz low/spa/contigs.fasta[multiple] reference.fasta[unmask] --chain --format=general:name1,start1,end1,size1,start2,end2,size2 > ./low_spa_data_plot.txt

real    0m4.139s
user    0m3.988s
sys 0m0.074s

time lastz low/vel/contigs.fa[multiple] reference.fasta[unmask] --chain --format=rdotplot > ./test

real    0m4.236s
user    0m4.039s
sys 0m0.082s

time lastz low/spa/contigs.fasta[multiple] reference.fasta[unmask] --chain --format=rdotplot > ./test

real    0m4.299s
user    0m4.111s
sys 0m0.074s

time velveth high/vel 21 -fastq -shortPaired -separate reads_1.fastq reads_2.fastq

real    0m14.338s
user    0m13.362s
sys 0m0.560s

time velvetg high/vel

real    0m30.745s
user    0m29.585s
sys 0m0.596s

time spades.py -1 reads_1.fastq -2 reads_2.fastq -o ./high/spa/

real    3m31.363s
user    9m34.121s
sys 0m25.139s

./Sum_Contig.py high/vel/contigs.fa >> contig_summary.txt
./Sum_Contig.py high/spa/contigs.fasta >> contig_summary.txt


time lastz high/vel/contigs.fa[multiple] reference.fasta[unmask] --chain --format=rdotplot > ./test

real    0m4.524s
user    0m4.414s
sys 0m0.061s

time lastz high/spa/contigs.fasta[multiple] reference.fasta[unmask] --chain --format=rdotplot > ./test

real    0m4.883s
user    0m4.695s
sys 0m0.107s

quast.py ./low/vel/contigs.fa low/spa/contigs.fasta ./high/vel/contigs.fa high/spa/contigs.fasta

