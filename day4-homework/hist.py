#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_table(sys.argv[1])
df_roi=df["FPKM"]!=0

names=df[df_roi]["t_name"].values   # list of strings
x=np.log10(df[df_roi]["FPKM"])  #

minimum = np.min(x)           # Grab the minimum...
maximum = np.max(x) 

plt.figure()
   
plt.hist(                      # ... plot a histogram of
		x,                   # ... ... only the values corresponding to that species
		bins=100,                   # ... ... Use thirty bars
		#range=[minimum,maximum],   # ... ... ranging from the minimum to the maximum
		#normed=True,               # ... ... Normalize the bars to frequencies instead of counts
		#label=names[i],          # ... ... Assign the corresponding species name as the label
		#alpha=0.5                  # ... ... Make the bars only 50% opaque
		)                  



plt.title("FPKM values for SRR072893", size=20)

#plt.xticks(range(len(names)),names)

#locs, labels = plt.xticks()
#plt.setp(labels, rotation=90)

#plt.xlabel("Transcripts Names")
plt.ylabel("mRNA abundance (FPKM)",size=20)
plt.legend(loc="upper left")

#plt.xlim([-1,8])
plt.subplots_adjust(left=0.2, bottom=0.15, top=0.85,right=0.85)
plt.savefig("histgram.png")    
plt.close()
