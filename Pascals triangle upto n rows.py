num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))

for i in range(num_rows):
    # Print leading spaces for alignment
    for k in range(1, num_rows - i):
        print(" ", end="")

    # Calculate and print elements of the current row
    current_coefficient = 1
    for j in range(0, i + 1):
        print(current_coefficient, end=" ")
        current_coefficient = current_coefficient * (i - j) // (j + 1)
    print()
