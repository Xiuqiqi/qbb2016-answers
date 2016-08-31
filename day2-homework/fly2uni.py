#!/usr/bin/env python

import sys

# Use the fly.txt as standard input to the script.
for line in sys.stdin:
    if "DROME" not in line:
        continue
        # select only the lines with ID
    print "".join(line[52:63]), "\t", "".join(line[40:46])
    # first print the Flybase ID, a <TAB>, then UniProt ID, in string
    