import speech_recognition as sr
import wikipedia
import openai
import os


import pyttsx3



def say(text):
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()




def type(text1):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("You typed "+ text1)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        querry  = r.recognize_google(audio , language = "en-in")
        print(f"user said: {querry}")
        say(querry)




say("Hello, I am Jarvis AI. built by Neeraj Patil.  ")
#y = input()
#type(y)
print("listening....")
text = takeCommand()


  