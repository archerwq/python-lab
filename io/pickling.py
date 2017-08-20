#!/usr/bin/python

# cPickle is written in C and 1000X quicker than pickle module
import cPickle as p
# import pickle as p

shoplist_file = 'shoplist.data'
shoplist = ['Apple', 'Meat', 'Beer', 'Salt']
f = file(shoplist_file, 'w')
p.dump(shoplist, f)  # write an object in pickle format to the given file
f.close()

del shoplist

f = file(shoplist_file, 'r')
stored_shoplist = p.load(f)  # load pickle from the given file
print stored_shoplist
f.close()
