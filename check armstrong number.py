num = int(input("Enter a number: "))  # take input
temp = num                            # store original number
sum = 0                               # variable to hold the sum of cubes
while temp > 0:
    digit = temp % 10         # get last digit
    sum += digit ** 3         # cube it and add to sum
    temp //= 10               # remove last digit
if num == sum:
    print(num, "is an Armstrong number 💪")
else:
    print(num, "is not an Armstrong number ❌")
