Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=30
a<b
True
a>b
False
a<=b
True
a>=b
False
a!=b
True
c=30
c+=10
c
40
c-=10
c
30
c*=2
c
60
c//=4
c
15
c**=2
c
225
c%=3
c
0
c/=1
c
0.0
#comparsion operators
n=10
n%2==0
True
n%3==0
False
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n<5
False
not n<5
True
#membership operators
#str list tuple set dict
s='mahesh'
'e' in s
True
'z' in s
False
l=[1,2,3,4,5]
4 in l
True
6 in l
False
7 is not in l
SyntaxError: invalid syntax
7 not in l
True
tuple=(2,3,4,5,6,)
2 in tuple
True
7 in tuple
False
set{'2','3','5','7',}
SyntaxError: invalid syntax
True
True
set={'2','3','5','7'}
2 in set
False
8 in set
False
9 not in set
True
d={'name':'mahesh','batch':63,'course':'python','age':'22'}
'name' in d
True
'mahesh' in d
False
'age' in d
True
'22' in d
False
#identify operators
l=[2,3,4,5,6,]
m=[2,3,4,5,6]
id(l)
2261843162752
id(m)
2261798407104
l is m
False
n=1
id(n)
140722822694008
n=l
id(n)
2261843162752
l is n
True
l is m
False
l is not n
False
#immutable
s=('mahesh')
id(s)
2261843140528
s=('mahesh yadav')
id(s)
2261843268976
t=(1,2,3,4,5,)
id(t)
2261842888256
t.add(6)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t.add(6)
AttributeError: 'tuple' object has no attribute 'add'
s={1,2,3,4}
s.appened(5)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s.appened(5)
AttributeError: 'set' object has no attribute 'appened'
#mutable
l=[1,2,3,4,5]
l.add(6)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    l.add(6)
AttributeError: 'list' object has no attribute 'add'
id(l)
2261841605568
l.add[7]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    l.add[7]
AttributeError: 'list' object has no attribute 'add'
#bitwise operators
9&10
8
9
9
9|10
11
9^10
3
8>>2
2
8<<<3
SyntaxError: invalid syntax
8<<3
64
~45
-46
~56
-57
 #output formating
a=10
b=10.3
c='codegnan'
print(a,b,c)
10 10.3 codegnan
print("a value is",a)
a value is 10
print("a value is",a,"|b value is",b,"|c value is ",c)
a value is 10 |b value is 10.3 |c value is  codegnan
print(a,b,c)
10 10.3 codegnan
print(a,b,c,sep+'')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    print(a,b,c,sep+'')
NameError: name 'sep' is not defined. Did you mean: 'set'?
print(a,b,c,sep=''

      print(a,b,c,sep'')
      
SyntaxError: '(' was never closed
>>> print(a,b,c,sep='')
...       
1010.3codegnan
>>> print(a,b,c,sep='\n')
...       
10
10.3
codegnan
>>> print(a,b,c,sep='\t')
...       
10	10.3	codegnan
>>> print(a,b,c,sep='|t',end='@')
...       
10|t10.3|tcodegnan@
>>> print(a,b,c,sep='t',end='\n\n')
...       
10t10.3tcodegnan

>>> print(a,b,c,sep='',end='\n\n')
...       
1010.3codegnan

>>> print(f'a={a} b={b} c= {c}')
...       
a=10 b=10.3 c= codegnan
>>> print(f"value is {a} | b value is{b}|c value is {c}")
...       
value is 10 | b value is10.3|c value is codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
...       
a=10 b=10.300000 c=codegnan
>>> print('a=%d b=%2f c=%s'%(a,b,c))
...       
a=10 b=10.300000 c=codegnan
>>> print('a={} |b={} |c+{}'..format(a,b,c))
...       
SyntaxError: invalid syntax
>>> print('a={} |b={} |c+{}'.format(a,b,c))
...       
a=10 |b=10.3 |c+codegnan
>>> print('a={} |b={} |c={}'.format(a,b,c))
...       
a=10 |b=10.3 |c=codegnan
>>> print('a={1} |b={2} |c={0}'.format(a,b,c))
...       
a=10.3 |b=codegnan |c=10
