import pip
from tkinter import *
from playsound import playsound
import pyttsx3 as pt
import speech_recognition as sr
import gtts
import os
from time import sleep
import tkinter as tk
from tkinter import ttk
from translate import Translator
from tkinter import *
from langdetect import detect
from PIL import ImageTk, Image  
import mysql.connector as connector
#from googletrans import Translator, LANGUAGES
#code for text to speech c
# # importing required module
# create tkinter window

root = Tk()

# make our background stylish
frame1 = Frame(root,
			bg="black",
			height = "400")

# plcae the widget in gui window
frame1.pack(fill = X)
bg = PhotoImage(file = "C:\\Users\HP\\Downloads\\b.png")
CB1P_Image_Pack = tk.Label(frame1, image = bg, height=320, width=1000).grid()

frame2 = Frame(root,
			bg = "Black",
			height = "500")
frame2.pack(fill=X)

# styling the label which show the text
# in our tkinter window
label = Label(frame1, text = "Translator ",
			font = "bold, 30",
			bg = "lightblue")

label.place(x = 280, y =20)


# entry is used to enter the text

 # combobox language choosen
n = tk.StringVar()
label = ttk.Label(text="Please select a Language:")
label.pack(fill='x', padx=5, pady=5)
label.place(x = 170, y =200)
chooselan = ttk.Combobox(frame1, width = 27, textvariable = n)
chooselan['values'] = ('af', 
                          'en','fr','hi','es','zh-TW','pt','pa','kn','ne','mr','bn','ta','ur','sa','ml','or')
  
chooselan.grid(column = 1, row = 5)
chooselan.current()
chooselan.place(x=150,y=250)

# get text and convert into audio
language = chooselan.get()


n1 = tk.StringVar()
label = ttk.Label(text="Please select a Language :")
label.pack(fill='x', padx=5, pady=5)
label.place(x = 370, y =200)
chooselan1 = ttk.Combobox(frame1, width = 27, textvariable = n1)
chooselan1['values'] = ('af', 
                          'en','fr','hi','es','zh-TW','pt','pa','kn','ne','mr','bn','ta','ur','sa','ml','or')
  
chooselan1.grid(column = 1, row = 5)
chooselan1.current()
chooselan1.place(x=360,y=250)
var=StringVar()
var1=StringVar()
entry1 = Entry(frame2, width = 50,textvariable=var,
			bd = 4, font = 14)

entry1.place(x =150, y =00)
entry1.insert(0,"")


entry2 = Entry(frame2, width = 50,textvariable=var1,
			bd = 4, font = 14)

entry2.place(x = 150, y =50)
entry2.insert(0,"")
def translate():
    translator= Translator(from_lang=chooselan.get(),to_lang=chooselan1.get())
    translation = translator.translate(var.get())
    var1.set(translation)
btn4 = Button(frame2, text = "Translate",
			width = "15", pady = 10,
			font = "bold, 15",
			command = translate, bg='yellow')

btn4.place(x = 430,
		y = 90)    

    
def play():    
    language = chooselan.get()
    tts = gtts.gTTS(text = entry1.get(),
                lang =language, 
                slow = False)
    tts.save("hello.mp3")
    os.system("start hello.mp3")     
btn = Button(frame2, text = "TextToAudio",
			width = "15", pady = 10,
			font = "bold, 15",
			command = play, bg='yellow')

btn.place(x = 150,
		y = 90)

def file():
    file = open("C:/Users/HP/Desktop/MyText.txt", "r").read().replace("\n", " ")
    language = chooselan.get()
    speech = gtts.gTTS(text = str(file), lang = language, slow = False)
    speech.save("voice.mp3")
    os.system("start voice.mp3")

btn3 = Button(frame2, text = "Filetospeak",
			width = "15", pady = 10,
			font = "bold, 15",
			command = file, bg='yellow')

btn3.place(x = 430,
		y = 160)   


# translator
    
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
            entry1.delete(0,"end")
            lines=entry1.insert(0,text_output)
            text_file = open("C:/Users/HP/Desktop/MyText.txt", "a")
            text_file.write(" "+text_output) 
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

btn1.place(x = 150,
		y = 160)

from tkinter import filedialog
import pytesseract 
from tkinter import filedialog
from PIL import Image
import PIL.Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def imgToText():
    path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
    text = pytesseract.image_to_string(PIL.Image.open(path))
    text=entry1.insert(0,text)
    print(text)
    
btn3 = Button(frame2, text = "imgtToTxt",
			width = "15", pady = 10,
			font = "bold, 15",
			command = imgToText, bg='yellow')

btn3.place(x =150,
		y = 230)    
 
 
 #############################################################################################################################################################
import mysql.connector 
import mysql
from mysql.connector import errorcode 
c = (mysql.connector.connect(host='127.0.0.1',username='root',password='savi@maan',
                      database='pythontest',
                      auth_plugin='mysql_native_password'))
print(c)
import tkinter as tk
import mysql.connector
from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
def loginid():
    def clear():
        userentry.delete(0,END)
        passentry.delete(0,END)
    def close():
        win.destroy()	
    def login():
        if user_name.get()=="" or password.get()=="":
            messagebox.showerror("Error","Enter User Name And Password",parent=win)
        else:
            try:
                con = pymysql.connect(host="127.0.0.1",user="root",password="savi@maan",database="pythontest")
                cur = con.cursor()
                cur.execute("select * from student where username=%s and password = %s",(user_name.get(),password.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)
                else:
                    messagebox.showinfo("Success" , "Successfully Login" , parent = win)
                    close()
                    deshboard()
                con.close()
            except Exception as es:
                messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)

#---------------------------------------------------------------End Login Function ---------------------------------

#---------------------------------------------------- DeshBoard Panel -----------------------------------------
    def deshboard():
        def book():
            if docter_var.get() =="" or day.get() =="" or month.get() == "" or year.get() == "":
                messagebox.showerror("Error" , "All Fields Are Required" , parent = des)
            else:
                con = pymysql.connect(host="127.0.0.1",user="root",password="savi@maan",database="pythontest")
                cur = con.cursor()
                cur.execute("update student set docter ='" + docter_var.get() + "', day ='" +  day.get() + "', month = '" + month.get() + "', year = '" + year.get() + "' where username ='"+ user_name.get() +"'")
                con.commit()
                con.close()
                messagebox.showinfo("Success" , "register successfully " , parent = des)
        des = Tk()
        des.title("Admin Panel detail App")
        des.maxsize(width=800 ,  height=500)
        des.minsize(width=800 ,  height=500)		
		#heading label
        heading = Label(des , text = f"User Name : {user_name.get()}" , font = 'Verdana 20 bold',bg='red')
        heading.place(x=220 , y=50)
        f=Frame(des,height=1,width=800,bg="green")
        f.place(x=0,y=95)
        con = pymysql.connect(host="127.0.0.1",user="root",password="savi@maan",database="pythontest")
        cur = con.cursor()
        cur.execute("select * from student where username ='"+ user_name.get() + "'")
        row = cur.fetchall()
        a=Frame(des,height=1,width=400,bg="green")
        a.place(x=0,y=195)
        b=Frame(des,height=100,width=1,bg="green")
        b.place(x=400,y=97)
        for data in row:
            first_name = Label(des, text= f"First Name : {data[1]}" , font='Verdana 10 bold')
            first_name.place(x=20,y=100)
            last_name = Label(des, text= f"Last Name : {data[2]}" , font='Verdana 10 bold')
            last_name.place(x=20,y=130)
            age = Label(des, text= f"Age : {data[3]}" , font='Verdana 10 bold')
            age.place(x=20,y=160)
            gender = Label(des, text= f"ID : {data[0]}" , font='Verdana 10 bold')
            gender.place(x=250,y=100)
            city = Label(des, text= f"City : {data[5]}" , font='Verdana 10 bold')
            city.place(x=250,y=130)
            add = Label(des, text= f"Address : {data[6]}" , font='Verdana 10 bold')
            add.place(x=250,y=160)
        #button
        con = pymysql.connect(host="127.0.0.1",user="root",password="savi@maan",database="pythontest")
        cur = con.cursor()
        cur.execute("select * from student where username ='"+ user_name.get() + "'")
        rows = cur.fetchall()
        # book Appoitment Details
        heading = Label(des , text = f"{user_name.get()} " , font = 'Verdana 15 bold')
        heading.place(x=20 , y=250)
        for book in rows:
            d1 = Label(des, text= f"Docter: {book[9]}" , font='Verdana 10 bold')
            d1.place(x=20,y=300)
            d2 = Label(des, text= f"Day: {book[10]}" , font='Verdana 10 bold')
            d2.place(x=20,y=320)
            d3 = Label(des, text= f"Month: {book[11]}" , font='Verdana 10 bold')
            d3.place(x=20,y=340)
            d4 = Label(des, text= f"Year: {book[12]}" , font='Verdana 10 bold')
            d4.place(x=20,y=360)		




					
#-----------------------------------------------------End Deshboard Panel -------------------------------------
#----------------------------------------------------------- Signup Window --------------------------------------------------

    def signup():
        # signup database connect 
        def action():
            if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
                messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
            elif password  .get() !=very_pass.get():
                messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
            else:
                try:
                    con = pymysql.connect(host="127.0.0.1",user="root",password="savi@maan",database="pythontest")
                    cur = con.cursor()
                    cur.execute("select * from student where username=%s",user_name.get())
                    row = cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                    else:
                        cur.execute("insert into student(first_name,last_name,age,gender,city,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
						(
						first_name.get(),
						last_name.get(),
						age.get(),
						var.get(),
						city.get(),
						add.get(),
						user_name.get(),
						password.get()
						))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
                        clear()
                        switch()
                except Exception as es:
                    messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)
        def switch():
            winsignup.destroy()
        def clear():
            first_name.delete(0,END)
            last_name.delete(0,END)
            age.delete(0,END)
            var.set("Male")
            city.delete(0,END)
            add.delete(0,END)
            user_name.delete(0,END)
            password.delete(0,END)
            very_pass.delete(0,END)
# start Signup Window	
        winsignup = Tk()
        winsignup.title("User's Details")
        winsignup.maxsize(width=500 ,  height=600)
        winsignup.minsize(width=500 ,  height=600)
#heading label
        heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold')
        heading.place(x=80 , y=60)
# form data label
        first_name = Label(winsignup, text= "First Name :" , font='Verdana 10 bold')
        first_name.place(x=80,y=130)
        
        last_name = Label(winsignup, text= "Last Name :" , font='Verdana 10 bold')
        last_name.place(x=80,y=160)
        
        age = Label(winsignup, text= "Age :" , font='Verdana 10 bold')
        age.place(x=80,y=190)
        
        Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold')
        Gender.place(x=80,y=220)
        
        city = Label(winsignup, text= "City :" , font='Verdana 10 bold')
        city.place(x=80,y=260)
        
        add = Label(winsignup, text= "Address :" , font='Verdana 10 bold')
        add.place(x=80,y=290)
        
        user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
        user_name.place(x=80,y=320)
        
        password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
        password.place(x=80,y=350)
        
        very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
        very_pass.place(x=80,y=380)

	# Entry Box ------------------------------------------------------------------
        first_name = StringVar()
        last_name = StringVar()
        age = IntVar(winsignup, value='0')
        var= StringVar()
        city= StringVar()
        add = StringVar()
        user_name = StringVar()
        password = StringVar()
        very_pass = StringVar()
        first_name = Entry(winsignup, width=40 , textvariable = first_name)
        first_name.place(x=200 , y=133)
        last_name = Entry(winsignup, width=40 , textvariable = last_name)
        last_name.place(x=200 , y=163)
        age = Entry(winsignup, width=40, textvariable=age)
        age.place(x=200 , y=193)
        
        Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
        Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 238)
        
        city = Entry(winsignup, width=40,textvariable = city)
        city.place(x=200 , y=263)
        
        add = Entry(winsignup, width=40 , textvariable = add)
        add.place(x=200 , y=293)
        
        user_name = Entry(winsignup, width=40,textvariable = user_name)
        user_name.place(x=200 , y=323)
        
        password = Entry(winsignup, width=40, textvariable = password)
        password.place(x=200 , y=353)
        
        very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
        very_pass.place(x=200 , y=383)
        # button login and clear
        btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
        btn_signup.place(x=200, y=413)
        btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
        btn_login.place(x=280, y=413)
        sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
        sign_up_btn.place(x=350 , y =20)
        winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------	


	

#------------------------------------------------------------ Login Window -----------------------------------------

    win = Tk()
    # app title
    win.title("your data is here , plese review")
    # window size
    win.maxsize(width=500 ,  height=500)
    win.minsize(width=500 ,  height=500)
    #heading label
    heading = Label(win , text = "Login" , font = 'Verdana 25 bold')
    heading.place(x=80 , y=150)

    username = Label(win, text= "User Name :" , font='Verdana 10 bold')
    username.place(x=80,y=220)

    userpass = Label(win, text= "Password :" , font='Verdana 10 bold')
    userpass.place(x=80,y=260)
    # Entry Box
    user_name = StringVar()
    password = StringVar()
    
    userentry = Entry(win, width=40 , textvariable = user_name)
    userentry.focus()
    userentry.place(x=200 , y=223)
    
    passentry = Entry(win, width=40, show="*" ,textvariable = password)
    passentry.place(x=200 , y=260)
# button login and clear
    btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login)
    btn_login.place(x=200, y=293)
    btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
    btn_login.place(x=260, y=293)
# signup button
    sign_up_btn = Button(win , text="Switch To Sign up" , command = signup )
    sign_up_btn.place(x=350 , y =20)
    win.mainloop()       
########################################################################################################################################################           
btn_login = Button(frame1, text = "login",
			width = "15", pady = 10,
			font = "bold, 15",
			command = loginid, bg='yellow')

btn_login.place(x = 280,
		y = 130)           
        
 ###################################
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Feedback:

    def __init__(self, mainframe):
        mainframe.title('Add Your Comment')
        mainframe.resizable(False, False)
        mainframe.configure(background='#f7f7f7')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f7f7f7')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#f7f7f7', font=('Arial', 12))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        self.header_frame = ttk.Frame(mainframe)
        self.header_frame.pack()

        ttk.Label(self.header_frame, text='Comment App', style='Header.TLabel').grid(row=0, column=1)
        ttk.Label(self.header_frame, wraplength=300,
                  text=(
                      'Add your name, email, and comment, then click submit to add your comment.  Click clear if you make a mistake.')).grid(
            row=1, column=1)

        self.content_in_frame = ttk.Frame(mainframe)
        self.content_in_frame.pack()

        ttk.Label(self.content_in_frame, text='Name:').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.content_in_frame, text='Email:').grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.content_in_frame, text='Comments:').grid(row=2, column=0, padx=5, sticky='sw')

        self.comment_name = ttk.Entry(self.content_in_frame, width=24, font=('Arial', 10))
        self.comment_email = ttk.Entry(self.content_in_frame, width=24, font=('Arial', 10))
        self.comments = Text(self.content_in_frame, width=50, height=10, font=('Arial', 10))

        self.comment_name.grid(row=1, column=0, padx=5)
        self.comment_email.grid(row=1, column=1, padx=5)
        self.comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.content_in_frame, text='Submit',
                   command=self.submit).grid(row=4, column=0, padx=5, pady=5, sticky='e')
        ttk.Button(self.content_in_frame, text='Clear',
                   command=self.clear).grid(row=4, column=1, padx=5, pady=5, sticky='w')

    def submit(self):
        print(f'Name: {self.comment_name.get()}')
        print(f'Email: {self.comment_email.get()}')
        print(f'Comments: {self.comments.get(1.0, "end")}')
        self.clear()
        messagebox.showinfo(title='Comment info', message='Thanks for your comment!')

    def clear(self):
        self.comment_name.delete(0, 'end')
        self.comment_email.delete(0, 'end')
        self.comments.delete(1.0, 'end')

def main():
    root = Tk()
    root.geometry('500x400')
    feedback = Feedback(root)
    root.mainloop()
button_fd = tk.Button(frame2,width = "15", pady = 10,
			font = "bold, 15",text = "feedback", command = main,bg='yellow')
button_fd.pack
button_fd.place(x=430,y=230)
 ###########################################           
def close_window():
    
    root.destroy()

button = tk.Button(text = "Click and Quit", command = close_window)
button.pack()

# give a title
root.title("text_to_speech_convertor")

# we can not change the size
# if you want you can change
root.geometry("700x800+350+200")

# start the gui
root.mainloop()
