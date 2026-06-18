stack_1 = []
stack_2 = []
a = int(input())

for _ in range(a):
    query = list(map(int, input().split()))
    operation = query[0]
    
    if operation == 1:
        stack_1.append(query[1])

    elif operation == 2:
        if not stack_2:
            while stack_1:
                stack_2.append(stack_1.pop())
        stack_2.pop()

    elif operation == 3:
        if not stack_2:
            while stack_1:
                stack_2.append(stack_1.pop())
        print(stack_2[-1])
