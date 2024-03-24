from tkinter import *
import tkinter as tk
import mysql.connector
conn = mysql.connector.connect(host="localhost", password="+C,+E}>{kk}$dO36", user="root")

root = Tk()
root.title("Kontaktliste")            
#root.config(bg="blue")                
root.minsize(200, 200)             
root.geometry("700x500")

exit = tk.Button(root, text="Exit the app", command = root.destroy).grid(row=1, column=1)
#exit.pack()







root.mainloop()