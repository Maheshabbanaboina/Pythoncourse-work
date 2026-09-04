Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c="python programming"
len(c)
18
ord("p")
112
ord("a")
97
ord("a")
97
#ascii is the numeric code assign to the characters:
chr(22)
'\x16'
chr(127)
'\x7f'



cha(50)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cha(50)
NameError: name 'cha' is not defined. Did you mean: 'chr'?
char(50)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    char(50)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(50)
'2'
#ord gives the what is standard number
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
#case conversion methods
a="Hello"
a.upper()
'HELLO'
a.lower()
'hello'
a.capitalize()
'Hello'
'mahesh yadav'
'mahesh yadav'
'mahesh yadav'.capitalizes()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    'mahesh yadav'.capitalizes()
AttributeError: 'str' object has no attribute 'capitalizes'. Did you mean: 'capitalize'?
'mahesh yadav'.captilize()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    'mahesh yadav'.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
"mahesh yadav".title()
'Mahesh Yadav'
"rUSVSUudus EJEjfwe".swapcase()
'RusvsuUDUS ejeJFWE'
"saaerGYTEDhjsydt".casefold()
'saaergytedhjsydt'
c="list is mutable"
c
'list is mutable'
c.center(50,'%')
'%%%%%%%%%%%%%%%%%list is mutable%%%%%%%%%%%%%%%%%%'
c.ljust(100,'*')
'list is mutable*************************************************************************************'
c.ljust(30,'^')
'list is mutable^^^^^^^^^^^^^^^'
c.rjust(40,'!')
'!!!!!!!!!!!!!!!!!!!!!!!!!list is mutable'
'1234'.zfill()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    '1234'.zfill()
TypeError: str.zfill() takes exactly one argument (0 given)
"12".zfill(5)
'00012'
"34".zfill(2)
'34'
#search and find methods
c
'list is mutable'
#search&find methods
c
'list is mutable'
c.find('l')
0
c.find('m')
8
c.rfind('t')
10
c.find('z')
-1
c.index('m')
8
c.rindex('t')
10
c.index('z')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c.count('i')
2
c.count('m')
1
c.count('t')
2
#replace and modify methods
c
'list is mutable'
c.replace('i','0')
'l0st 0s mutable'
c.replace('m','n')
'list is nutable'
c.replace('list','set')
'set is mutable'
c.maketrans('aeiou','1234')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    c.maketrans('aeiou','1234')
ValueError: the first two maketrans arguments must have equal length
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
#hash table for us
c,translate(c.maketrans('aeiou','12345')
            c.translate(c.maketrans('aeiou','12345')
                        
SyntaxError: '(' was never closed
c.translate(c.maketrans('aeiou','12345'))
                        
'l3st 3s m5t1bl2'
c.translate(c.maketrans('aeiou','@@@@@@))
                        
SyntaxError: unterminated string literal (detected at line 1)
c.translate(c.maketrans('aeiou','@@@@@@'))
                        
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    c.translate(c.maketrans('aeiou','@@@@@@'))
ValueError: the first two maketrans arguments must have equal length
c.translate(c.maketrans('aeiou','@@@@@'))
                        
'l@st @s m@t@bl@'
#spliting and joining methods
                        
c.split()
                        
['list', 'is', 'mutable']
'list,is,mutable'.split()
                        
['list,is,mutable']
'list,is,mutable'.split(',')
                        
['list', 'is', 'mutable']
'list_is_mutable'.split('_')
                        
['list', 'is', 'mutable']
'list is mutable'.split()
                        
['list', 'is', 'mutable']
'list is mutable'.rsplit('  ' ,2)
                        
['list is mutable']
'list is mutable'.rsplit(' '1)
                        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
'list is mutable'.rsplit('',1)
                        
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    'list is mutable'.rsplit('',1)
ValueError: empty separator
'list is mutable'.rsplit(' ',1)
                        
['list is', 'mutable']
'list is mutable'.rsplit('  ',0)
                        
['list is mutable']
s=
                        
SyntaxError: invalid syntax
s='''
python
programming
lamg'''
                        
s
                        
'\npython\nprogramming\nlamg'
splitlines(s)
                        
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    splitlines(s)
NameError: name 'splitlines' is not defined
s.splitlines()
                        
['', 'python', 'programming', 'lamg']
''.join(['', 'python', 'programming', 'lamg'])
                        
'pythonprogramminglamg'
'  '.join(['', 'python', 'programming', 'lamg'])
                        
'  python  programming  lamg'
''.join([1,2,3,4])
                        
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    ''.join([1,2,3,4])
TypeError: sequence item 0: expected str instance, int found
''.join(['1','2','3'])
                        
'123'
'list is mutable'.partition()
                        
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    'list is mutable'.partition()
TypeError: str.partition() takes exactly one argument (0 given)
'list is mutable'.partition('is')
                        
('l', 'is', 't is mutable')
s=('java','python','c++')
                        
s
                        
('java', 'python', 'c++')
s.partition(,)
                        
SyntaxError: invalid syntax
s.partition(',')
                        
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    s.partition(',')
AttributeError: 'tuple' object has no attribute 'partition'
s.partition(',')
                        
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s.partition(',')
AttributeError: 'tuple' object has no attribute 'partition'
>>> 'java','python','c++'.partition(',')
...                         
('java', 'python', ('c++', '', ''))
>>> s='java,python,c++'
...                         
>>> s
...                         
'java,python,c++'
>>> s.partition(',')
...                         
('java', ',', 'python,c++')
>>> s.rpartition(',')
...                         
('java,python', ',', 'c++')
>>> #whitespace and trimming methods
...                         
>>> c='        mahesh       yadav        '
...                         
>>> c
...                         
'        mahesh       yadav        '
>>> c.strip()
...                         
'mahesh       yadav'
>>> c.lstrip()
...                         
'mahesh       yadav        '
>>> c.rstrip()
...                         
'        mahesh       yadav'
>>> text = "Hello café 🙂"
...                         
>>> text.encode()
...                         
b'Hello caf\xc3\xa9 \xf0\x9f\x99\x82'
>>> text.decode()
...                         
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> b'Hello caf\xc3\xa9 \xf0\x9f\x99\x82'.decode()
...                         
'Hello café 🙂'
