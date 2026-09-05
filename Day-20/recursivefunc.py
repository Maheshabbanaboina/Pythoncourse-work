'''def display(n):
    if n>5:
        return
    print(n)
    display(n+1)
display(1)''' 

#from 10 to 1 numbers
'''def display(n):
    if n>10:
        return
    display(n+1)
    print(n)
display(1)'''

#print sum of n numbers
'''def displaysum(n):
    if n==0:
        return 0 
    return n+displaysum(n-1)
print(displaysum(8))'''

#product of n numbers
'''def productofn(n):
    if n ==1:
        return 1
    return n*productofn(n-1)
print(productofn(4))'''

#iteration of each character using recursion
def display(ind):
    if ind == len(s):
        return
    display(ind+1)
    print(s[ind],end = '')
s= "Mahesh yadav"
display(0)


'''s = "python"
def display(n):
    if n>len(s):
        return
    print(s[:n])
    display(n+1)
display(1)'''

'''def display(ind,w):
    if ind>len(s)-w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)
s = "Mahesh Abbanaboina"
display(0,20)'''

'''n = 987654
def display(n):
    if n == 0:
        return
    display(n//10)
    print(n % 10)
display(n)'''

#sum

'''n = 987654
def display(n):
    if n == 0:
        return 0
    return n%10+display(n//10)
    
print(display(n))'''




 

