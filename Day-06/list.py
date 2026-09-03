Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c='strings.py'
c.startswith('str')
True
c.startswith('python')
False
c.endswith('python')
False
c.endswith('py')
True
c.islower()
True
c.isupper()
False
'PYTHON@123'.ISUPPER()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    'PYTHON@123'.ISUPPER()
AttributeError: 'str' object has no attribute 'ISUPPER'
'PYTHON123'.isupper()
True
c.isaplha()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
c.isalpha()
False
c.isalnum()
False
'          '.isspace()
True
'h         '.isspace()
False
'this is title'.istitle()
False
'TYHIS IS TITLE'.istitle()
False
'This Is Title'.istitle()
True
'my@var'isidentifier()
SyntaxError: invalid syntax
'my@var'.isidentifier()
False
'my_var'.isidentifier()
True
#day6 list
l=[]
l=list()
>>> l=[1,2.3,2+3j],str',[1,2,3,],(1,2,3,),{1,2,3}
SyntaxError: unterminated string literal (detected at line 1)
>>> l=[1,2.3,2+3j],str',[1,2,3,],(1,2,3,),{1,2,3},{1:1},none,true
SyntaxError: unterminated string literal (detected at line 1)
>>> l=[1,2.3,2+3j],'str',[1,2,3,],(1,2,3,),{1,2,3},{1:1},none,true
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l=[1,2.3,2+3j],'str',[1,2,3,],(1,2,3,),{1,2,3},{1:1},none,true
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> l=[1,2.3,2+3j],str',[1,2,3,],(1,2,3,),{1,2,3},{1:1},none,true]
SyntaxError: unterminated string literal (detected at line 1)
>>> l=[1,2.3,2+3j],'str',[1,2,3,],(1,2,3,),{1,2,3},{1:1},none,true]
SyntaxError: unmatched ']'
>>> l=[1,2.3,2+3j),'str',[1,2,3,],(1,2,3,),{1,2,3},{1:1},none,true]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> l=[1,2.3,(2+3j),'str',[1,2,3,],(1,2,3,),{1,2,3},{1:1},none,true]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    l=[1,2.3,(2+3j),'str',[1,2,3,],(1,2,3,),{1,2,3},{1:1},none,true]
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> l=[1,2,3,4]
>>> m=[5,6,7]
>>> l+m
[1, 2, 3, 4, 5, 6, 7]
>>> m*3
[5, 6, 7, 5, 6, 7, 5, 6, 7]
>>> l
[1, 2, 3, 4]
>>> l[3]
4
>>> l[-1]
4
>>> l[1;]
SyntaxError: invalid syntax
>>> l[1:]
[2, 3, 4]
>>> l[:3]
[1, 2, 3]
>>> l[::-1]
[4, 3, 2, 1]
>>> 4 in l
True
>>> 5 in l
False
>>> 1 in l
True
