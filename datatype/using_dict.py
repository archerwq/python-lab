#!/usr/bin/python

addr_book = {
    'Qiang Wang': 'archer.wq@gmail.com',
    'Cold Play': 'cold.play@gmail.com',
    'Jay Zhou': 'jay.zhou@gmail.com'
  }

print "Qiang's address is %s" % addr_book['Qiang Wang']

addr_book['Kobe Bryant'] = 'kobe.bryant@gmail.com'

del addr_book['Jay Zhou']

print 'There are %d contacts in the address book.' % len(addr_book)

# dict.items(): list of (key, value) pairs, as 2-tuples
for name, address in addr_book.items():
  print 'contact %s at %s' % (name, address)

if 'Kobe Bryant' in addr_book: # or addr_book.has_key('Kobe Bryant')
  print "Kobe Bryant's address is %s" % addr_book['Kobe Bryant']


try:
  addr_book['Qiang']
except KeyError:
  print 'WTF. KeyError exception will be thrown out if key does not exist!'


print dir(dict)
help(dict)
