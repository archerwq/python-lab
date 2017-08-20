#!/usr/bin/python

class ShortInputException (Exception):
  '''A user-defined exception class.'''
  def __init__(self, length, atleast):
    Exception.__init__(self)
    self.length = length
    self.atleast = atleast
  
  def __str__(self):
    return 'ShortInputException: The input was of length %d, \
was expecting at least %d' % (self.length, self.atleast) 

try:
  s = raw_input('Enter something: ')
  if len(s) < 3:
    raise ShortInputException(len(s), 3)
except EOFError: # ctr+d
  print '\nWhy did you do an EOF on me?'
except ShortInputException, e:
  print e # will call e.__str__()
except:
  print '\nSome error/exception occurred.'
else:
  print 'No exception was raised.' 
