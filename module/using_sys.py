#!/usr/bin/python

import sys

print 'The command line arguments are:'

# note the executing file name is the first argument in argv
print sys.argv

for arg in sys.argv: # sys.argv is a list
  print arg

print '\n\nThe PYTHONPATH is %s \n' % sys.path
