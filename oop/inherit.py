#!/usr/bin/python

class SchoolMember:
  '''Represents any school member.'''
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print 'Initialing SchoolMember: %s' % self.name

  def tell(self):
    print 'Name: %s, Age: %d' % (self.name, self.age)

class Student(SchoolMember):
  '''Represents a student.'''
  def __init__(self, name, age, marks):
    SchoolMember.__init__(self, name, age)
    self.marks = marks
    print 'Initializing a Student: %s' % self.name

  def tell(self):
    SchoolMember.tell(self)
    print 'Marks: %d' % self.marks

class Teacher(SchoolMember):
  '''Represents a teacher.'''
  def __init__(self, name, age, salary):
    SchoolMember.__init__(self, name, age)
    self.salary = salary
    print 'Initializing a Teacher: %s' % self.name

  def tell(self):
    SchoolMember.tell(self)
    print 'Salary: %d' % self.salary

if __name__ == '__main__':
  s1 = Student('Qiang Wang', 33, 99)
  s2 = Student('Liang Li', 28, 89)
  t1 = Teacher('Mr. Green', 55, 5000)
  members = [s1, s2, t1]
  for m in members:
    m.tell() 
