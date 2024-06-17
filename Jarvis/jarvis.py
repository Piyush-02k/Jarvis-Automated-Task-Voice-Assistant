from tkinter import *
from winsound import PlaySound
from pywikihow import RandomHowTo, search_wikihow
import pywhatkit
from PIL import ImageTk,Image #pip install Pillow
#pip install --no-index -f https://dist.plone.org/thirdparty/ -U PIL
from dataclasses import replace
import imp
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
#unofficial download pyaudio
import wikipedia #pip install wikipedia
from bs4 import BeautifulSoup
import webbrowser
import os
import requests
import json
import time
import smtplib
import random
import wmi  # pip install wmi
import json
from PIL import Image

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

i=0

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning, Sir")

    if hour>=12 and hour<16:
        speak("Good Afternoon, Sir")

    if hour>=16 and hour<24:
        speak("Good Evening, Sir")

    speak("Jarvis here, How may i help you!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print(e)
        print("Try Again please...")
        return "None"
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    greeting()
    while True:
        btn1.configure(bg = 'orange')
        query = takecommand().lower()
        if 'wikipedia' in query:
            try:
                speak('Searching in wikipedia')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                speak(results)
            except Exception as e:
                print(e)

        elif 'exit' in query:
            var.set("Bye sir I wish you a cherrful day ahead")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir I wish you  a cherrful day ahead")
            break

        elif 'wish me' in query:
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Good morning, Sir")

            if hour>=12 and hour<16:
                speak("Good Afternoon, Sir")

            if hour>=16 and hour<24:
                speak("Good Evening, Sir")

            speak("Jarvis here, How may i help you!")

        elif 'search' in query:
            var.set('searching....')
            window.update()
            speak("what do you want to search sir..")

            webbrowser.open('https://google.com/search?q=' + ''.com)

        elif 'open Google' in query:
            var.set('Opening Google')
            window.update()
            speak('opening ...Sir')
            webbrowser.open("www.google.com")

        elif 'open amazon' in query:
            var.set('Opening Amazon')
            window.update()
            speak('opening ...Sir')
            webbrowser.open("www.amazon.com")

        elif 'open flipkart' in query:
            var.set('Opening Flipkart')
            window.update()
            speak('opening ...Sir')
            webbrowser.open("www.flipkart.com")

        elif 'open amazon prime' in query:
            var.set('Opening PrimeVideo')
            window.update()
            speak('opening ...Sir')
            webbrowser.open("www.primevideo.com")

        elif 'open netflix' in query:
            webbrowser.open("www.netflix.com")

        elif 'stock updates' in query or 'open money control' in query or 'stock update' in query:
            var.set('Opening Stocks Updates')
            window.update()
            speak('showing results ...Sir')
            webbrowser.open("www.moneycontrol.com/stocksmarketsindia/")

        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'search on youtube' in query:
            query = query.replace("search on youtube ","")
            query = query.replace(" ","+")
            path = f"youtube.com/results?search_query={query}"
            print(path)
            webbrowser.open(path)   

        elif 'whats the time' or 'what time is it now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        # elif 'open vs code' in query:
           # var.set('Opening VS code')
           # window.update()
           # codePath = "C:\Users\ppkul\Downloads\VSCodeUserSetup-x64-1.80.1.exe"
           # os.startfile(codePath)
        
        elif 'open instagram' in query:
            var.set('Opening Instagram')
            window.update()
            speak('opening instagram..Sir')
            webbrowser.open("www.instagram.com")

        elif 'facebook' in query:
            var.set('opening Facebook')
            window.update()
            speak('opening facebook .. Sir')
            webbrowser.open('wwww.facebook.com')

        elif 'music' in query or "ganna" in query:
            var.set("Playing music")
            import os

            speak('ok..Sir')
            music_dir = "D:\Hindi Songs"           
            songs = os.listdir(music_dir)
            random_gen = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[random_gen]))
            window.update()

        elif 'roll a dice' in query:
            num = random.randint(0,5)
            num = num + 1
            print("Result :", num)
            speak(f"Sir, its {num}")

        elif 'toss a coin' in query:
            num = random.randint(0,1)
            if num == 0:
                speak(f"Sir, its heads")
            else:
                speak(f"Sir, its tails")
        
        elif 'read news' in query or 'what is todays news' in query or 'what is today news' in query or "today's news" in query or 'today news' in query:          
            url = 'https://www.bbc.com/news'
            response = requests.get(url)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            for x in headlines:
                results.append(x["title"])
                print("titles=", x["title"])
                speak(x["title"])
                results.append(x["description"])
                print("description=", x["description"])
                speak(x["description"])
                print(x.text.strip())
                speak(x.text.strip())
                i = i+1
                if i==5:
                    break

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('FRIDAY')

label = Label(window, width = 500, height = 500)

label.pack()
window.after(0, update, 0)


btn0 = Button(text = 'WISH ME',width = 20, command = greeting, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = PlaySound, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
