S = input("Enter a string: ")

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

# sing For loop , lower() method to determine the vowels.

result = S # Initialize result with the original string.

for i in S: # Iterate through the original string to preserve order.

 if i in vowels:

# Using replace method to remove vowels.

  result = result.replace(i, "")

print("After removing vowels", result)
