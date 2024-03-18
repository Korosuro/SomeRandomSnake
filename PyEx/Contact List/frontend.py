from tkinter import *

window = Tk()
window.title("Kontaktliste")        #adding a title
window.config(bg="blue")            #changing backgroundd color
window.minsize(200, 200)            #setting a fix minimum-size     without setting max-size, its unlimited
window.geometry("300x300+50+50")    #width x height + x + y
window.mainloop()

