try:
    a = int(input())
except ValueError:
    print("Enter the correct datatype")
else:
    print("a=",a)
finally:
    print("end of the program")


#for multiple errors:
'''try:
    a = int(input())
    k = {1:3,34:45}
    print(k[14])
    print(l[10])
    print(10/0)
    print('1'+1)
except ValueError:
    print("Enter the correct datatype")
except KeyError:
    print("key is not there")
except IndexError:
    print("index out of range")
except ZeroDivisionError:
    print("cannot divide with zero")
except TypeError:
    print("define the program")
except NameError:
    print("enter the correct variable")
else:
    print("error free program")
finally:
    print("end of the program")'''
'''try:
    a = int(input())
    k = {1:3,34:45}
    print(k[14])
    print(l[10])
    print(10/0)
    print('1'+1)
except (ValueError,IndexError,TypeError,ZeroDivisionError,NameError,KeyError) as e:
     print("error occured:",e)
else:
     print("error free program")
finally:
     print("end of the program")'''


#easy method
'''try:
    a = int(input())
    k = {1:3,34:45}
    print(k[14])
    l = [231,55]
    print(l[10])
    print(10/0)
    print('1'+1)
except Exception as e:
     print("error occured:",e)
else:
     print("error free program")
finally:
     print("end of the program")'''
try:
     amount = int(input("enter the amount:"))
     balance = 80000
     if amount<0:
      raise Exception("amount needs to be positive")

except Exception as e:
     print("error occured:",e)
else:
     print("error free program")
finally:
     print("end of the program")
