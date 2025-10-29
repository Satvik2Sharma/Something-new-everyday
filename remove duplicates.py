 Using for loop and append() method.
# To remove duplicates from a list without using sets.


alist = list(map(int, input("Enter list: ").split()))
res = []
for i in alist:
    if i not in res:
        res.append(i)
print(res)
