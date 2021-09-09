import pip
from tkinter import *
from playsound import playsound
import pyttsx3 as pt
import speech_recognition as sr
from gtts import gTTS
import os
from time import sleep
import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
#code for text to speech c
# # importing required module
# create tkinter window
root = Tk()

# styling the frame which helps to
# make our background stylish
frame1 = Frame(root,
			bg = "Black",
			height = "150")

# plcae the widget in gui window
frame1.pack(fill = X)

frame2 = Frame(root,
			bg = "Black",
			height = "750")
frame2.pack(fill=X)

# styling the label which show the text
# in our tkinter window
label = Label(frame1, text = "   Translator ",
			font = "bold, 30",
			bg = "lightblue")

label.place(x = 190, y = 80)

# entry is used to enter the text
entry = Entry(frame2, width = 50,
			bd = 4, font = 14)

entry.place(x = 130, y = 52)
entry.insert(0,"")
 # combobox language choosen
n = tk.StringVar()
monthchoosen = ttk.Combobox(frame2, width = 27, textvariable = n)
monthchoosen['values'] = ('af', 
                          'en',
                          'fr')
  
monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
monthchoosen.place(x=430,y=49)

# get text and convert into audio
def play():    
    language="en"
    myobj = gTTS(text = entry.get(),
                lang =language, 
                slow = False)
    myobj.save("hello.mp3")
    os.system("start hello.mp3") 
    
btn = Button(frame2, text = "TextToAudio",
			width = "15", pady = 10,
			font = "bold, 15",
			command = play, bg='yellow')

btn.place(x = 130,
		y = 130)

def file():
    file = open("C:/Users/HP/Desktop/19001601049_SAVITA/MyText.txt", "r").read().replace("\n", " ")
    language = 'en'
    speech = gTTS(text = str(file), lang = language, slow = False)
    speech.save("voice.mp3")
    os.system("start voice.mp3")

btn3 = Button(frame2, text = "Filetospeak",
			width = "15", pady = 10,
			font = "bold, 15",
			command = file, bg='yellow')

btn3.place(x = 250,
		y = 250)    
    
def get():
    import speech_recognition as SRG 
    import time
 
    store = SRG.Recognizer()
    with SRG.Microphone() as s:
     
        print("Speak...")
     
        audio_input = store.record(s, duration=7)
        print("Recording time:",time.strftime("%I:%M:%S"))
   
        try:
            text_output = store.recognize_google(audio_input)
            print("Text converted from audio:\n")
            
            entry.delete(0,"end")
            lines=entry.insert(0,text_output)
            text_file = open("C:/Users/HP/Desktop/19001601049_SAVITA/MyText.txt", "a")
            text_file.write(text_output) 
            text_file.save() 
            text_file.close()   
            print("Finished!!")            
            print("Execution time:",time.strftime("%I:%M:%S"))
        except:
            print("Couldn't process the audio input.") 
            

btn1 = Button(frame2, text = "speechToText",
			width = "15", pady = 10,
			font = "bold, 15",
			command = get, bg='yellow')

btn1.place(x = 380,
		y = 130)

def close_window():
    root.destroy()

button = tk.Button(text = "Click and Quit", command = close_window)
button.pack()
# give a title
root.title("text_to_speech_convertor")

# we can not change the size
# if you want you can change
root.geometry("650x550+350+200")

# start the gui
root.mainloop()
