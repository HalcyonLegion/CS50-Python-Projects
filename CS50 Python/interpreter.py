#Need to implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value
#To 1 decimal place

expression = input("Expression: ")

x, y, z = expression.split(" ")

in_x = float(x)
in_z = float(z)

if y == "+":
    result = in_x + in_z
if y == "-":
    result = in_x - in_z
if y == "*":
    result = in_x * in_z
if y == "/":
    result = in_x / in_z
print(result)