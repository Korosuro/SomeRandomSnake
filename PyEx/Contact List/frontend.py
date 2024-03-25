from tkinter import *
import tkinter as tk
import mysql.connector
conn = mysql.connector.connect(host="localhost", password="+C,+E}>{kk}$dO36", user="root")
import backend

root = Tk()
root.title("Kontaktliste")            
#root.config(bg="blue")                
root.minsize(200, 200)             
root.geometry("700x500")

exit = tk.Button(root, text="Exit the app", command = root.destroy).grid(row=0, column=0)
#exit.pack()

vornamepre = Label(root, text="Vorname: ")
vornamepre.grid(column=0, row=1)
vorname = Entry(root)
vorname.grid(column=1, row=1)

nachnamepre = Label(root, text="Nachname bitte: ")
nachnamepre.grid(column=0, row=2)
nachname = Entry(root)
nachname.grid(column=1, row=2)

telnumpre = Label(root, text="Telefonnummer bitte: ")
telnumpre.grid(column=0, row=3)
telnum = Entry(root)
telnum.grid(column=1, row=3)

mailpre = Label(root, text="E-Mail-Adresse bitte: ")
mailpre.grid(column=0, row=4)
mail = Entry(root)
mail.grid(column=1, row=4)

adresspre = Label(root, text="Wohnort bitte: ")
adresspre.grid(column=0, row=5)
adress = Entry(root)
adress.grid(column=1, row=5)

def submit_data():
    vorname_value = vorname.get()
    nachname_value = nachname.get()
    telnum_value = telnum.get()
    mail_value = mail.get()
    adress_value = adress.get()

    backend.data_input(vorname_value, nachname_value, telnum_value, mail_value, adress_value)

submit_button = Button(root, text="Bestätigen", command=submit_data)     
submit_button.grid(column=0, row=6)

root.mainloop()