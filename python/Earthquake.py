x=input("enter earthquake strength")
x=float(x)
if x>0 and x<2:
    print("Mirco")
if x>2 and x<3:
    print("Very minor")
if x>3 and x<4:
    print("Minor")
if x>4 and x<5:
    print("light")
if x>5 and x<6:
    print("moderate")
if x>6 and x<7:
    print("strong")
if x>7 and x<8:
    print("major")
if x>8 and x<10:
    print("great")
if x>10:
    print("meteorite")


