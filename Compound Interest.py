# Mathematically calculating compound interest.

p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
ci = p * ((1 + r/100) ** t - 1)
print("Compound Interest:", ci)
