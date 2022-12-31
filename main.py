from tkinter import *
from tkinter import ttk
from googletrans import Translator
from googletrans import LANGUAGES
from PIL import ImageTk, Image
r = Tk()
r.geometry('800x500')
r.title("Translator")
swap_img = ImageTk.PhotoImage(Image.open("swap.png"))
logo = ImageTk.PhotoImage(Image.open("Google_Translate_logo.svg.png"))
r.iconphoto(False,logo)
r.config(bg="black")
#            Head Label
headlbl = Label(r,text="Language Translator",bg="black",fg="white",font=("Constantia",20,"bold"))
headlbl.place(relx=0.5,rely=0.1,anchor=CENTER)
#            Notify Label
notiflbl = Label(r,text="Enter Text",bg="black",fg="white",relief=FLAT)
notiflbl.place(relx=0.25,rely=0.2,anchor=CENTER)
#            Text Box Input
textbox = Text(r,bg="black",fg="white",height=10,width=20,padx=10,pady=1,bd=1)
textbox.place(relx=0.25,rely=0.5,anchor=CENTER)

languageslist = list(LANGUAGES.values())
#            Input Language Dropdown
DDinlang = ttk.Combobox(r,state='readonly',values=languageslist,width=10)
DDinlang.place(relx=0.35,rely=0.2,anchor=CENTER)
DDinlang.set("english")
#            Notify Outpt Label
notifoutlbl = Label(r,text="Output:", bg="black", fg="white")
notifoutlbl.place(relx=0.65,rely=0.2, anchor=CENTER)
#            Output Language Dropdown
DDoutlang = ttk.Combobox(r,state="readonly",values=languageslist,width=10)
DDoutlang.place(relx=0.75,rely=0.2,anchor=CENTER)
#            Text Box Output
textboxout = Text(r,bg="black",fg="white",height=10,width=20,padx=10,pady=1,bd=1,state="normal")
textboxout.place(relx=0.75,rely=0.5,anchor=CENTER)
#            Button Translate
btntrans = Button(r,text="Translate",font=("Tahoma",30),bg="black",fg="white",activebackground="white",activeforeground="black",relief=FLAT,padx=10,pady=1)
btntrans.place(relx=0.5,rely=0.9,anchor=CENTER)
#            sWap Button
def swap():
    inin = DDinlang.get()
    ouou = DDoutlang.get()
    DDinlang.set(ouou)
    DDoutlang.set(inin)
swap = Button(r,image=swap_img,command=swap)
swap.place(relx=0.5,rely=0.2,anchor=CENTER)
r.mainloop()