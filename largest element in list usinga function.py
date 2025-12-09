numbers = list(map(int, input("Enter numbers: ").split()))
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number =", largest)
