import speech_recognition as sr
import pyttsx3 as p3

listener = sr.Recognizer()
engine = p3.init()
voices = engine.getProperty("voices")
# to change voice we have to put 0(for Men vocals) and 1(for Women vocals) at the place of voices[x]
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
