#!/usr/bin/python

# Both tuple and list are sequence

zoo = ('wolf', 'elephant', 'panda')
print 'Number of animals in the zoo is', len(zoo)

new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All the animals in the new zoo are', new_zoo
print 'Animals bought from old zoo are', new_zoo[2]
print 'The last animal bought from old zoo is', new_zoo[2][2]


# print tuple
name = 'Qiang'
age = 30
print '%s is %d years old' % (name, age)
print 'Why is %s playing with Python?' % name


print dir(tuple)
help(tuple)
