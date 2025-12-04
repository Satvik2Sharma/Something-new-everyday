a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
result = 1

for i in range(b):
    result *= a

print("Result =", result)
