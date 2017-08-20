#!/usr/bin/python

shoplist = ['apple', 'mango', 'carrot', 'banana']
print 'I have %d items to purchase.' % len(shoplist)

print 'These items are:',
for item in shoplist:
  print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist

print 'I will sort my list.'
shoplist.sort()
print 'Sorted shopping list is', shoplist

print 'The first item I will buy is', shoplist[0]
old_item = shoplist[0]
del shoplist[0]
print 'I bought', old_item
print 'Now the list is', shoplist

print 'list is class defined in __builtin__ module, the members of list are:'
print dir(list)

help(list)
