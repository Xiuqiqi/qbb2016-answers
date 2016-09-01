#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

#get the lines with Sxl
df_roi=df["gene_name"]=="Sxl"
df_sxl=df[df_roi]
#get the lines with FPKM>0
df_roi=df_sxl["FPKM"]>0
df_sxl=df_sxl[df_roi]
y1=np.log10(df_sxl["FPKM"])


#get the lines with Sxl
df2_roi=df2["gene_name"]=="Sxl"
df2_sxl=df2[df2_roi]
#get the lines with FPKM>0
df2_roi=df2_sxl["FPKM"]>0
df2_sxl=df2_sxl[df2_roi]
y2=np.log10(df2_sxl["FPKM"])


plt.figure()
#plt.semilogy(df_sxl)
plt.boxplot([y1,y2],labels=["SRR072893", "SRR072915"])
plt.xlabel("Developmental Stages")
plt.ylabel("lg(FPKM)")

plt.title("Abundance for Sxl isoforms in different developmental stages")
plt.savefig("box")
plt.close

# Merge the two files

#dfMerge=

#smoothed = df_chrom["FPKM"].rolling(200).mean()
#print smoothed
#print type(smoothed)

# plt.figure()
# plt.plot(smoothed)
# plt.title("Chromosome 4L, FPKM rolling mean (size=200)")
# plt.savefig("smoothed.png")
# plt.close
