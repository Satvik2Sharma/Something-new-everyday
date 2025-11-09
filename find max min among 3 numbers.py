# Write a program to find the maximum and minimum of three numbers using nested if-else.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# finding Maximum using nested if-else
if a > b:
    if a > c:
        maximum = a
    else:
        maximum = c
else:
    if b > c:
        maximum = b
    else:
        maximum = c

# finding Minimum using nested if-else
if a < b:
    if a < c:
        minimum = a
    else:
        minimum = c
else:
    if b < c:
        minimum = b
    else:
        minimum = c

print("Maximum =", maximum)
print("Minimum =", minimum)
