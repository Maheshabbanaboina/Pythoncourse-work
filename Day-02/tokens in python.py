Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tokens in python
>>> #keywords
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keyword.kwlist))
35
>>> #variables
>>> product_name = 'laptop'
>>> price = 4500
>>> in_stock = True
>>> print(product_name,price,in_stock)
laptop 4500 True
>>> a,b,c=10,20,30
>>> print(a,b,c)
10 20 30
>>> x=10
>>> x=10
>>> x
10
>>> x=5
>>> x=10
>>> x
10
>>> x=5
>>> x
5
>>> a,b=5,10
>>> a,b
(5, 10)
>>> b,a
(10, 5)
>>> a,b=b,a
>>> a,b
(10, 5)
