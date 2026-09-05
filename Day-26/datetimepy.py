from datetime import date,time,datetime,timedelta

today = date.today()

print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())


t = time(23,6,5)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

#date and time
n = datetime.now()
print(n)
print(n.today)
print(n.month)
print(n.year)
print(n.weekday())
print(n.hour)
print(n.minute)
print(n.second)
print(n.strftime('%d-%m-%Y'))
print(n.strftime('%d-%m-%Y %H:%M:%S'))
print(n.strftime('%d-%m-%Y %H:%M:%S %p'))
print(n.strftime('%d-%b-%Y %H:%M:%S %p'))
print(n.strftime('%d-%B-%Y %H:%M:%S %p'))
print(n.strftime('%a,%d-%B-%Y %H:%M:%S %p'))
print(n.strftime('%A,%d-%B-%Y %H:%M:%S %p'))

#timedelta
t = date.today()
n = datetime.now()
t5 = t + timedelta(days=5)
t6 = t - timedelta(days=4)
n30 = n + timedelta(minutes=30)
print(t,t5)
print(n,n30)








