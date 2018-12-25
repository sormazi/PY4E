# Wage calculation program
h = input("Enter number of hours: ")
hrs = float(h)
r = input("Enter  hourly rate: ")
hr_rate = float(r)
if hrs <= 40 :
    wage = hrs * hr_rate
    print('The wage is', wage)
elif hrs > 40 :
    s = hrs - 40
    wage = 40 * hr_rate + s * 1.5 * hr_rate
    print('The wage is', wage)
