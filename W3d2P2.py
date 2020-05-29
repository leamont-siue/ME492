#Leanne Montgomery
from numpy import*

Hours= int(input("Please enter the number of hours: "))
RPH= int(input("Please enter the rate per hour: "))

def computepay(hours, rate):
	if hours >=40:
		basehours = 40
		overtime = hours-40
	else:
		basehours = Hours
		overtime = 0
	grosspay = basehours * rate + overtime * 1.5 * rate
	return grosspay

gross_pay = computepay(Hours, RPH)

print (Hours, ' hours worked.')
print ('Gross pay is $', gross_pay)
