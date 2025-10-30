s = input("Enter the numbers separated by spaces: ")

# Split the input string into a list of strings and convert each string to an integer using map.

alist = list(map(int, s.split()))

# Using sort() method to arrange the numbers in ascending order.
alist.sort()

print(alist)
