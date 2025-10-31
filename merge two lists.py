# Gtting input strings of numbers separated by spaces for two lists and convert them to lists of integers.
a = list(map(int, input("Enter list1: ").split()))
b = list(map(int, input("Enter list2: ").split()))

# Initialising an empty list to store the merged list without duplicates.
c = []

# Using for loop to Iterate through the elements of both lists.
for i in a+b:
# If the element is not already in the result list, using append() method.
    if i not in c:
        c.append(i)

print(c)