from urllib import request
import speech_recognition as sr
import pyttsx3 as p3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess
from colorama import Fore
import urllib
import pyaudio

listener = sr.Recognizer()
engine = p3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_commond():
    try:
        with sr.Microphone() as souce:
            print("listening...")
            voice = listener.listen(souce)
            commond = listener.recognize_google(voice)
            commond = commond.lower()
            if "jarvis" in commond:
                commond = commond.replace("jarvis", "")
                print(commond)

    except:
        pass
    return commond


def run_jarvis(play_yt, time, birthday_chaitanya, today_date):
    commond = take_commond()
# To stop Jarvis
    if "stop" in commond:
        print(Fore.YELLOW+"I am going to sleep now\nif you want to wake me\nclick on run")
        print(Fore.WHITE)
        talk("I am going to sleep now, if you want to wake me, click on run")
        exit()
# to repeat after you.
    elif "repeat" in commond:
        print(Fore.YELLOW+commond)
        print(Fore.WHITE)
        repeat = commond.replace("repeat", "")
        talk(repeat)
# To play something in Youtube.
    elif "play" in commond:
        play_yt = commond.replace("play", "")
        print(Fore.YELLOW + play_yt)
        print(Fore.WHITE)
        talk("playing"+play_yt)
        pywhatkit.playonyt(play_yt)
# To get current date and time both.
    elif "date and time" in commond:
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        print(commond)
        print(Fore.YELLOW + current_datetime)
        print(Fore.WHITE)
        current_datetime = str(current_datetime)
        talk("current and date time are "+current_datetime)
# To get only date.
    elif "date" in commond:
        today_date = datetime.date.today()
        print(commond)
        today_date = str(today_date)
        print(Fore.YELLOW + today_date)
        print(Fore.WHITE)
        talk("today's date is "+today_date)
# To get only time.
    elif "time" in commond:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(commond)
        print(Fore.YELLOW + time)
        print(Fore.WHITE)
        talk("current time is"+time)
# To ask chaitanya's birthday and play Happy birthday song.
    elif "chaitanya's" and "birthday" in commond:
        birthday_chaitanya = datetime.date(2003, 7, 21)
        print(commond)
        print(Fore.YELLOW + birthday_chaitanya)
        print(Fore.WHITE)
        birthday_chaitanya = str(birthday_chaitanya)
        talk("chaitanya's birthday is on "+birthday_chaitanya)
        pywhatkit.playonyt("happy birthday ryhme song")
# To get Jokes.
    elif "joke" in commond:
        joke = pyjokes.get_joke()
        print(commond)
        print(Fore.YELLOW + joke)
        print(Fore.WHITE)
        talk(joke)
# To find location.
    elif "location" in commond:
        print(commond)
        webbrowser.open("https://whatismyipaddress.com/")
# Search in Google.
    elif "search in google" in commond:
        print(commond)
        commond = commond.replace("search in google", "")
        talk("searching"+commond)
        webbrowser.open("https://www.google.co.in/search?q="+commond)
# To open a application.
    elif "open" in commond:
        if "calculator" in commond:
            print(commond)
            talk("opening calculator")
            subprocess.call("calc.exe")
        elif "notepad" in commond:
            print(commond)
            talk("opening notepad")
            subprocess.call("Notepad.exe")
        elif "gmail" in commond:
            print(commond)
            talk("opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "youtube" in commond:
            print(commond)
            talk("opening youtube")
            webbrowser.open("https://www.youtube.com/")
        elif "spotify" or "music" or "song" in commond:
            print(commond)
            talk("opening spotify")
            webbrowser.open("https://open.spotify.com/")
# Send message through what's app
    elif "whatsapp message" in commond:
        if "chaitanya" in commond:
            commond = commond.replace(
                "send whatsapp message to chaitanya", "#")
            hour = int(datetime.datetime.now().strftime("%H"))
            minute = int(datetime.datetime.now().strftime("%M"))+1
            print(Fore.YELLOW + commond)
            print(Fore.WHITE)
            talk("Finall message going to send is "+commond)
            pywhatkit.sendwhatmsg("+919315490815", commond, hour, minute)
        else:
            talk("To whom you want to send message")
# To search in wikipedia.
    elif "who" or "what" in commond:
        search = wikipedia.summary(commond, 1)
        print(commond)
        print(Fore.YELLOW + search)
        print(Fore.WHITE)
        talk(search)
# To find Temperature.
    elif "temperature" in commond:
        pywhatkit.search("Temperature")
        print(commond)

while True:
    run_jarvis("play_yt", "time", "birthday_chaitanya", "today_date")