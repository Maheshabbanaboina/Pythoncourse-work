'''greater = lambda a,b:a if a>b else b 
print(greater(12,13))
print(greater(40,20))
print(greater(23,56))

wish = lambda name:f'welcome to the course{name}'

print(wish('mahesh'))
print(wish('venu'))
print(wish('nandu'))


iseven = lambda n:"even" if n%2==0 else "odd"
print(iseven(2))
print(iseven(45))
print(iseven(65))

avg = lambda a,b,c:(a+b+c)/3
print(avg(2,4,7))
print(avg(3,45,7))'''


'''domain = lambda mail:(mail.split('@')[-1]).split('.')[0]
print(domain('mahesh@gmail.com'))
print(domain('mahesh@outlook.com'))
print(domain('mahesh@yahoo.com'))'''

'''gst = lambda price : price + price*0.18
print(gst(1000))
print(gst(500))
print(gst(800))'''

'''price = [4324,2436,3534,2355,1345,456,26436,]
result = list(map(lambda price : price +price *0.18,price))
print(result)'''

'''names = ['Mahesh','Nandu','Venu','Rahul','Swamy']
result = list(map(lambda name: name.title(),names))
print(result)'''

'''prices = [123531,5443,15745,33472,537,32465,237235]
result = list(map(lambda price: price - price*0.3,prices))
print(result)'''

'''prices = [123531,5443,15745,33472,537,32465,237235]
result = list(filter(lambda price: price>8000,prices))
print(result)'''

'''from functools import reduce
l = [23,354,25,35,6,34,6,36,34]
res = reduce(lambda sum,i:sum+i,l)
print(res)'''

products = {'sugar' :60,
            'salt' : 50,
            'eggs' : 90,
            'cooking oil' : 120,
             'bread':45
            }
print(dict(sorted (products.items())))
print(dict(sorted(products.items() ,reverse=True)))


        