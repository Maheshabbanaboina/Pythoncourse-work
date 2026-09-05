''''for i in range(1,10):
    if i==5:
        break
    print(i)
else:
    print("end of the loop")'''

''''pin = 2345
for i in range(4):
 epin = int(input("enter the epin"))
 if pin==epin: 
         print("phone unlocked")
         break
 else:
        print("invalid pin")
else:
    print("try again after 30 sec")'''

#factorial

''''n= int(input("enter the number"))
print("factors:" ,end = ' ')
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=' ')'''

# prime number
'''n= int(input("enter the number:"))
c = 0
for i in range(1,n):
    if n%i==0:
        c+=1
if c==2:
    print("prime number")
else:
    print("not a prime no")'''

n= int(input("enter the number:"))
for i in range(2,n//2+1):
    if n%i==0:
        print("not an prime number")
        break
else:
        print("prime number")