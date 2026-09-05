'''i = 10
while i>=0:
    print(i)
    i-=1'''
#even number from 100 to 0
'''i=100
while i>0:
    print(i)
    i-=2'''

'''s = 'python programming'
i = 0
while i<=len(s)-1:
    print(s[i], end='')
    i+=1'''

'''l = [1,0,1,1,1,1,1,1,1,23,4,65,2,554,0,0,0,]
while 0 in l:
    l.remove(0)
print(l)'''

'''data = {}
total_bill = 0

while True:
    product = input("enter the product(for exit):")
    if product =='exit':
        break
    price = float(input("enter the price"))
    total_bill+=price
    data[product]=price

print(data)
print("TOTAL bill:",total_bill)'''

#whilewithelse
i = 0
while i<=10:
    i+=1
    if i==11:
        break
    print(i)
else:
    print("end of the loop")

