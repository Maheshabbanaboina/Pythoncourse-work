#postional arugments
'''def display(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
display('xyz@gmail.com','xyz','xyz@123')'''

#keyword Arugments
'''def display(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
display(name='Mahesh',email='Mahesh@gmail.com',password='1234')
display(email='Mahesh@gamil.com',name='Mahesh',password='1234')'''

#default arugments
'''def display(name,email,password=''):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
display(name='Mahesh',email='Mahesh@gmail.com',password='1234')
display(email='Mahesh@gamil.com',name='Mahesh',password='1234')
display(name='Mahesh',email='Mahesh@gmail.com')'''

#variable length arguments
'''def display(*names):
    print(names)

display('Mahesh','Venu','Nandu')
display('Mahesh','jagadeesh','saivivek','rahul')
display('Mahesh','yadav')'''

#keyword variable length arugments
'''def profile(**details):
    print(details)
profile( name='Mahesh',age= '22',city= 'Hyderabad',)'''





