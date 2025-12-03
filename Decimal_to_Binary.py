n = int(input("Enter decimal number: "))
binary = ""

if n == 0:
    print("0")
else:
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    print("Binary =", binary)
