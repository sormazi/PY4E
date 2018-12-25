#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except
#Put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.

largest_no = None
smallest_no = None
while True :
    sval= input('Enter a number : ')
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except :
        print("Invalid input")
        continue
for fval in [7,2,10,4] :
    if largest_no is None :
        largest_no = fval
    elif fval > largest_no :
        largest_no = fval
print("Maximum is: ",largest_no)
for fval in [7,2,10,4] :
    if smallest_no is None :
        smallest_no = fval
    elif fval < smallest_no :
        smallest_no = fval
print("Minimum is: ",smallest_no)
