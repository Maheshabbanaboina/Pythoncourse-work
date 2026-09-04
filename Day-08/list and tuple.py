Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4,5,]
l=[1,45,23,56,78,]
l
[1, 45, 23, 56, 78]
id(l)
1411855544192
l.append(14)
l
[1, 45, 23, 56, 78, 14]
l.append(35)
l
[1, 45, 23, 56, 78, 14, 35]
id(l)
1411855544192
l.insert(20,100)
l
[1, 45, 23, 56, 78, 14, 35, 100]
l.insert(2,85)
l
[1, 45, 85, 23, 56, 78, 14, 35, 100]
l.insert(1,43)
l
[1, 43, 45, 85, 23, 56, 78, 14, 35, 100]
l.extend([1,2])
l
[1, 43, 45, 85, 23, 56, 78, 14, 35, 100, 1, 2]
l.extend([35,26])
l
[1, 43, 45, 85, 23, 56, 78, 14, 35, 100, 1, 2, 35, 26]
#removing element methods
l.pop()
26
l.pop(4)
23
l.pop(8)
100
l
[1, 43, 45, 85, 56, 78, 14, 35, 1, 2, 35]
l.remove(1)
l
[43, 45, 85, 56, 78, 14, 35, 1, 2, 35]
l.remove(85)
l
[43, 45, 56, 78, 14, 35, 1, 2, 35]
del l[2]
l
[43, 45, 78, 14, 35, 1, 2, 35]
del l[5]
l
[43, 45, 78, 14, 35, 2, 35]
l.clear()
l
[]
id(l)
1411855544192
l=[10,30,40,32,23,56]
l
[10, 30, 40, 32, 23, 56]
max(l)
56
min(l)
10
sorted(l)
[10, 23, 30, 32, 40, 56]
l
[10, 30, 40, 32, 23, 56]
l.reverse()
l
[56, 23, 32, 40, 30, 10]
l.sort()
l
[10, 23, 30, 32, 40, 56]
l=[1,2,3]
m=[1,2,3]
L(id)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    L(id)
NameError: name 'L' is not defined. Did you mean: 'l'?
l(id)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    l(id)
TypeError: 'list' object is not callable
l
[1, 2, 3]
l.sort(reverse=True)
l
[3, 2, 1]
sum(l)
6
n=l
n.append(4)
n
[3, 2, 1, 4]
l
[3, 2, 1, 4]
m=l.copy()
m
[3, 2, 1, 4]
m.append(10)
m
[3, 2, 1, 4, 10]
l
[3, 2, 1, 4]
all(['','',[],(),set(),{},flase])
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    all(['','',[],(),set(),{},flase])
NameError: name 'flase' is not defined
>>> all(['','',[],(),set(),{},False])
False
>>> any([1,'',[],(),set(),{},False])
True
>>> l
[3, 2, 1, 4]
>>> l.index[2]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    l.index[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l.indes(2)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    l.indes(2)
AttributeError: 'list' object has no attribute 'indes'. Did you mean: 'index'?
>>> l.index(2)
1
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    l.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> l.count(3)
1
>>> l.count(1)
1
>>> l.count(5)
0
>>> #nested list
>>> l=[[1,2,3,4,],[2,4,56,]]
>>> l[0]
[1, 2, 3, 4]
>>> l
[[1, 2, 3, 4], [2, 4, 56]]
>>> l[0][1]]
SyntaxError: unmatched ']'
>>> l[0][2]
3
>>> l[1][2]
56
>>> l[0][-1]
4
>>> l[1][-1]
56
>>> #tuple
