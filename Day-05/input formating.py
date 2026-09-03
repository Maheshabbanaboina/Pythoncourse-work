Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#input formating
#int float str list tuple set dict
x=input()
fdhdhsjtyy
x
'fdhdhsjtyy'
name=input()
bharath
name
'bharath'
#str
name=input("enter your name")
enter your name mahesh
name
' mahesh'
age = input("enter your age")
enter your age 22
age
' 22'
type(age)
<class 'str'>
age= int(input("enter your age"))
enter your age 22
age
22
type(age)
<class 'int'>
names = input("enter the names:")
enter the names:mahesh venu nandu
names
'mahesh venu nandu'
names.split()
['mahesh', 'venu', 'nandu']
['mahesh', 'venu', 'nandu']
['mahesh', 'venu', 'nandu']
names=input("enter the names").split()))
SyntaxError: unmatched ')'
names=input("enter the names").split())
SyntaxError: unmatched ')'
SyntaxError: unmatched ')'
SyntaxError: invalid syntax
names=input("enter the names").split()
enter the names mahesh venu nandu
names
['mahesh', 'venu', 'nandu']
names=input("enter the names:").split()
enter the names:1 2 3 4 5 6
names
['1', '2', '3', '4', '5', '6']
map(int(input()
        map(int(input(),names))
        
SyntaxError: '(' was never closed
values=list(map(int,input().split())
         values=list(map(int,input().split())
                     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
list(map(int,names))
                     
[1, 2, 3, 4, 5, 6]
values=list(map(int,input().split()))
                     
1 2 3 4 5 6 7 8 9  0
values
                     
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
names=tuple(input().split())
                     
mahesh madhu rahul
names
                     
('mahesh', 'madhu', 'rahul')
values=tuple(map(int,input().split()))
                     
1 2 3 4 5 6 7 8 7 777 
values
                     
(1, 2, 3, 4, 5, 6, 7, 8, 7, 777)
(1, 2, 3, 4, 5, 6, 7, 8, 7, 777)
                     
(1, 2, 3, 4, 5, 6, 7, 8, 7, 777)




















a,b=[1,2]
                     
a
                     
1
b
                     
2
a,b(1,2)
                     
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a,b(1,2)
TypeError: 'int' object is not callable
a,b=(1,2)
                     
a,b=(1,2)
                     
email,password=input("enter the emaiol and password:").split()))
        
SyntaxError: unmatched ')'
email,password=input("enter the emaiol and password:").split())
    
SyntaxError: unmatched ')'
email,password=input("enter the emaiol and password:").split()
    
enter the emaiol and password:mahesh@gmail.com
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    email,password=input("enter the emaiol and password:").split()
ValueError: not enough values to unpack (expected 2, got 1)

email,password=input("enter the email and password:").split()
    
enter the email and password:mahesh@.com and 1234
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    email,password=input("enter the email and password:").split()
ValueError: too many values to unpack (expected 2, got 3)
email,password=input("enter the email and password:").split()
    
enter the email and password:mahesh@gmail.com 1234
email
    
'mahesh@gmail.com'
password
    
'1234'
a,b,c=list(map(int,input().split()))
    
123
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 1)
a,b,c=list(map(int,input().split()))
    
1 2 3
>>> a
...     
1
>>> b
...     
2
>>> c
...     
3
>>> name,marks= input().split()
...     
mahesh 80
>>> name
...     
'mahesh'
>>> marks
...     
'80'
>>> int(marks)
...     
80
>>> e= eval(input())
...     
1
>>> e
...     
1
>>> e= eval(input())
...     
12.35
>>> e
...     
12.35
>>> e=eval(input())
...     
("mahesh")
>>> e
...     
'mahesh'
>>> e=eval(input())
...     
[1,2,3,4,5]
>>> e
...     
[1, 2, 3, 4, 5]
