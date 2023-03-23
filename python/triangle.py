

side_one = input("Please enter your length of side one...\n")
side_two = input("Please enter your length of side two...\n")
side_three = input("Please enter your length of side three...\n")
if side_one == side_two and side_two == side_three:
    print("the triangle is an equilateral")
elif side_one == side_two or side_two == side_three or side_one == side_three:
    print("it is an isosceles triangle")
else:
    print("the triangle is scalene")
