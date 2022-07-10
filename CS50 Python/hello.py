#Ask the User for their Name, and Removes any whitespace from the string, and Capitalises the User's name
name = input("What's your name? ").strip().title()

#Print Hello and the User's Name to the terminal
print(f"Hello, {name}")
#f indicates special formatting to follow in python, the {} are used to call values determined earlier
#docs.python.org full documentation here