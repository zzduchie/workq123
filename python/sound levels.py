x=input("enter a sound level")
x=int(x)
if x>0 and x<40:
    print("Quiet room")
if x>40 and x<70:
    print("Alarm clock")
if x>70 and x<106:
    print("Petrol lawnmower")
if x>130:
    print("Jackhammer")


