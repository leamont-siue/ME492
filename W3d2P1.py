#Leanne Montgomery
from numpy import*

Hours= int(input("Please enter the number of hours: "))
RPH= int(input("Please enter the rate per hour: "))



if Hours >= 40:
	basehours = 40
	overtime = Hours - 40
else:
	basehours = Hours
	overtime = 0

basepay = basehours * RPH
overtime_pay= 1.5 * RPH * overtime 

paycheck = basepay + overtime_pay

print ('Basepay is $', basepay)
print ('Overtime is $', overtime_pay)
print ('Total paycheck is $', paycheck)
