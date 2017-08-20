#!/usr/bin/python

import sys

def read_file(filename):
  f = file(filename)
  while True:
    line = f.readline()
    if len(line) == 0:
      break
    print line, # Notice comma to avoid automatic newline added by Python
  f.close()

if __name__ == '__main__':
  help_message = '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
  --version : Prints the version number
  --help    : Display this help'''

  # the first argument is always the program name
  if len(sys.argv) < 2:
    print 'No action specified.'
    print help_message
    sys.exit()
  
  if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
      print 'Version 1.0'
    elif option == 'help':
      print help_message
    else:
      print 'Unkonw option.'
  else:
    for filename in sys.argv[1:]:
      read_file(filename)
