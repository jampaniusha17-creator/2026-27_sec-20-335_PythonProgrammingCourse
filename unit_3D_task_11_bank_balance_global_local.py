balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)
    print("Updated balance:", balance)

def local_balance(amount):
    balance = 500
    balance += amount
    print("Local balance:", balance)

print("Initial balance:", balance)

deposit(200)

local_balance(300)

print("Final account balance:", balance)