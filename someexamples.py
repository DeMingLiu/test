#!/usr/bin/env python
#-*-coding:utf-8 -*-
# print 'hello, %s' % 'world'

# print 'Hi, %s, you have $%.1f.' %('Michael', 33.111)


# print '%02d - %03d' % (2,1)

# print "growth rate: %d%%" % 7

# source1 = 72
# source2 = 85
# imp = ((85 - 72) / 72) * 100
# # print "improve: %.1f%%" % ((source2-source1)/source1)*100
# print 'improve: ' , imp

'''
classmates = ['Michael','Bob','Tracy']
print classmates
print len(classmates)
classmates.append('Adam')
print classmates
classmates.insert(1,'Jack')
print classmates
classmates.pop(1)
print classmates
classmates[1] = 'Sarch'
print classmates

L = ['Apple',123, True]
print L

classmates_tuple = ('Michael','Bob','Tracy')
print classmates_tuple
t = (2,)
print t
'''

'''
d = {'Michael':95,'Bob':75 ,'Tracy': 85}
print d
d.pop('Bob')
print d


# s = set([1,2,3])
# print s

s = {'No1':1,'(1,2,3)':(1,2,3)}
print s['(1,2,3)']
'''

'''
def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)

# print fact(5)

def fact2(n):
    return fact_iter(n,1)

def fact_iter(num, producter):
    if num == 1 :
        return producter
    # print "fact_iter(%d, %d)" % (num-1, num*producter)
    print "fact_iter(%d, %d)" % (num, producter)
    return fact_iter(num-1, num*producter)


print fact2(5)
'''

'''
L = ['Michael', 'Sarch', 'Tracy', 'Bob', 'Jack']
print L[:3]

l = range(100)
print l[::5]
'''

'''
d = {'a':1, 'b':2, 'c':3}

for key in d:
    print key , d[key]

for value in d.itervalues():
    print value
'''

'''
from  collections import Iterable
print isinstance(1234, Iterable)


for key, value in enumerate(('A','B','C')):
    print key, value

for x,y,z in [(1,1,1),(2,4,8), (3,9,27)]:
    print x,y,z
'''

'''
L = []
# print range(1,11)

l = [x * x for x in range(1,11) if x % 2 ==0]
print l

b = [m + n for m in 'ABC' for n in 'XYZ']
print b

l = ["Hello", 'World',18, 'Apple',None]

aa = [word.lower() for word in l if isinstance(word,str)]
bb = [word.lower() if isinstance(word,str) else word for word in l]
print aa
print bb
'''


# g = (x * x for x in range(10))

# for n in g :
#     print n
'''
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3

o = odd()
o.next()
o.next()
o.next()
o.next()
'''

'''
f = abs
def add(x, y, f):
    return f(x) + f(y)

a = 2
b = 2
c=b
print id(a)
print id(b)
print a is c
'''

'''
a = [1,2,3,4,5,6,7,8,9]
def f(x):
    return x*x
print map(f,a)

def fn (x,y):
    return x*10 + y

print reduce(fn,[1,3,5,7,9])
'''

'''
bar = lambda:'begineman'
print bar()

def add(x, y):return x + y
add2 = lambda x,y : x+y
print add2(1,2)

'''

'''
def str2int(s):
    def fn(x,y):
        return x*10+y

    def char2num(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
     
    return reduce(fn,map(char2num,'25689'))
'''

'''
def is_add(n):
    return n % 2 == 1
print filter(is_add,[1,2,4,5,6,9,10,15])
'''

'''
numlist = range(1,101)
def snum(num):
    count = 0
    for i in range(1,num+1):
        if num %i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
print filter(snum,numlist)


def fn(x):
    n=2 
    while n < x:
        if x % n == 0:
            return False
        n = n + 1
    return True
print filter(fn,range(2,101))
'''

'''
def lazy_sum(*args):
    def calc_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return calc_sum

f = lazy_sum(1,3,4,6,7,9)
print f()
'''

'''
def f():
    print 'Call f() ...'
    def g():
        print 'call g()...'
    return g

x = f()
x()
'''

'''
def make_addr(addend):
    def adder(augend):
        return addend + augend
    return adder

p = make_addr(23)
q = make_addr(44)

print p(100)
print q(100)
'''

'''
def hellocounter(name):
    count = [0]
    def counter():
        count[0] += 1
        print 'Hello, ', name, ',', str(count[0]) + ' access!'
    return counter
hello = hellocounter('ma6714')
hello()
hello()
hello()
'''

'''
def count():
    fs = []
    for i in range(1,4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs
z1,z2,z3 = count()
print z1()
print z2()
print z3()


func = lambda i :lambda :i*i 
def count2():
    fs = []
    for i in range(1, 4):
        fs.append(func(i) )
    return fs
x1,x2,x3 = count2()
print x1()
print x2()
print x3()
'''

'''
def makebold(fn):
    def wrapped():
        return '<b>' + fn() + "/b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return '<i>' + fn() + '</i>'
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

# print hello()

aaa =  makebold(makeitalic(hello))
print aaa()
'''


'''
def now():
    print '2013-12-25'

f = now
print f()
print now.__name__
print f.__name__
'''


'''

def log(func):
    def wrapper(*args, **kw):
        print 'call %s(): ' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2013-12-25'

# # f = now
# # f()
# # print f()
# # print now.__name__
# # print f.__name__
# now()

a = log(now)
a()
'''


'''
' a test module '
__author__ = 'MDing'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print "Hello World!"
    elif len(args) == 2:
        print "Hello, %s!" % args[1]
    else:
        print 'Too many arguments!'
    print 'this is %s' % args[0]

if __name__ == '__main__':
    test()
'''
#   deal with failure



try :
    print 'try ....'
    r = 10 / 0
except ZeroDivisionError, e:
    print 'except: ', e
finally:
    print 'finally ...'
print 'END'








''''''