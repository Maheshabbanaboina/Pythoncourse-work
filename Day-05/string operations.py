Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string operations
#concatenation
s=''
s
''
s='codegnan'
s
'codegnan'
'codegnan'+'pfs'
'codegnanpfs'
>>> 'codegnan'*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
>>> '_*_'*20
'_*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*_'
>>> #indexing
>>> s='codegnan'
>>> s[4]
'g'
>>> s[0]
'c'
>>> s[6]
'a'
>>> s[-1]
'n'
>>> s[-3]
'n'
>>> s[-7]
'o'
>>> names='mahesh rahul venu yadav'
>>> names[0]
'm'
>>> names[3]
'e'
>>> names[8]
'a'
>>> #s[start:end+1:step]+>[0:len:1]
>>> names[0:5]
'mahes'
>>> names[0:7]
'mahesh '
>>> names[7:13]
'rahul '
>>> names[13:18]
'venu '
>>> #membership
>>> mahesh not in names
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    mahesh not in names
NameError: name 'mahesh' is not defined
>>> 'mahesh' in names
True
>>> 'karthik' in names
False
>>> 'rahul' in names
True
