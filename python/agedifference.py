import datetime 

dob_1 = input("Please enter a Date")
dob_2 = input("Please enter a Date")
date_object1 = datetime.datetime.strptime(dob_1 , '%d %b %Y')
date_object2 = datetime.datetime.strptime(dob_2, '%d %b %Y')

age_difference=date_object1-date_object2
years=int(age_difference.days/365)
print(abs(years))
