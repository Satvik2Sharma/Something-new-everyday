# Using while loop to find Highest Common Factor of two numbers.

a, b = map(int, input("Enter 2 numbers: ").split())
while b:
    a, b = b, a % b
print("HCF:", a)