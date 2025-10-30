 Getting input string of numbers separated by spaces from the user and convert to a list of integers.
alist = list(map(int, input("Enter list: ").split()))

# Converting the list to a set to remove duplicates, then convert back to a list.
alist = list(set(alist))

# Using sort() method to arrange the list in ascending order.
alist.sort()

# using if and else statements to check if the list has more than one element.
if len(alist) > 1:
    # If yes, print the second to last element (which is the second largest after sorting)
    print("Second largest:", alist[-2])
else:
    print("No second numbers provided.")
