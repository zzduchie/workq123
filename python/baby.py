from datetime import datetime
from datetime import timedelta
date_input = input("Please enter you age DD MM YY")
date_object = datetime.strptime(date_input, '%d %b %Y')
print(date_object.year)
datetime.today()
my_age = datetime.today() - date_object
print(my_age)
print ("My exact age just in years is ", int(my_age.days/365), "years\n")