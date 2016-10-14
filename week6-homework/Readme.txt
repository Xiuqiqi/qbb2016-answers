Week6
Xiuqi Chen
2016.10.14


bowtie2-build chr19.fa mm9_chr19

bowtie2 -x mm9_chr19 -U CTCF_ER4.fastq -S CTCF_ER4.sam
bowtie2 -x mm9_chr19 -U CTCF_G1E.fastq -S CTCF_G1E.sam
bowtie2 -x mm9_chr19 -U input_ER4.fastq -S input_ER4.sam
bowtie2 -x mm9_chr19 -U input_G1E.fastq -S input_G1E.sam

macs2 callpeak -t CTCF_ER4.sam -c input_ER4.sam -n ER4 -outdir ER4
macs2 callpeak -t CTCF_G1E.sam -c input_G1E.sam -n G1E -outdir G1E

./peak2BED.py ER4/ER4_peaks.narrowPeak > ER4_peaks.bed
./peak2BED.py G1E/G1E_peaks.narrowPeak > G1E_peaks.bed

bedtools subtract -A -a ER4_peaks.bed -b G1E_peaks.bed > CTCF_gain.bed	
bedtools subtract -A -a G1E_peaks.bed -b ER4_peaks.bed > CTCF_lost.bed

sort ER4_peaks.bed -k5 -r -n > sorted_ER4_peaks.bed
head -100 sorted_ER4_peaks.bed > 100sorted.bed

./bed2fa.py ref/mm9_chr19.fa ER4_peaks.bed > ER4_peaks.fa

./bed2fa.py ref/mm9_chr19.fa 100sorted.bed > 100_ER4_peaks.fa

/usr/local/opt/meme/bin/meme-chip -db motif_databases/JASPAR/JASPAR_CORE_2016.meme -meme-maxw 20 100_ER4_peaks.fa 


