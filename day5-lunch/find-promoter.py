#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd

df = pd.read_table(sys.argv[1]) #index_col=None)

df_extract=df[["t_name","chr","start","end"]]

#print df_extract

#df_roi=df["strand"]=="+"
#df_promoter=df[["strand","start"]]

#for line in df:
#print df

df_roi=df["strand"]=="+"
df_promoter_plus=df[df_roi][["chr","start","end","t_name"]]
df_promoter_plus.columns=["chr","start","end","t_name"]
df_promoter_plus["start"]=df_promoter_plus["start"]-500
df_promoter_plus["end"]=df_promoter_plus["start"]+1000

#print df_promoter_plus

df_roi=df["strand"]=="-"
df_promoter_minus=df[df_roi][["chr","end","start","t_name"]]
df_promoter_minus.columns=["chr","start","end","t_name"]
df_promoter_minus["start"]=df_promoter_minus["start"]-500
df_promoter_minus["end"]=df_promoter_minus["start"]+1000
#print df_promoter_minus

pieces=[df_promoter_plus,df_promoter_minus]

df_promoter=pd.concat(pieces).sort_index()

df_roi=df_promoter["chr"].str.len() < 4
df_promoter=df_promoter[df_roi]


df_promoter.to_csv( sys.stdout, sep="\t",index=False,header=False)


#print df_promoter


