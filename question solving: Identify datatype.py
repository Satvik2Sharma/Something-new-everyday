#  QUESTION:
#  How will you identify which of following is a string, list, tuple, set or dictionary?
#  {5,17,26.2}, [11,2,3.14,’cyber’], {13 : ‘simple’,32 : ‘complicated’, 12 : ‘complex’}
#  “check it!”
#  1 + 2j


#  SOLUTION:

# Identifying different data types using the built-in type() method.
# Define various data structures and types
data1 = {5, 17, 26.2}  # A set
data2 = [11, 2, 3.14, 'cyber']  # A list
data3 = {13: 'simple', 32: 'complicated', 12: 'complex'}  # A dictionary
data4 = "check it!"  # A string
data5 = 1 + 2j  # A complex number
# Use type() to identify and print the type of each variable
# Assign the type result to a variable before printing for clarity
type_data1 = type(data1)
type_data2 = type(data2)
type_data3 = type(data3)
type_data4 = type(data4)
type_data5 = type(data5)
print("{5,17,26.2} is of type", type_data1)
print("[11,2,3.14,'cyber'] is of type", type_data2)
print("{13:'simple',32:'complicated',12:'complex'} is of type", type_data3)
print('"check it!" is of type', type_data4)
print("1 + 2j is of type", type_data5)


#  OUTPUT:
#  {5,17,26.2} is of type <class 'set'>
#  [11,2,3.14,'cyber'] is of type <class 'list'>
#  {13:'simple',32:'complicated',12:'complex'} is of type <class 'dict'>
#  "check it!" is of type <class 'str'>
#  1 + 2j is of type <class 'complex'>
