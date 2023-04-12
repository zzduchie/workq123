x=input("enter your score")
x=float(x)
if x>0 and x<0.4:
    print("Unacceptable performance", x*2400)
if x>0.39 and x<0.6:
    print("Acceptable performance" , x*2400)
if x>0.59:
    print ("Meritorious performance" , x*2400)

