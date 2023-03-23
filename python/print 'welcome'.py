def welcome():
    print("welcome")

welcome()

def addition():
    x = input("Type a number: ")
    y = input("Type another number: ")
    sum = int(x) + int(y)

    print("The sum is: ", sum)
addition()

def subtraction():
    x = input("Type a number: ")
    y = input("Type another number: ")

    sum = int(x) - int(y)
    print("The sum is: ", sum)
subtraction()

def names():
    fname = input("input first name: ")
    lname = input("input your last name: ")
    print (f"hello {fname} {lname}")
names()