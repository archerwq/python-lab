#!/usr/bin/python

# default param can only be the last one
def say(message, times=1):
  print message * times

say('Hello')
say('World', 5)


def func(a, b=5, c=10):
  print 'a is %d, b is %d, and c is %d' % (a, b, c)

func(3)
func(3, 7)
func(25, c=24)
func(c=30, a=100)
