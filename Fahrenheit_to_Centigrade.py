# Program to convert Fahrenheit degree temperature to Centigrade degree.

# Prompt user to enter temperature in Fahrenheit
fahrenheit_input = input("Enter temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_input)

# Calculate Centigrade temperature using the conversion formula
# C = (F - 32) * 5 / 9
centigrade_raw = (fahrenheit - 32) * 5 / 9

# Round the centigrade temperature to two decimal places
centigrade_rounded = round(centigrade_raw, 2)

# Print the converted temperature
print("Temperature in Centigrade:", centigrade_rounded)

# FACT: -40 degree Centigrade is equal to -40 degree Fahrenheit.
