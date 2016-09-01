#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])
windowSize=int(sys.argv[3])

chromo=["2L","2R","3L","3R","4","X"]

for i in range(0,6): #6 is the final
    #get the lines with chr
    df_roi=df["chr"]==chromo[i]
    df_chr=df[df_roi]
    y1 = df_chr["FPKM"].rolling(windowSize).mean()
    
    #get the lines with chr
    df2_roi=df2["chr"]==chromo[i]
    df2_chr=df2[df2_roi]
    y2 = df2_chr["FPKM"].rolling(windowSize).mean()
    
    plt.figure()
    plt.plot(y1,color="Red")
    plt.plot(y2,color="Green")
    plt.legend()
    plt.title("Chromosome {}, FPKM rolling mean (size={})".format(chromo[i],windowSize))
    plt.savefig("chr_roll_{}.png".format(chromo[i]))
    plt.close
    


# plt.figure()
# plt.boxplot([y1,y2],labels=["SRR072893", "SRR072915"])
# plt.xlabel("Developmental Stages")
# plt.ylabel("lg(FPKM)")
# plt.title("Abundance for Sxl isoforms in different developmental stages")
# plt.savefig("box")
# plt.close
# Merge the two files

#dfMerge=

#smoothed = df_chrom["FPKM"].rolling(200).mean()
#print smoothed
#print type(smoothed)

