#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# The output columns of BigWigOverAverageBed are:
#    name - name field from bed, which should be unique
#    size - size of bed (sum of exon sizes
#    covered - # bases within exons covered by bigWig
#    sum - sum of values over all bases covered
#    mean0 - average over bases with non-covered bases counting as zeroes
#    mean - average over just covered bases


# This is the FPKM from t_ctab
y = pd.read_table(sys.argv[1])[["t_name","FPKM"]]

# This is the Chipseq on promoter from Bigwig output
x = pd.read_table(sys.argv[2])[[0,5]]
x.columns=["t_name","mean"]

# Though the number of rows don't match, this keeps the minimal one
data=pd.merge(y,x,on="t_name")

y=data["FPKM"]
#y=np.log10(data["FPKM"])

x=data["mean"]

model=sm.OLS(y,x)
results=model.fit()

fig, ax = plt.subplots()

#x_pred = np.linspace(-10, 10, 100)
#y_pred = results.predict(x_pred) +30
#ax.plot(x_pred, y_pred, '-', color='darkorchid', linewidth=50)

fig = sm.graphics.plot_fit(results, 0, ax=ax, alpha =0.5)

ax.set_ylabel("Expression Level (FPKM)")
ax.set_xlabel("Histone Modification")
ax.set_title("Linear Regression H3K{}me3".format(sys.argv[2][0:2]))
ax.set_ylim([0,200])
plt.savefig("Histone-mRNA_Expression-H3K{}me3.png".format(sys.argv[2][0:2]))
