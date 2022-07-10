#ask for input
thought = input("What is the Answer to the Great Question of Life, the Universe, and Everything? " ).strip().lower()

if thought == "42":
    print("Yes")
elif thought == "forty two":
    print("Yes")
elif thought == "forty-two":
    print("Yes")
else:
    print("No")
