'''l = [1,2,3,4,5]
sum=15
max=20
print(max)'''

#int float str list tuple set dict bool 
#int float str tuple bool -immutable values-pass by value
#list set dict-mutable values -pass by refernce

#int
'''def display(n):
    n= n+10
    print("Inside:",n)
n=10
display(n)
print("Outside:",n)'''

#float
'''def display(n):
    n += 10.5
    print("Inside:",n)
n=11.5
display(n)
print("Outside:",n)'''

#str
'''def display(n):
    n += "lang"
    print("Inside:",n)
n="python"
display(n)
print("Outside:",n)'''

#list
'''def display(n):
    n +=[1,2,3,4]
    print("Inside:",n)
n=[2,3,4,5,6]
display(n)
print("Outside:",n)'''

#bool
'''def display(n):
    n= False
    print("Inside:",n)
n= True
display(n)
print("Outside:",n)'''

#dict
'''def display(n):
    n[5]=6
    print("Inside:",n)
n= {'2':'5','4':'6'}
display(n)
print("Outside:",n)'''