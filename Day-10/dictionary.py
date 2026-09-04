Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data = {'name':'mahesh','batch':63,'course':'PFS'}
data['name']
'mahesh'
data['batch']
63
data['course']
'PFS'
63 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age','key is not present')
'key is not present'
data.get('course','key is not present')
'PFS'
data['batch']=64
data
{'name': 'mahesh', 'batch': 64, 'course': 'PFS'}
data['skills']= ['python','mysql','flask']
data
{'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data['age']=21
data
{'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
data.update({'phone no':90653282537,'email':'mahesh@gmail.com'})
data
{'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phone no': 90653282537, 'email': 'mahesh@gmail.com'}
data.pop('age')
21
data.pop('skills')
['python', 'mysql', 'flask']
del data['name']
data
{'batch': 64, 'course': 'PFS', 'phone no': 90653282537, 'email': 'mahesh@gmail.com'}
data.popitem()
('email', 'mahesh@gmail.com')
data.popitem()
('phone no', 90653282537)
data.clear()
data
{}
data=
{'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phone no': 90653282537, 'email': 'mahesh@gmail.com'}

SyntaxError: invalid syntax

data={'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phone no': 90653282537, 'email': 'mahesh@gmail.com'}
data
{'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phone no': 90653282537, 'email': 'mahesh@gmail.com'}
data.keys()
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phone no', 'email'])
data.values()
dict_values(['mahesh', 64, 'PFS', ['python', 'mysql', 'flask'], 21, 90653282537, 'mahesh@gmail.com'])
data.items()
dict_items([('name', 'mahesh'), ('batch', 64), ('course', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('age', 21), ('phone no', 90653282537), ('email', 'mahesh@gmail.com')])
sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phone no', 'skills']
sorted(data,reverse=True)
['skills', 'phone no', 'name', 'email', 'course', 'batch', 'age']
max(data)
'skills'
min(data)
'age'
data
{'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phone no': 90653282537, 'email': 'mahesh@gmail.com'}
data.pop('age')
21
data
{'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phone no': 90653282537, 'email': 'mahesh@gmail.com'}
data['age']
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age')
data.setdefalut('age',0)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    data.setdefalut('age',0)
AttributeError: 'dict' object has no attribute 'setdefalut'. Did you mean: 'setdefault'?
>>> data.setdefault('age'.0)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> data.setdefault('age',0)
0
>>> data
{'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phone no': 90653282537, 'email': 'mahesh@gmail.com', 'age': 0}
>>> data.setdefault('name','rahul')
'mahesh'
>>> data
{'name': 'mahesh', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phone no': 90653282537, 'email': 'mahesh@gmail.com', 'age': 0}
>>> a={1:1,2:2}
>>> b=a
>>> b[3]=3
>>> a
{1: 1, 2: 2, 3: 3}
>>> b
{1: 1, 2: 2, 3: 3}
>>> c=a.copy()
>>> c=[4]=4
SyntaxError: cannot assign to literal
>>> c = [4]=4
SyntaxError: cannot assign to literal
>>> c=[a]=4
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    c=[a]=4
TypeError: cannot unpack non-iterable int object
>>> c=[5]=4
SyntaxError: cannot assign to literal
>>> c[5]=4
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    c[5]=4
TypeError: 'int' object does not support item assignment
>>> c=a.copy()
>>> c[4]=4
>>> c
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3}
>>> d=dict.fromkeys(['a','b'],0)
>>> d
{'a': 0, 'b': 0}
