#!/usr/bin/env python
import sys
import re
import os

#get the start directory 
start= sys.argv[1]

#Get the patterns from the command line arguments
pattern=sys.argv[2]

#convert them to regular expressions
expr=re.compile(pattern)
#traverse the directories for all the files
for root, dirs, files in os.walk(start):
	for fname in files:
		if fname in files:
			if expr.match(fname):
				print os.path.join(root, fname)
				#print root+"/"+fname
		#if a file matches the pattern, print its name



