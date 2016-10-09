Week3 - Homework
Xiuqi Chen
9.23.2016


wget ftp://hgdownload.cse.ucsc.edu/goldenPath/mm9/chromosomes/chr4.fa.gz

wget ftp://hgdownload.cse.ucsc.edu/goldenPath/mm9/chromosomes/chr7.fa.gz

wget ftp://hgdownload.cse.ucsc.edu/goldenPath/mm9/chromosomes/chr11.fa.gz

cat chr4.fa chr7.fa chr11.fa > ref-4_7_11.fa

time bwa index ref-4_7_11.fa

real    10m4.144s
user    9m44.295s
sys 0m8.784s

brew install freebayes


time bwa mem -R '@RG\tID:1449\tSM:1449' ref/ref-4_7_11.fa chd/1449_002_LA.region.fq > 1449_002_LA-aln-sq.bam

real    0m4.822s
user    0m3.100s
sys 0m1.359s

time bwa mem -R '@RG\tID:1526\tSM:1526' ref/ref-4_7_11.fa chd/1526_007_LA.region.fq > 1526_007_LA-aln-sq.sam

real    0m5.525s
user    0m3.190s
sys 0m1.803s

time bwa mem -R '@RG\tID:183\tSM:183' ref/ref-4_7_11.fa chd/183-005-NB.region.fq > 183_005_NB-aln-sq.sam

real    0m3.712s
user    0m2.115s
sys 0m1.023s

samtools view -b 1449_002_LA-aln-sq.sam -o 1449_002_LA-aln-sq.bam
samtools view -b 1526_007_LA-aln-sq.sam -o 1526_007_LA-aln-sq.bam
samtools view -b 183_005_NB-aln-sq.sam -o 183_005_NB-aln-sq.bam

samtools sort 1449_002_LA-aln-sq.bam -o 1449_002_LA-aln-sq-sorted.bam
samtools sort 1526_007_LA-aln-sq.bam -o 1526_007_LA-aln-sq-sorted.bam
samtools sort 183_005_NB-aln-sq.bam -o 183_005_NB-aln-sq-sorted.bam


time freebayes -f ref/ref-4_7_11.fa 1449_002_LA-aln-sq-sorted.bam > 1449_var.vcf

real    1m44.395s
user    1m42.571s
sys 0m1.305s

time freebayes -f ref/ref-4_7_11.fa 1526_007_LA-aln-sq-sorted.bam > 1526_var.vcf

real    1m43.887s
user    1m41.762s
sys 0m1.147s

time freebayes -f ref/ref-4_7_11.fa 183_005_NB-aln-sq-sorted.bam > 183_var.vcf

real    1m41.081s
user    1m38.015s
sys 0m1.672s

wget http://downloads.sourceforge.net/project/snpeff/snpEff_v3_6_core.zip
unzip snpEff_v3_6_core.zip
java -jar snpEff/snpEff.jar download GRCm37.67


time freebayes --min-alternate-count 5 --min-alternate-fraction 0.2 -f ref/ref-4_7_11.fa 1449_002_LA-aln-sq-sorted.bam > 1449_var-filtered.vcf

real	3m30.581s
user	2m38.857s
sys	0m6.915s

time freebayes --min-alternate-count 5 --min-alternate-fraction 0.2 -f ref/ref-4_7_11.fa 1526_007_LA-aln-sq-sorted.bam > 1526_var-filtered.vcf

real	3m32.692s
user	2m41.691s
sys	0m6.762s

time freebayes --min-alternate-count 5 --min-alternate-fraction 0.2 -f ref/ref-4_7_11.fa 183_005_NB-aln-sq-sorted.bam > 183_var-filtered.vcf

real	3m23.098s
user	2m34.080s
sys	0m6.578s

java -jar snpEff/snpEff.jar GRCm37.67 1449_var-filtered.vcf > 1449_var-filtered-anno.vcf
java -jar snpEff/snpEff.jar GRCm37.67 1526_var-filtered.vcf > 1526_var-filtered-anno.vcf
java -jar snpEff/snpEff.jar GRCm37.67 183_var-filtered.vcf > 183_var-filtered-anno.vcf

###############################
Problem:

java -Xmx1g -jar snpEff/snpEff.jar GRCm37.67 1449_var-filtered.vcf > 1449_var-filtered-anno.vcf
java.lang.OutOfMemoryError: GC overhead limit exceeded
	at java.lang.Integer.valueOf(Integer.java:832)
	at ca.mcgill.mcb.pcingola.interval.tree.IntervalNode.<init>(IntervalNode.java:45)
	at ca.mcgill.mcb.pcingola.interval.tree.IntervalNode.<init>(IntervalNode.java:74)
	at ca.mcgill.mcb.pcingola.interval.tree.IntervalTree.build(IntervalTree.java:67)
	at ca.mcgill.mcb.pcingola.interval.tree.IntervalForest.build(IntervalForest.java:65)
	at ca.mcgill.mcb.pcingola.snpEffect.SnpEffectPredictor.buildForest(SnpEffectPredictor.java:156)
	at ca.mcgill.mcb.pcingola.snpEffect.commandLine.SnpEff.loadDb(SnpEff.java:357)
	at ca.mcgill.mcb.pcingola.snpEffect.commandLine.SnpEffCmdEff.run(SnpEffCmdEff.java:734)
	at ca.mcgill.mcb.pcingola.snpEffect.commandLine.SnpEffCmdEff.run(SnpEffCmdEff.java:713)
	at ca.mcgill.mcb.pcingola.snpEffect.commandLine.SnpEff.run(SnpEff.java:685)
	at ca.mcgill.mcb.pcingola.snpEffect.commandLine.SnpEff.main(SnpEff.java:118)

