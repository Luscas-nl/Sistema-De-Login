import random
from tkinter import *
import os
import time

win = Tk()

class Funcoes():
    def Quit(self):
        self.win2.destroy()       
    def Register(self):
        self.emInfo = self.enEmailCd.get()
        self.seInfo = self.enSenhaCd.get()
        
        self.file = open(self.emInfo+".txt", "w")
        self.file.write(self.emInfo+"\n")
        self.file.write(self.seInfo)
        self.file.close()
        
        self.mens = Label(self.frame03, text= "Usuario cadastrado", font=("arial", 8), bg= "#202020", fg= "#09E376")
        self.mens.place(relx= 0.15, rely= 0.1, relwidth= 0.7, relheight= 0.075)
        
        self.enEmailCd.delete(0, END)
        self.enSenhaCd.delete(0, END)        
    def DontRegistry(self):
        self.lbMes = Label(self.frame01, text= "Usuario/Senha não cadastrado", background= "#202020", fg="#FF0000") 
        self.lbMes.place(relx= 0.29, rely= 0.23, relwidth= 0.42, relheight= 0.02)
    def Login(self):
        self.vfEm = self.enEmail.get()+".txt"
        self.vfSe = self.enSenha.get()
        self.enEmail.delete(0, END)
        self.enSenha.delete(0, END)
             
        self.listaArq = os.listdir()
        if self.vfEm in self.listaArq:
            self.file1 = open(self.vfEm, "r")
            self.verify = self.file1.read().splitlines()
            if self.vfSe in self.verify:
                self.LogConfig()
            else:
                self.DontRegistry()
                
        else:
            self.DontRegistry()
    def BgAle(self):
        self.i = random.randint(0, 2)
        
        self.img = PhotoImage()
        if self.i == 0:
            self.img.config(file= "images/ifal/img1.png")
        if self.i == 1:
            self.img.config(file= "images/ifal/img2.png")
        if self.i == 2:
            self.img.config(file= "images/ifal/img3.png")

class Application(Funcoes):
    def __init__(self):
        self.win = win
        self.AppConfig()
        self.Colors()
        self.Images()
        self.Frames()
        self.BgAle()
        self.Widgets()
        self.win.mainloop()
    def LogConfig(self):
        self.win3 = Tk()
        self.win3.title("Instituto Federal de Alagoas")
        self.win3.geometry("400x400")
        self.win3.iconbitmap("images/logo_if.ico")
        self.win3.resizable(False, False)
        self.frame04 = Frame(self.win3, background= "#202020")
        self.frame04.place(relx=0, rely= 0, relwidth= 1, relheight= 1)
        
        self.lbLog = Label(self.frame04, text= "Login Efetuado")
        self.lbLog.place(relx= 0.15, rely= 0.42, relwidth= 0.7, relheight= 0.075)
        self.win3.mainloop()        
    
    def Images(self):
        self.fundo = PhotoImage(file="images/fundo_if.png")
    
    def CadastroConfig(self):
        self.win2 = Tk()
        self.win2.title("Cadastro")
        self.win2.geometry("400x400")
        self.win2.iconbitmap("images/logo_if.ico")
        self.win2.resizable(False, False)
        
        self.frame03 = Frame(self.win2, bg= "#202020")
        self.frame03.place(relx= 0, rely=0, relwidth= 1, relheight= 1)
        
        self.lbMsgCd = Label(self.frame03, background= "#202020", text= f"Cadastro {' '*24}", fg= "White", font= ("arial", 18, "bold"))
        self.lbMsgCd.place(relx= 0.15, rely= 0.2, relwidth= 0.7, relheight= 0.1)
        
        self.lbEmailCd = Label(self.frame03, background= self.cl1, text= f"E-mail {' '*81}", font= ("arial black", 7), fg= "white")
        self.lbEmailCd.place(relx= 0.15, rely= 0.315, relwidth= 0.7, relheight= 0.025)
        self.enEmailCd = Entry(self.frame03, bd= 0, background= self.cl1, font=("arial", 12), fg="white")
        self.enEmailCd.place(relx= 0.15, rely= 0.34, relwidth= 0.7, relheight= 0.09)
        
        self.lbSenhaCd = Label(self.frame03, background= self.cl1, text= f"Senha {' '*81}", font= ("arial black", 7), fg= "white")
        self.lbSenhaCd.place(relx= 0.15, rely= 0.465, relwidth= 0.7, relheight= 0.025)
        self.enSenhaCd = Entry(self.frame03, bd= 0, background= self.cl1, font=("arial", 12), fg="white")
        self.enSenhaCd.place(relx= 0.15, rely= 0.49, relwidth= 0.7, relheight= 0.09)
        
        self.btnCadCd = Button(self.frame03, background= "white", bd= 0, text= "Cadastrar", relief= FLAT, fg= "#202020",
                             font= ("arial", 15, "bold"), command= self.Register)
        self.btnCadCd.place(relx= 0.15, rely= 0.61, relwidth= 0.34, relheight= 0.12)
        
        self.btnSair = Button(self.frame03, background= "#FF0000", bd= 0, text= "Sair", relief= FLAT, fg= "white",
                             font= ("arial", 15, "bold"), command= self.Quit)
        self.btnSair.place(relx= 0.51, rely= 0.61, relwidth= 0.34, relheight= 0.12)
        self.line2 = Label(self.frame03, bg="#09E376")
        self.line2.place(relx=0, rely=0, relwidth= 0.02, relheight= 1)
        
        self.win2.mainloop()  
    def AppConfig(self):
        self.win.title("Instituto Federal de Alagoas")
        self.win.geometry("900x500")
        self.win.iconbitmap("images/logo_if.ico")
        self.win.resizable(False, False)   
    def Colors(self):
        self.cl1 = "#3E3E3E"   
    def Frames(self):
        
        self.frame01 = Frame(self.win, bg= "#202020")
        self.frame01.place(relx= 0.55, rely=0, relwidth= 0.45, relheight= 1)
        
        self.frame02 = Frame(self.win, bg= "#09E376")
        self.frame02.place(relx= 0, rely=0, relwidth= 0.55, relheight= 1)        
    def Widgets(self):
        
        self.bg = Label(self.frame01, image= self.fundo)
        self.bg.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.lbMsg = Label(self.frame01, background= "#202020", text= f"Login", fg= "White", font= ("arial", 18, "bold"))
        self.lbMsg.place(relx= 0.15, rely= 0.27, relwidth= 0.16, relheight= 0.06)
        
        self.lbEmail = Label(self.frame01, background= self.cl1, text= f"E-mail {' '*81}", font= ("arial black", 7), fg= "white")
        self.lbEmail.place(relx= 0.15, rely= 0.345, relwidth= 0.7, relheight= 0.025)
        self.enEmail = Entry(self.frame01, bd= 0, background= self.cl1, font=("arial", 12), fg="white")
        self.enEmail.place(relx= 0.15, rely= 0.37, relwidth= 0.7, relheight= 0.075)
        
        self.lbSenha = Label(self.frame01, background= self.cl1, text= f"Senha {' '*81}", font= ("arial black", 7), fg= "white")
        self.lbSenha.place(relx= 0.15, rely= 0.485, relwidth= 0.7, relheight= 0.025)
        self.enSenha = Entry(self.frame01, bd= 0, background= self.cl1, font=("arial", 12), fg= "white", show= "*")
        self.enSenha.place(relx= 0.15, rely= 0.51, relwidth= 0.7, relheight= 0.075)
        
        self.btnLog = Button(self.frame01, background= "#09E376", bd= 0, text= "Entrar", relief= FLAT, fg= "white",
                             font= ("arial", 15, "bold"), command= self.Login)
        self.btnLog.place(relx= 0.15, rely= 0.62, relwidth= 0.34, relheight= 0.1)
        
        self.btnCad = Button(self.frame01, background= "white", bd= 0, text= "Cadastrar", relief= FLAT, fg= "#202020",
                             font= ("arial", 15, "bold"), command= self.CadastroConfig)
        self.btnCad.place(relx= 0.51, rely= 0.62, relwidth= 0.34, relheight= 0.1)
        
        self.btnEsq = Button(self.frame01, background= "#202020", bd= 0, text= "Esqueci minha senha", relief= FLAT, fg= "#2FB2FF",
                             activebackground= "#202020", activeforeground= "white")
        self.btnEsq.place(relx= 0.35, rely= 0.75, relwidth= 0.28, relheight= 0.025)
        
        # FRAME 02 #
        self.imagens = Label(self.frame02, image= self.img)
        self.imagens.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        self.line = Label(self.frame02, background= "#09E376")
        self.line.place(relx=0.97, rely= 0, relwidth= 0.03, relheight= 1)
Application()