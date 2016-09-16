#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it.
"""

import sys

class FASTAReader( object ):
    def __init__( self, file ):
        self.file = file
        self.last_id = None
        
    def next( self ):
        if self.last_id is None:
            line = self.file.readline()
            # Verify is header line
            assert line.startswith( ">" )
            # Extract id -- whole line
            ## identifier = line[1:].rstrip( "\r\n" )
            # Extract id -- space
            identifier = line[1:].split()[0]
        else:
            identifier = self.last_id

        sequences = []

        while True:
            line = self.file.readline().rstrip("\r\n")
            if line.startswith( ">" ):
                self.last_id = line[1:].split()[0]
                break
            elif line == "":
                sequences.append( line )
                return False, identifier, "".join( sequences )
            else:
                sequences.append( line )
                
        return True, identifier, "".join( sequences )
        
#print identifier, "".join(sequences)
    
# what I want;

#reader = FASTAReader(sys.stdin)
    
#while 1:
#    identifier, sequence=reader.next()
#    if identifier is None:
#        break
#    print identifier, sequence
    
