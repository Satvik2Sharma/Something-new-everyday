s = input("Enter string: ")

# Counting characters using dictionary comprehension.

freq = {c: s.count(c) for c in s}

print(freq)
