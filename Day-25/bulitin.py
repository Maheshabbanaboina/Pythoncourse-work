'''import sys
#print(sys.path)
#print(sys.argv)
#print(sys.version)
print("start")
sys.exit()
print("end")'''

'''#platform
import platform
print(platform.system())
print(platform.release())
print(platform.processor())'''


'''import math
print(math.pi)
print(math.e)

print(math.sqrt(4))
print(math.pow(6,5))

print(math.ceil(12.45))
print(math.ceil(13.04))
print(math.ceil(11.05))
print(math.ceil(7.985))

print(math.floor(12.06))
print(math.floor(15.00))
print(math.floor(17.06))
print(math.floor(18.56))'''

'''import math
print(math.factorial(10))
print(math.factorial(8))

print(math.gcd(3,5))
print(math.gcd(10,5))

print(math.fabs(-10))
print(math.log(3.8))
print(math.sin(60))
print(math.cos(30))
print(math.tan(90))
print(math.degrees(30))
print(math.radians(80))'''


'''import random
print(random.random())
print(random.randint(2,10))
print(random.uniform(4,16))


l = ["mahesh","venu","rahul"]
print(random.choice(l))
print(random.choices(l,k=2))

random.shuffle(l)
print(l)'''

from  collections import Counter
s= "python programming"
'''m = 'this is that that is this is that is is '.split()
l= [13,32,42.2,11,2,12,12,12,1,3,1,3,1,2,1,2,31,1,1,]
print(Counter(s))
print(Counter(m))
print(Counter(l))'''


d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

'''s = "Mahesh Yadav"
from collections import defaultdict
d = defaultdict(int)
for i in s:
    d[i]+=1
print(d)'''

'''from collections import deque
l = deque([])
l.append(10)
l.append(20)
l.append(50)
l.pop()
l.pop()
l.append(45)

print(l)'''


'''from itertools import combinations,permutations

res1 = list(combinations('Mahi',2))
res2 = list(permutations('Mahi',2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])


print(list(combinations('Mahi',2)))
print(list(permutations('Mahi',2)))'''




