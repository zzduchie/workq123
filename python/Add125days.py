import datetime 

date_input = input("Please enter a Date")
date_object = datetime.datetime.strptime(date_input, '%d %b %Y')
DD = datetime.timedelta(days=125)
date2=date_object-DD
print(date2)
