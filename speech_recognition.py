from math import exp
import speech_recognition as sr
listener = sr.Recognizer()
try:
    with sr.Microphone() as souce:
        print("listening...")
        voice = listener.listen(souce)
        commond = listener.recognize_google(voice)
        print(commond)
except:
    pass
