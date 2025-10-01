# using for loop to display all odd numbers in a given range

a, b = map(int, input("Enter range (a b): ").split())
for i in range(a, b+1):
    if i % 2 != 0:
        print(i, end=" ")
