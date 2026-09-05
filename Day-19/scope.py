'''def display(n):
    n=n+40
    print('Inside:',n)
n=10
display(n)
print('Outside:',n)'''

'''def display(n):
    print('Inside:',n)
n=10
display(n)
print('Outside:',n)'''

'''def display(n):
    n=n+30
    print('Inside:',n)
display(n)
print('Outside:',n)'''

'''def display():
    global n 
    n=n+20
    print('Inside:',n)
n=10
display()
print('Outside:',n)'''

'''def display():
    global n 
    n='PFS'
    print("updated course:",n)

n = 'JFS'
display()
print("Final course:",n)'''

'''def display():
    n = 'JFS'
    def update():
        nonlocal n
        n = 'PFS'
        print("updated course:",n)
    update()
    print("Final course",n)
display()'''





    
