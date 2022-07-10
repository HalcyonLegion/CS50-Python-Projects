#create a library of emojis and corresponding icons
def  emoji_converter(Message):
     words = Message.split( " ")
     emojis = {
        ":)" : "🙂",
        ":(" : "🙁",
     }
     outcome = " "
     for word in words:
         outcome += emojis.get(word, word) + " "
     return outcome


Message = input("Please enter text with either :) or :( here! ")
print(emoji_converter(Message))