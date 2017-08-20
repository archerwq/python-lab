#!/usr/bin/python

import time

try:
  f = file('./try_finally.py')
  while True:
    line = f.readline()
    if (len(line) == 0):
      break
    time.sleep(3)
    print line,
finally:
  f.close()
  print 'Cleaning up... file closed'
  
