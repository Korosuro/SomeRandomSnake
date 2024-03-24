from tkinter import *
from tkinter import ttk
import tkinter as tk

window = Tk()
window.title("Kontaktliste")            #adding a title
window.config(bg="blue")                #changing backgroundd color
window.minsize(200, 200)                #setting a fix minimum-size     without setting max-size, its unlimited
window.geometry("700x500")

#creating a label, which can be used to display either text or images
text = Label(window, text="Test-Text")
text.pack()
text2 = Label(window, text="--Wisdom")
text2.pack()

exit = tk.Button(window, text="Exit the app", command = window.destroy)
exit.pack()














window.mainloop()

