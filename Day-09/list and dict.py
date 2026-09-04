Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={}
type(s)
<class 'dict'>
s=set()
s={1,2,3,4,5,1,2,45,6,12345}
s
{1, 2, 3, 4, 5, 6, 45, 12345}
s=set()
s
set()
s.add(1)
s.add(12.3)
s.add(2+4j)
s
{1, 12.3, (2+4j)}
s
{1, 12.3, (2+4j)}
s={flase,1,"str",(1,2,3),12.3,(2+4J)}
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s={flase,1,"str",(1,2,3),12.3,(2+4J)}
NameError: name 'flase' is not defined
s
{1, 12.3, (2+4j)}
s={1,1,1,1,1,1,1,}
s
{1}
a={1,2,3,4,5}
b = {3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a|b
{1, 2, 3, 4, 5, 7, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
a ^ b
{1, 2, 4, 7, 9}
a <= b
False
{1}<=a
True
{1,2,3,4}<=a
True
a
{1, 2, 3, 4, 5}
{1,2,3,4,5}<=a
True
b
{9, 3, 5, 7}
a.isdisjoint(b)
False
a.isdisjoint{9,10}
SyntaxError: invalid syntax
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
2 in a
True
5 not in a
False
8 not in a
True
a
{1, 2, 3, 4, 5}
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c = a.copy()
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
a.add(123,45)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.add(123,45)
TypeError: set.add() takes exactly one argument (2 given)
a.add(123)
a
{1, 2, 3, 4, 5, 123, 12}
a.update(1235,45)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.update(1235,45)
TypeError: 'int' object is not iterable
a.update([1235,45])
a
{1, 2, 3, 4, 5, 12, 1235, 45, 123}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 12, 1235, 45, 123}
a.remove(1235)
a
{3, 4, 5, 12, 45, 123}
a.remove(1235)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.remove(1235)
KeyError: 1235
a.discard(1235)
a.dicard(45)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.dicard(45)
AttributeError: 'set' object has no attribute 'dicard'. Did you mean: 'discard'?
a.discard(45)
a
{3, 4, 5, 12, 123}
a.clear()
a
set()
a= frozenset({2,3,4,5,6,7,})
a
frozenset({2, 3, 4, 5, 6, 7})
a.add(45)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.add(45)
AttributeError: 'frozenset' object has no attribute 'add'
#dictionary properties
d={}
d=dict()
type(d)
<class 'dict'>
d = {'k1': 'v1' ,'k2' : 'v2','k3' : 'v3','k4': 'v4"}
     
SyntaxError: unterminated string literal (detected at line 1)
d = {'k1': 'v1' ,'k2' : 'v2','k3' : 'v3','k4': 'v4'}
     
d
     
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
id(d)
     
2796284287424
d['k4']= 'v4'
     
d
     
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d['k4'] = 'mahesh'
     
d
     
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'mahesh'}
id(d)
     
2796284287424
d={}
     
d[1]='int'
     
d
     
{1: 'int'}
d[12.3]='flt'
     
d
     
{1: 'int', 12.3: 'flt'}
d[2+4j]='complex'
     
d
     
{1: 'int', 12.3: 'flt', (2+4j): 'complex'}
d[(1,2,3,4,)]='tuple'
     
d
     
{1: 'int', 12.3: 'flt', (2+4j): 'complex', (1, 2, 3, 4): 'tuple'}
d[{1,45,67}]='set'
     
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    d[{1,45,67}]='set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{'2';}]='dict'
     
SyntaxError: invalid syntax
d[{'2':}]='dict'
     
SyntaxError: expression expected after dictionary key and ':'
d[[1,23,45,]]='list'
     
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    d[[1,23,45,]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d['Flase']='Flase'
     
d
     
{1: 'int', 12.3: 'flt', (2+4j): 'complex', (1, 2, 3, 4): 'tuple', 'Flase': 'Flase'}
d[frozenset{1,2,3,5}]='fset'
     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d
     
{1: 'int', 12.3: 'flt', (2+4j): 'complex', (1, 2, 3, 4): 'tuple', 'Flase': 'Flase'}
d[frozenset{1,2,3,5}]='fset'
     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d{}
     
SyntaxError: invalid syntax
d{}
     
SyntaxError: invalid syntax
d={}
     
d[1]=1
     
d[2]=12.3
     
d[3]=12+3j
     
d[4]='str'
     
d[5]=[1,2,3,4,5]
     
d[6]=91,2,3,4,56)
SyntaxError: unmatched ')'
d[6]=(1,2,3,4,5,6,7)
d[7]={1,2,3,4,5}
>>> d
{1: 1, 2: 12.3, 3: (12+3j), 4: 'str', 5: [1, 2, 3, 4, 5], 6: (1, 2, 3, 4, 5, 6, 7), 7: {1, 2, 3, 4, 5}}
>>> 9 in d
False
>>> 2 in d
True
>>> 'str' in d
False
>>> 5 in d
True
>>> d[5]
[1, 2, 3, 4, 5]
>>> d[8]
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    d[8]
KeyError: 8
>>> d[7]
{1, 2, 3, 4, 5}
>>> d.get[2]
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    d.get[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> d.get(2)
12.3
>>> d.get(10,'key is not present')
'key is not present'
>>> d.get(2,'key is not present')
12.3
>>> d.get(5,'key is present')
[1, 2, 3, 4, 5]
>>> d[2]=20
>>> d
{1: 1, 2: 20, 3: (12+3j), 4: 'str', 5: [1, 2, 3, 4, 5], 6: (1, 2, 3, 4, 5, 6, 7), 7: {1, 2, 3, 4, 5}}
>>> d[5]= 12345
>>> d
{1: 1, 2: 20, 3: (12+3j), 4: 'str', 5: 12345, 6: (1, 2, 3, 4, 5, 6, 7), 7: {1, 2, 3, 4, 5}}
>>> d[7]=3763es6
SyntaxError: invalid decimal literal
>>> d[7]=3456793
>>> d
{1: 1, 2: 20, 3: (12+3j), 4: 'str', 5: 12345, 6: (1, 2, 3, 4, 5, 6, 7), 7: 3456793}
