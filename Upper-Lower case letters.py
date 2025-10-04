# Distinguishing Uppercase and Lowercase letters using if, elif and else statements.

char = input("Enter character: ")
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
else:
    print("Not an alphabet")
