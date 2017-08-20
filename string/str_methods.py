#!/usr/bin/python

name = 'archerwq'
if name.startswith('arc'):
  print 'Yes, the string starts with "arc"'

if 'a' in name:
  print 'Yes, "a" is in the string'

if name.find('erw') != -1:
  print 'Yes, "erw" is in the string'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)


print dir(str)
help(str)
