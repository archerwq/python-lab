#!/usr/bin/python

from oop import people as p

print dir(p) # get list of attributes for people module

print p.Person.__doc__
print p.__name__
print p.__file__
print p.__package__

from oop.people import Person
guy = Person('Tim')
guy.sayHi()

# import a var in a module
from sys import argv
print argv
