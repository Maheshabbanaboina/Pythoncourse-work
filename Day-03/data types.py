Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
age=21
type(age)
<class 'int'>
price=10.5
type(price)
<class 'float'>
z=5+2j
type(z)
<class 'complex'>
#sequence data types
text="python"
type(text)
<class 'str'>
numbers=[10,20,30]
type(numbers)
<class 'list'>
numbers[1]
20
data=(1,2,4)
type(data)
<class 'tuple'>
colors={"red","blue","white"}
type(colors)
<class 'set'>
tags=frozenset(["sales","trending"])
type(tags)
<class 'frozenset'>
tags.remove(sales)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tags.remove(sales)
AttributeError: 'frozenset' object has no attribute 'remove'
#mapping type
student={"name":"mahesh"}
type(student)
<class 'dict'>
student["name"]="venu"
student[name]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    student[name]
NameError: name 'name' is not defined
student["name"]
'venu'
#boolean type
a=0
type(a)
<class 'int'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> #none datatype
>>> tracking_id=none
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tracking_id=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> #mutable datatypes
>>> list
<class 'list'>
>>> set
<class 'set'>
>>> dict
<class 'dict'>
>>> #immutable datatypes
>>> int
<class 'int'>
>>> float
<class 'float'>
>>> str
<class 'str'>
>>> tuple
<class 'tuple'>
>>> frozenset
<class 'frozenset'>
>>> bool
<class 'bool'>
>>> noneType
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    noneType
NameError: name 'noneType' is not defined
>>> //#mutable datatypes
SyntaxError: invalid syntax
>>> list
<class 'list'>
>>> set
<class 'set'>
>>> dict
<class 'dict'>
>>> #immutable data types
