data = {
    211604: {'pin':1234,'balance':10000,'history':[]},
    211605: {'pin':1234,'balance':10000,'history':[]},
    211606: {'pin':1234,'balance':10000,'history':[]},
    211607: {'pin':1234,'balance':10000,'history':[]},
    
}

def menu():
    print('[C]heck balance')
    print('[D]epoist')
    print('[W]ithdraw')
    print('[V]iew transactions')
    print('[E]xit')

def login():
    global acc_num
    acc_num = int(input("enter the account number:"))
    pin = int(input("enter the pin:"))
    if acc_num in data and data[acc_num]['pin']==pin:
        print("login successful")
        return True
    else:
        
        