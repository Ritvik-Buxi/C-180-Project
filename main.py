from tkinter import *
from tkinter import ttk
from googletrans import Translator
from PIL import ImageTk, Image
r = Tk()
r.geometry('500x500')
r.title("Translator")
logo = ImageTk.PhotoImage(Image.open("Google_Translate_logo.svg.png"))
r.iconphoto(False,logo)
r.config(bg="black")
headlbl = Label(r,text="Language Translator",bg="black",fg="white",font=("Constantia",20,"bold"))
headlbl.place(relx=0.5,rely=0.1,anchor=CENTER)
notiflbl = Label(r,text="Enter Text",bg="black",fg="white",relief=FLAT)
notiflbl.place(relx=0.25,rely=0.2,anchor=CENTER)
textbox = Text(r,bg="black",fg="white",height=10,width=20,padx=10,pady=1,bd=1)
textbox.place(relx=0.25,rely=0.5,anchor=CENTER)
r.mainloop()
'''Hello :)'''