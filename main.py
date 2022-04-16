from tkinter import *

win = Tk()

class Application():
    def __init__(self):
        self.win = win
        self.AppConfig()
        self.Colors()
        self.Frames()
        self.Widgets()
        self.win.mainloop()

    def AppConfig(self):
        self.win.title("IFAL - Instituto Federal de Alagoas")
        self.win.geometry("900x500")
        self.win.resizable(False, False)
    
    def Colors(self):
        self.cl1 = "#3E3E3E"
    
    def Frames(self):
        self.frame01 = Frame(self.win, bg= "#202020")
        self.frame01.place(relx= 0.55, rely=0, relwidth= 0.45, relheight= 1)
        
        self.frame02 = Frame(self.win, bg= "#09E376")
        self.frame02.place(relx= 0, rely=0, relwidth= 0.55, relheight= 1)
        
    def Widgets(self):
        
        self.lbMsg = Label(self.frame01, background= "#202020", text= f"Login {' '*29}", fg= "White", font= ("arial", 18, "bold"))
        self.lbMsg.place(relx= 0.15, rely= 0.27, relwidth= 0.7, relheight= 0.1)
        
        self.lbEmail = Label(self.frame01, background= self.cl1, text= f"E-mail {' '*81}", font= ("arial black", 7), fg= "white")
        self.lbEmail.place(relx= 0.15, rely= 0.375, relwidth= 0.7, relheight= 0.025)
        self.enEmail = Entry(self.frame01, bd= 0, background= self.cl1, font=("arial", 12), fg="white")
        self.enEmail.place(relx= 0.15, rely= 0.4, relwidth= 0.7, relheight= 0.075)
        
        self.lbEmail = Label(self.frame01, background= self.cl1, text= f"Senha {' '*81}", font= ("arial black", 7), fg= "white")
        self.lbEmail.place(relx= 0.15, rely= 0.515, relwidth= 0.7, relheight= 0.025)
        self.enEmail = Entry(self.frame01, bd= 0, background= self.cl1, font=("arial", 12), fg="white")
        self.enEmail.place(relx= 0.15, rely= 0.54, relwidth= 0.7, relheight= 0.075)
        
        self.btnLog = Button(self.frame01, background= "#09E376", bd= 0, text= "Entrar", relief= FLAT, fg= "white",
                             font= ("arial", 15, "bold"))
        self.btnLog.place(relx= 0.15, rely= 0.66, relwidth= 0.34, relheight= 0.1)
        
        self.btnCad = Button(self.frame01, background= "white", bd= 0, text= "Cadastrar", relief= FLAT, fg= "#202020",
                             font= ("arial", 15, "bold"))
        self.btnCad.place(relx= 0.51, rely= 0.66, relwidth= 0.34, relheight= 0.1)
Application()