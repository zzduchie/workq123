print ("Welcome to get taxed")
salary=input("How much did you earn this year?")
salary = int(salary)
if salary <= 14000:
    tax = salary * 0.1050
elif salary <= 48000:
    tax = 1470+(salary-14000) * 0.1750
elif salary <= 70000:
    tax = 7420+(salary-48000) * 0.30
elif salary <= 180000:
    tax = 14020+(salary-70000) * 0.33
else:
    tax = 50320+(salary-180000) * 0.39
print(tax)
