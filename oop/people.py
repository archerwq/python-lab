#!/usr/bin/python

class Person:
  '''Represents a person.'''
  population = 0

  def __init__(self, name):
    '''Initilize the person's data.'''
    self.name = name;
    print 'Initilizing %s' % self.name
    Person.population +=1

  def __del__(self):
    '''Delete a person. '''
    print '%s say goodbye.' % self.name
    Person.population -= 1
    if Person.population == 0:
      print 'I am the last one.'
    else:
      print 'There are still %d people left.' % Person.population

  def sayHi(self):
    '''Greeting from the person.'''
    print 'Hello, how are you doing? My name is', self.name

  def howMany(self):
    '''Print the current population.'''
    if Person.population == 1:
      print "I'm the only person here."
    else:
      print 'We have %d people here.' % Person.population

if __name__ == '__main__':
  p1 = Person("Qiang")
  p2 = Person("Tom")
  p3 = Person("Tim")
  p1.sayHi()
  p1.howMany()
  p2.sayHi()
  del p1
  p3.sayHi()
  del p2
  p3.howMany()
  del p3
  
  print Person.__doc__
  print Person.sayHi.__doc__


