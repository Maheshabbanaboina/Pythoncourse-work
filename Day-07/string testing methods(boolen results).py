Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#STRING TESTING METHODS
s="python.py"
s.startswith("py")
True
s.startswith("mahesh")
False
s.endswith("py")
True
>>> s.endswith("zd")
False
>>> s.isaplha
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.isaplha
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
>>> s.isalpha()
False
>>> s="Hello"
>>> s.isalpha()
True
>>> s="mahesh"
>>> s.isalpha()
True
>>> s="mahesh123"
>>> s.isalpha()
False
>>> s="MAhesh"
>>> s.islower()
False
>>> s="mahesh"
>>> s.islower
<built-in method islower of str object at 0x000001CC9C445830>
>>> s.islower()
True
>>> s="HELLO"
>>> s.isupper()
True
>>> s='Upper()
SyntaxError: unterminated string literal (detected at line 1)
>>> s="Upper"
>>> s.isupper()
False
>>> s="mahesh yadav"
>>> s.isspace()
False
>>> s=" ".isspace()
>>> s
True
>>> s="identifier12"
>>> s.isidentifier()
True
>>> s="2identifier"
>>> s.isidentifier()
False
