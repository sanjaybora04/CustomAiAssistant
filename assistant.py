import chatbot

while True:
    sentence = input("You : ")
    print("Assistant : ",chatbot.chat.reply(sentence))