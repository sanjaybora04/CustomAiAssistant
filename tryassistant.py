import assistant

while True:
    sentence = input("You : ")
    print("Assistant : ",assistant.chat.reply(sentence))