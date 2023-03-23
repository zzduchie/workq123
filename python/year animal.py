
year = int(input("enter your year"))
print(year)
year_names = ["dragon","snake","horse","sheep","monkey","rooster","dog","pig","rat","ox","tiger","hare"]

if (year-2000) % 12 == 0:
    print("Dragon")
elif  (year-2000) % 12 == 1:
    print("Snake")
elif  (year-2000) % 12 == 2:
    print("horse")
elif  (year-2000) % 12 == 3:
    print("sheep")
elif  (year-2000) % 12 == 4:
    print("monkey")
elif  (year-2000) % 12 == 5:
    print("rooster")
elif  (year-2000) % 12 == 6:
    print("dog")
elif  (year-2000) % 12 == 7:
    print("pig")
elif  (year-2000) % 12 == 8:
    print("rat")
elif  (year-2000) % 12 == 9:
    print("ox")
elif  (year-2000) % 12 == 10:
    print("tiger")
elif  (year-2000) % 12 == 11:
    print("hare")
else:
    print("Invalid Year")