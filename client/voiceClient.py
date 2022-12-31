import pyttsx3
import speech_recognition as sr
import requests
import json

engine = pyttsx3.init()
voicespeed = 150
engine.setProperty('voice', 'english+f3')
engine.setProperty('rate', voicespeed)
url = "http://127.0.0.1:5000"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1.2
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio)
    except Exception as e:
        print(e)
        print("---")

        return "None"
    return query

while True:
    sentence = takeCommand()
    print("You:",sentence)
    r = requests.post(url+'/assistant',data = json.dumps({"msg":sentence}))
    r = json.loads(r.text)
    print("Assistant : ",r["msg"])
    speak(r["msg"])