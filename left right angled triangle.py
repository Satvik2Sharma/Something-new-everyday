# Using for loop to print a right angled triangle using asterisk(*) of any height.

n = int(input("Enter height: "))
for i in range(1, n+1):
    print("*" * i)
