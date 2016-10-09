
brew install plink2

wget ...


plink2 --vcf BYxRM_GenoData.vcf --pca 2

./PCA.py plink.eigenvec

plink2 --vcf BYxRM_GenoData.vcf --freqx

./Allele.py plink.frqx

./transPheno.py BYxRM_PhenoData.txt > Pheno.pheno

plink2 -assoc --allow-no-sex --all-pheno --pheno Pheno.pheno --vcf BYxRM_GenoData.vcf

./Manhattan.py *.qassoc