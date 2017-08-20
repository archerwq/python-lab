#!/usr/bin/python
# -*- coding: utf-8 -*-

print 'Quote me on this'

print "What's your name?"

print '''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''

print 'This is the first sentence.\
This is the second sentence.'
# equals to 'This is the first sentence. This is the second sentence.'

print r'Newlines are indicated by \n'
print R'Newlines are indicated by \n'

# print u'这是Unicode字符串'
# print U'这是Unicode字符串'
# need to add coding header firstly
print '这是Unicode字符串'

print 'What\'s' 'your name?' # will be concatenated automatically

# print is a statement keyword
print 'Hi, my name is %s, I am living in %s city.' % ('Qiang', 'Beijing')

# notice the differences
# print a tuple
print ('Qiang', 'Beijing')
print('Qiang', 'Beijing')

print 'Qiang', 'Beijing' # will add a space between each string

print 'Qiang', # will not add a new line
print 'Wang'
