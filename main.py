from tkinter import *
from tkinter.messagebox import showinfo
import speech_recognition as sr
from translate import Translator
import os
from tkinter.messagebox import *
from tkinter.filedialog import *


# notepad using tkinter
root = Tk()
root.title("Notepad")
root.geometry("600x400")

eng_text = StringVar()

r = sr.Recognizer()


def SpeechToText():
    # Speech to Text
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        text_area.insert(END, text)
    except:
        pass


def EnglistToHindi():
    # English To Hindi
    global eng_text
    eng_text = text_area.get("1.0", END)
    translator = Translator(to_lang="Hindi")
    new_text = translator.translate(text_area.get("1.0", END))
    text_area.delete("1.0", END)
    text_area.insert(END, new_text)


def HindiToEnglish():
    # Hindi To English
    global eng_text
    text_area.delete("1.0", END)
    text_area.insert(END, eng_text)


def DarkTheme():
    # Dark Theme
    root.configure(background="#2d2d2d")
    text_area.configure(background="#2d2d2d", foreground="#ffffff")


def LightTheme():
    # Light Theme
    root.configure(background="#ffffff")
    text_area.configure(background="#ffffff", foreground="#000000")


def showAbout():
    showinfo("Notepad", "Developed by: Gautam Anand")


def openFile():

    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])

    if file == "":
        # no file to open
        __file = None
    else:
        # Try to open the file
        # set the window title
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        file = open(file, "r")
        text_area.insert(1.0, file.read())
        file.close()


dialog_frame = Frame(root,  bg="#e6e6e6", bd=5)
# dialog_frame.pack(side=BOTTOM, fill=X)
dialog_frame.place(x=0, y=0, width=600, height=50)

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=openFile)
file.add_command(label='Save', command=None)
file.add_command(label='Speech to Text', command=SpeechToText)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)


# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Translate', menu=edit)
edit.add_command(label='To Hindi', command=EnglistToHindi)
edit.add_command(label='To English', command=HindiToEnglish)


# Adding Edit Menu and commands
theme = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Theme', menu=theme)
theme.add_command(label='Dark', command=DarkTheme)
theme.add_command(label='Light', command=LightTheme)


# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Dev', command=showAbout)

# display Menu
root.config(menu=menubar)


text = StringVar()


header = Label(root, text="NOTEPAD  ", font=(
    "Arial", 14), bg='black', fg='white')
header.pack(fill=X, side=TOP)

text_area = Text(root, font=("Sans", 15), bg='white', fg='black')
text_area.pack(fill="both", expand=1)  # fill=BOTH, expand=1

root.mainloop()
