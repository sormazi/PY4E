import re

sum = 0

file = open('regex_sum_167634.txt', 'r')
for line in file:
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        for number in numbers:
            sum += int(number)

print(sum)

# += adds another value with the variable's value and assigns the new value to the variable.

# x = 3
# x += 2
# print (x)
# Output = 5
# -=, *=, /= does similar for subtraction, multiplication and division.
