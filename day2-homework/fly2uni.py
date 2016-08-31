#!/usr/bin/env python

import sys

# Use the fly.txt as standard input to the script.
for line in sys.stdin:
    if "DROME" not in line:
        continue
        # select only the lines with ID
    print line[52:63], "\t", line[40:46]
    # first print the Flybase ID, a <TAB>, then UniProt ID
    