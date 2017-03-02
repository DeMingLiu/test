#!/usr/env/bin python
# -*- encoding utf-8 -*-
'''
class Student(object):
    def __init__(self, name, source):
        self.__name = name
        self.__source = source

    def print_source(self):
        print '%s: %s' % (self.__name, self.__source)

    def get_grade(self):
        if self.__source >= 90:
            return 'A'
        elif self.__source >= 60:
            return 'B'
        else:
            return 'C'
    
    def get_name(self):
        return self.__name

    def get_source(self):
        return self.__source


    def set_name(self, name):
        self.__name = name

    def set_source(self, source ):
        if 0 <= source <= 100:
            self.__source = source
        else:
            raise ValueError('badsouce')

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_source()
lisa.print_source()
lisa.set_source(55)
lisa.print_source()


print bart.get_grade()
print Student.get_grade(bart)
'''

'''
class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print "Dog is running..."
    def eat(self):
        print "Eating meat..."

class Cat(Animal):
    def run(self):
        print "Cat is running..."
    def eat(self):
        print "Eating meat..."

def run_twice(animal):
    animal.run()
    animal.run()


dog = Dog()
dog.run()

cat = Cat()
cat.run()
'''

'''
from types import MethodType

def set_age(self,age):   
    self.age = age

class Student(object):
    pass

Student.set_age = MethodType(set_age,Student)

A = Student()
B = Student()
B.set_age(15)

A.set_age(10)

print A.age,B.age
'''


'''
#   __sloat__
from types import MethodType
class Student(object):
    __slots__ = ('name', 'age')


def func(self):
    print 'this is a test'

Student.func = MethodType(func, Student)

s = Student()
s.func()
'''


'''
#   property
class Student(object):

    def get_source(self):
        return self._source

    def set_source(self, value):
        if not isinstance(value, int):
            raise ValueError("Source must be an intager!")
        if value < 0 or value > 100:
            raise ValueError("source must between 0 ~ 100!")
        self._source = value

s = Student()
s.set_source(99)
print s.get_source()
s.set_source(5555)
print s.get_source()
'''

'''
class Student(object):
    
    @property 
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = value

s = Student()
s.score = 60
print s.score
s.score = 444
print s.score 

'''


'''
class Student(object):
    @property 
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value=1991):
        self._birth = value

    @property 
    def age(self):
        return 2017 - self._birth



s = Student()
# s.birth = 1991
print s.age
'''

'''
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runable(object):
    def run(self):
        print "Running..."

class Flyable(object):
    def fly(self):
        print "Flying ..."


class Dog(Mammal, Runable):
    pass

'''


'''
class Student(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Student object (name: %s,)" % self.name 
# print dir(Student)
print Student("lmd")
'''

'''
#   __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def next(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 200:
            raise StopIteration()
        return self.a

for n in Fib():
    print n
'''

#   __getitem__
'''
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):         
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range (stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L 

f = Fib()
print f[0]
print f[1]
print f[2]
print f[10]

print f[0:5]
'''



# import ctypes
# def h2f(s):
#     cp = ctypes.pointer(ctypes.c_longlong(s))
#     fp = ctypes.cast(cp, ctypes.POINTER(ctypes.c_double))
#     return fp.contents.value
# def f2h(s):
#     fp = ctypes.pointer(ctypes.c_double(s))
#     cp = ctypes.cast(fp, ctypes.POINTER(ctypes.c_longlong))
#     return hex(cp.contents.value)
# print(f2h(34.4536))
# print(h2f(0x40413a0f9096bb99))


from ctypes import *
def convert(s):
    i = int(s, 16)
    cp = pointer(c_int(i))
    fp = cast(cp, POINTER(c_float))
    return fp.contents.value


# print convert("470FC614")

import struct


a = struct.pack("<f", 3.4).encode('hex')
print a

print struct.unpack('!f', a.decode('hex'))[0]









 #