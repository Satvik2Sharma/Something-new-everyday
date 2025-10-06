# Using for loop to add the digits of given number.

n = int(input("Enter number: "))
s = 0
for d in str(abs(n)):
    s += int(d)
print("Sum of digits:", s)