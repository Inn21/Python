from Database import WorkerDatabase,Worker
import random
import tkinter as tk
from UI import Interface

names = ["Petro","Andriy","Ostap","Victor","Taras"]
departments = ["Software","Management","Cybersecurity","Analytics"]

def Start():
    Window = tk.Tk()
    app = Interface(Window)
    Window.mainloop()  
Start()