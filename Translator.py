import pip
from tkinter import *
from playsound import playsound
import pyttsx3 as pt
import speech_recognition as sr
from gtts import gTTS
import os
from time import sleep
#code for text to speech c
def set():
    mytext = input("enter what you want to say")
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("hello.mp3")
    os.system("start hello.mp3") 
#code for speech to text
def get():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("speak anything: ")
        audio=r.listen(source)
        print("Done")
        try:
            text=r.recognize_google(audio)
            text =text.lower()
            print("you said: "+text)
        except:
            print('oh oo ,sorry not recognize')   
val = input("Enter your choice: ")
if val=="speech":
    get()
if val=="text":
    set()  
 