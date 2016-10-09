#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


for f in sys.argv[1:]:
    # myfile=open(f)
    name=f.split(".")[1]
    a = pd.read_table(open(f),delim_whitespace = True)
    log=-1*np.log10(a[a["P"]<0.00001])
    plt.plot(log, '.',ms=8)    

    
    log = -1*np.log10(a[a["P"]>0.00001])
    plt.plot(log, '.', color = "red",ms=3)
    
    plt.xlabel("SNPs")
    plt.ylabel("Significance of Association")
    plt.title("Manhattan Plot for "+name)
    # plt.show()
    # break
    plt.savefig(name+".png")
    # pval = [] ##    A1
    # i=0
    # while True:
    #     line = myfile.readline().rstrip("\r\n")
    #     if line == "":
    #         break
    #     if line.startswith("C"):
    #         continue
    #
    #     fields=line.split("       ")
    #     print fields
    #     break
    #     pval.append(fields[8])
    #     print pval
    #     #x1.append(fields[4])
    #     #x2.append(fields[6])
    #
    #     i=i+1
    #
    # #print x
    # plt.scatter()
    # #plt.show()
    # plt.savefig("")
    # np.log