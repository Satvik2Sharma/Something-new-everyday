numbers = []

print("Enter numbers separated by space: ")

while True:
    s = input()
    if s == "":
        break
    numbers.append(int(s))

k = int(input("Enter the number who's successors you wannna find: "))

for x in numbers:
    if x > k:
        print(x)
