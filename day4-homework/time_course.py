#!/usr/bin/env python

"""
Draw one line of the male data, one line of the female data.
One set of male replicate dots. One set of female replicate dots.

Usage: ./time_course.py <metadata.csv> <rep_data.csv> <ctab_dir>
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_meta=pd.read_csv(sys.argv[1])
rep_meta=pd.read_csv(sys.argv[2])
ctab_dir=sys.argv[3]


#df_new=df_meta[df_roi]     # This is a DataFrame

# Male line blue, female line red. "." point

sex_Sxl=[]
sex=["male","female"]
color=["blue","red"]

plt.figure()
# Getting line data
for i in range(0,2):
    df_roi=df_meta["sex"]==sex[i]    # getting the roi in each sex
    df_meta_sex=df_meta[df_roi]
    stages=df_meta_sex["stage"].values  # converting dataframe to list
    for sample in df_meta_sex["sample"]:    # getting line in .ctab
        filename=ctab_dir+"/"+sample+"/t_data.ctab" # getting file name
        df = pd.read_table(filename)                
        df_roi = df["t_name"] == "FBtr0331261"      # Getting roi with the transcript
        #df[df_roi]["FPKM"]          # This is a Series
        sex_Sxl.append(df[df_roi]["FPKM"].values)          # Getting the FPKM in transcript
    plt.plot(sex_Sxl, color=color[i],label=sex[i],linewidth=3)
    sex_Sxl=[]      # Clean the FPKM list


# Add the replicates
rep_sex_Sxl=[0,0,0,0]       # skip 10,11,12,13
for i in range(0,2):
    rep_roi=rep_meta["sex"]==sex[i]    # getting the roi in each sex
    rep_meta_sex=rep_meta[rep_roi]
    for sample in rep_meta_sex["sample"]:    # getting line in .ctab
        filename=ctab_dir+"/"+sample+"/t_data.ctab" # getting file name
        rep = pd.read_table(filename)                
        rep_roi = rep["t_name"] == "FBtr0331261"      # Getting roi with the transcript
        rep_sex_Sxl.append(rep[rep_roi]["FPKM"].values)    # Getting the FPKM in transcript
    plt.plot(rep_sex_Sxl, ".", color=color[i],label="{} {}".format(sex[i], "replicates", markersize=5),linewidth=3)
    rep_sex_Sxl=[0,0,0,0]

plt.title("Sxl", size=40)
plt.xticks(range(len(stages)),stages)
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.xlabel("developmental stage",size=20)
plt.ylabel("mRNA abundance (FPKM)",size=20)
plt.legend(loc="upper left")
plt.xlim([-1,8])
plt.subplots_adjust(left=0.2, bottom=0.15, top=0.85,right=0.85)
plt.savefig("timecourse.png")    
plt.close()
    
    

