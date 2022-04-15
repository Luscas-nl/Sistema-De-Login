from tkinter import *

win = Tk()

class Application():
    def __init__(self):
        self.win = win
        self.AppConfig()
        self.win.mainloop()

    def AppConfig(self):
        self.win.title("IFAL - Instituto Federal de Alagoas")
        self.win.geometry("900x600")
        self.win.resizable(False, False)
    
Application()