#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

df = pd.read_table(sys.argv[1])
df =df["FPKM"].values

density=gaussian_kde(df)

xs = np.linspace(0,100,500)
density.covariance_factor = lambda : .25
density._compute_covariance()


plt.figure()
plt.plot(xs,density(xs))

plt.title("FPKM values for SRR072893", size=20)

#plt.xticks(range(len(names)),names)

#locs, labels = plt.xticks()
#plt.setp(labels, rotation=90)

plt.xlabel("FPKM Values")
plt.ylabel("Density",size=20)
#plt.legend(loc="upper left")

#plt.xlim([-1,8])
plt.subplots_adjust(left=0.2, bottom=0.15, top=0.85,right=0.85)
plt.savefig("densityMap.png")    
plt.close()

