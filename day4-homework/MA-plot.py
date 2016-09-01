#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

r=df["FPKM"].values+1
g=df2["FPKM"].values+1

#print len(r)
#print len(g)

m=np.log2(r/g)
a=0.5* np.log2(r*g)



plt.figure()
plt.scatter(a,m, alpha=0.3)

plt.title("SRR072893-SRR072915 MA-plot", size=20)
#plt.xticks(range(len(stages)),stages)
#locs, labels = plt.xticks()
#plt.setp(labels, rotation=90)
#plt.xlabel("developmental stage",size=20)
#plt.ylabel("mRNA abundance (FPKM)",size=20)
#plt.legend(loc="upper left")
#plt.xlim([-1,8])
plt.subplots_adjust(left=0.2, bottom=0.15, top=0.85,right=0.85)
plt.savefig("myMA-plot.png")    
plt.close()