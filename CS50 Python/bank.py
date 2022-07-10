#Ask for Input it needs to begin with h or contain Hello or not contain Hello
greeting = input("Greeting: ").lower().strip()

if "hello" in greeting:
    print("$0")

elif "h" == greeting[0]:
    print("$20")

else:
    print("$100")