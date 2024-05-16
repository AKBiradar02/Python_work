from msilib import type_localizable


t = (1,2,3,4)
mylist = [1,2,3,4]
type(t)
print(type(t))
type(mylist)
print(type(mylist))
len(t)
print(len(t))

w = ('one',3,'given',100)
w[0]
print(w[0])
print(w[-1])

a = ('a','a','a','a','b')
a.count('a')
print(a.count('a'))
print(a.index('a'))
print(a.index('b'))

mylist[0] = 'new'
print(mylist)

t[0] = 'waow'
print(t)

