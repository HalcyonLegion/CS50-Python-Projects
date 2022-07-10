#Prompt the user for a mass m in Kilograms, Joules is known so it's fixed e, and c is the result
m = float(input("What is the Mass in Kilograms? "))
e = int(90000000000000000)

c = round(m * e)

print (f"{c}")