#Write a program which repeateadly reads numbers untill the user enters "done".
#Once "done" is entered, print out the total, count and average of the numbers.
#If the user enters anything other than a number use try and except to detect.
#Print an error message and skip to the next number.

count = 0
total = 0
while True : #using while loop since the problem tell us to repeatedly read numbers till user enters done, hence implying infinity
    sval = input('Enter a number : ')
    if sval == 'done' :
        break
    try : #detecting bad input with try and except as mentioned in problem ; remember to use python3 in terminal to utilise this
        fval = float(sval) #converting the above string to a float type
    except :
        print('Bad data')
        continue #after entering bad data continue keyword drives the program back to the top of the loop, skipping to the next no.
    count = count + 1 #standard logic for count
    total = total + fval #standard logic for summing up all the numbers entered
print('All done')
print('Total : ', total, 'Count : ', count, 'Average : ',total/count) #calculating the average and printing the above mentioned quantities
