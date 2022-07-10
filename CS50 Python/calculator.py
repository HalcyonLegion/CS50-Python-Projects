#Requests the numbers from the users to determine the value of X and Y however does not specify NOT to return string values as opposed to actual numbers

x = float(input("What's x? "))
y = float(input("What's y? "))

#rounds floating point integers (i.e. numbers with decimals) to whole integers
z = round(x + y)

#automatically adds commas to long numbers
print(f"{z:,}")