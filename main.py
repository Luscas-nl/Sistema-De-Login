from tkinter import *

win = Tk()

class Application():
    def __init__(self):
        self.win = win
        self.AppConfig()
        self.Frames()
        self.win.mainloop()

    def AppConfig(self):
        self.win.title("IFAL - Instituto Federal de Alagoas")
        self.win.geometry("900x550")
        self.win.resizable(False, False)
    
    def Frames(self):
        self.frame01 = Frame(self.win, bg= "#202020")
        self.frame01.place(relx= 0.55, rely=0, relwidth= 0.45, relheight= 1)
        
        self.frame02 = Frame(self.win, bg= "#09E376")
        self.frame02.place(relx= 0, rely=0, relwidth= 0.55, relheight= 1)
Application()