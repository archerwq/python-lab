#!/usr/bin/python

import os

print 'OS name:', os.name
print 'Current directory:', os.getcwd()
print 'All the files under current directory:', os.listdir(os.getcwd())

print 'Run ls -al:'
os.system('ls -al')

print 'line seperator is', os.linesep
print os.path.split(os.getcwd())

print dir(os)
print dir(os.path)
