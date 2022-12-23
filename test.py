import chatbot

while True:
    sentence = input("You : ")
    print(chatbot.chat.reply(sentence))