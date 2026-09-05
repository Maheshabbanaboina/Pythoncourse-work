'''s = 'mahesh yadav'
for i in range(len(s)):
 if s[i] in 'aeiouAEIOU':
  print(i,s[i])'''

'''l= [23,45,67,12,45,67,78,89,57,34]
sum=0
for i in range(len(l)):
 if l[i]%2==0:
  sum=sum+i
  print(i,l[i])
print(sum)'''

'''n = int(input("enter the number"))
fact = 1
for i in range(1,n+1):
    fact*=i
print(f"factorial of {n} is {fact}")'''

'''data = {}
n = int(input("enter the no of students:"))
max_marks = 0
for i in range(n):
     name = input("enter the name:")
     marks = int(input("enter the marks:"))
     if marks > max_marks:
         max_marks = marks
data[name]=marks
print(data)
print("Maximum Marks:",max_marks)'''

'''n = int(input("enter the no of products:"))
total_bill = 0
products = {}
for i in range(n):
    product = input("enter the product")
    price = float(input("enter the price"))
    quantity= int(input("enter the quantity"))
    final_price = price * quantity
    total_bill += final_price
    products[product] = f'{price} * {quantity} = {total_bill}'
    print(products)
print("Total Bill:",total_bill)'''





        
