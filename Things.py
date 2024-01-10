import tkinter as tk

class SimpleApp:
    def __init__(self, master):
        self.master = master
        master.title("Meine erste Desktop-App")

        self.label = tk.Label(master, text="Hallo, das ist eine Desktop-App!")
        self.label.pack()

        self.quit_button = tk.Button(master, text="Beenden", command=master.quit)
        self.quit_button.pack()

# Hauptprogramm
root = tk.Tk()
app = SimpleApp(root)
root.mainloop()
app.geometry("400x300")


    
