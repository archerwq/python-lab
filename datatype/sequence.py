#!/usr/bin/python

shoplist = ['apple', 'mango', 'carrot', 'banana']

# Indexing operation, index starts with 0
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]

# Slicing on a list, start is included and end is excluded
print 'Item 1 to 3 is', shoplist[1:3] # return index 1, 2
print 'Item 2 to end is', shoplist[2:] # return index 2, 3
print 'Item 1 to -1 is', shoplist[1:-1] # return index 1, 2
print 'Item start to end is', shoplist[:] # return a copy of the list

# Slicing on a string
name = 'archerwq'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]
