import speech_recognition as sr
import pyttsx3 as p3

listener = sr.Recognizer()
engine = p3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("This is jarvis, personal assigtent of Iron man")
engine.runAndWait()

try:
    with sr.Microphone() as souce:
        print("listening...")
        voice = listener.listen(souce)
        commond = listener.recognize_google(voice)
        commond = commond.lower()
        if "jarvis" in commond:
            print(commond)
except:
    pass
