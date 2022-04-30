import random
import os
import smtplib
import email.message
import sqlite3
from tkinter import *


win = Tk()
class Funcoes():  
    # === ALTERAÇÃO DE SENHA === #
    def CriarEmail(self):
            # CRIAR EMAIL #
        self.corpoEmail = f"""
        <p>Ola, Aluno!
        <p>Ouvimos que você perdeu sua senha de acesso ao nosso sistema. Desculpe por isso!</p>
        <p>Mas não se preocupe! Você pode utilizar um codigo para alterar sua senha:<br>
        Seu codigo para alteração de senha é: <b>{self.codigo}</p>
        <p>Caso não tenha sido você, ignore esta mensagem</p>
        <p>Atenciosamente,<br>
        Equipe do IFAL Maceio</p>
        """
        self.msg = email.message.Message()
        self.msg["Subject"] = "[IFAL] Alteração de Senha"
        self.msg["From"] = "ifalcampimaceio@gmail.com"
        self.msg["To"] = self.emailCod
        self.senha = "if.campi"
        self.msg.add_header("Content-Type", "text/html")
        self.msg.set_payload(self.corpoEmail)
        
            # ENVIAR EMAIL #
        self.s = smtplib.SMTP("smtp.gmail.com: 587")
        self.s.starttls()
        self.s.login(self.msg["From"], self.senha)
        self.s.sendmail(self.msg["From"], self.msg["To"], self.msg.as_string().encode("utf-8"))   
    def EnviarCodigo(self):
        self.emailCod = self.enEmailCod.get()
        self.codigo = random.randint(100000, 1000000)
        
        self.listaCod = os.listdir()
        if self.emailCod + ".txt" in self.listaCod:
            self.CriarEmail()
            self.win5.destroy()
            self.win5 = None
            self.VerificCodConfig()
        else:
            self.mens = Label(self.frame06, text= "Usuario Não Encontrado", font=("arial", 8), bg= "#202020", fg= "#FF0000")
            self.mens.place(relx= 0.15, rely= 0.2, relwidth= 0.7, relheight= 0.075)
            self.enEmailCod.delete(0, END)            
    def VerificarCodigo(self):
        self.verifyCod = self.enEmailCod1.get() + self.enEmailCod2.get() + self.enEmailCod3.get() + self.enEmailCod4.get() + self.enEmailCod5.get() + self.enEmailCod6.get()
        self.verifyCodInt = int(self.verifyCod)
        if self.verifyCodInt == self.codigo:
            self.win6.destroy()
            self.win6 = None
            self.MudConfig()
        else:
            self.mens = Label(self.frame07, text= "Codigo Invalido", font=("arial", 8), bg= "#202020", fg= "#FF0000")
            self.mens.place(relx= 0.02, rely= 0.2, relwidth= 0.96, relheight= 0.075)
            self.enEmailCod1.delete(0, END)
            self.enEmailCod2.delete(0, END)
            self.enEmailCod3.delete(0, END)
            self.enEmailCod4.delete(0, END)
            self.enEmailCod5.delete(0, END)
            self.enEmailCod6.delete(0, END)                
    def Alterar(self):
        self.vfaEm = self.enEmailMd.get()
        self.vfaSe = self.enSenhaMd.get()
        self.enEmailMd.delete(0, END)
        self.enSenhaMd.delete(0, END)
        
        self.listaArqa = os.listdir()
        if self.vfaEm == self.vfaSe:
            os.remove(self.emailCod+".txt")
            print("Alterado")
            
            self.file = open(self.emailCod+".txt", "w") 
            self.file.write(self.emailCod+"\n")
            self.file.write(self.vfaSe)
            self.file.close()
        
            self.lbMes = Label(self.frame01, text= "Senha Aterada", background= "#202020", fg="#09E376") 
            self.lbMes.place(relx= 0.29, rely= 0.23, relwidth= 0.42, relheight= 0.02)
            self.win4.destroy()
            self.win4 = None
            self.win.lift()
        
        else:
            self.mens = Label(self.frame05, text= "As senhas não coincidem", font=("arial", 8), bg= "#202020", fg= "#FF0000")
            self.mens.place(relx= 0.15, rely= 0.1, relwidth= 0.7, relheight= 0.075)
    
    # === REGISTRO E LOGIN === #    
    def Register(self):
        self.emInfo = self.enEmailCd.get()
        self.seInfo = self.enSenhaCd.get()
        
        self.list = os.listdir()
        if ("@gmail.com" in self.emInfo or "@outlook.com" in self.emInfo or "@hotmail.com" in self.emInfo) and (self.emInfo+".txt" not in self.list):
            self.file = open(self.emInfo+".txt", "w")
            self.file.write(self.emInfo+"\n")
            self.file.write(self.seInfo)
            self.file.close()
            
            self.lbMes = Label(self.frame01, text= "Usuario Cadastrado", background= "#202020", fg="#09E376") 
            self.lbMes.place(relx= 0.29, rely= 0.23, relwidth= 0.42, relheight= 0.02)
            self.win2.destroy()
            self.win2 = None
            self.win.lift()
        elif self.emInfo + ".txt" in self.list:
            self.mens = Label(self.frame03, text= "Usuario Já Cadastrado", font=("arial", 8), bg= "#202020", fg= "#FF0000")
            self.mens.place(relx= 0.15, rely= 0.1, relwidth= 0.7, relheight= 0.075)
            self.enEmailCd.delete(0, END)
            self.enSenhaCd.delete(0, END) 
        else:
            self.mens = Label(self.frame03, text= "E-mail Inválido", font=("arial", 8), bg= "#202020", fg= "#FF0000")
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
    
    # === ALEATORIOS === #
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
        self.win6 = None
        self.win5 = None
        self.win4 = None
        self.win3 = None
        self.win2 = None
        self.win = win
        self.AppConfig()
        self.Frames()
        self.BgAle()
        self.Widgets()
        self.win.mainloop()
    def AppConfig(self):
        self.win.title("Instituto Federal de Alagoas")
        self.win.geometry("900x500")
        self.win.iconbitmap("images/logo_if.ico")
        self.win.resizable(False, False)           
    def CadastroConfig(self):
        if self.win2 is None:
            self.win2 = Tk()
            self.win2.title("Cadastro")
            self.win2.geometry("400x400")
            self.win2.iconbitmap("images/logo_if.ico")
            self.win2.resizable(False, False)
            
            self.frame03 = Frame(self.win2, bg= "#202020")
            self.frame03.place(relx= 0, rely=0, relwidth= 1, relheight= 1)
            
            def Quit():
                self.win2.destroy()     
                self.win2 = None
            
            self.lbMsgCd = Label(self.frame03, background= "#202020", text= f"Cadastro {' '*24}", fg= "White", font= ("arial", 18, "bold"))
            self.lbMsgCd.place(relx= 0.15, rely= 0.2, relwidth= 0.7, relheight= 0.1)
            
            self.lbEmailCd = Label(self.frame03, background= "#3E3E3E", text= f"E-mail {' '*81}", font= ("arial black", 7), fg= "white")
            self.lbEmailCd.place(relx= 0.15, rely= 0.315, relwidth= 0.7, relheight= 0.025)
            self.enEmailCd = Entry(self.frame03, bd= 0, background= "#3E3E3E", font=("arial", 12), fg="white")
            self.enEmailCd.place(relx= 0.15, rely= 0.34, relwidth= 0.7, relheight= 0.09)
            
            self.lbSenhaCd = Label(self.frame03, background= "#3E3E3E", text= f"Senha {' '*81}", font= ("arial black", 7), fg= "white")
            self.lbSenhaCd.place(relx= 0.15, rely= 0.465, relwidth= 0.7, relheight= 0.025)
            self.enSenhaCd = Entry(self.frame03, bd= 0, background= "#3E3E3E", font=("arial", 12), fg="white")
            self.enSenhaCd.place(relx= 0.15, rely= 0.49, relwidth= 0.7, relheight= 0.09)
            
            self.btnCadCd = Button(self.frame03, background= "white", bd= 0, text= "Cadastrar", relief= FLAT, fg= "#202020",
                                font= ("arial", 15, "bold"), command= self.Register)
            self.btnCadCd.place(relx= 0.15, rely= 0.61, relwidth= 0.34, relheight= 0.12)
            
            self.btnSair = Button(self.frame03, background= "#FF0000", bd= 0, text= "Sair", relief= FLAT, fg= "white",
                                font= ("arial", 15, "bold"), command= Quit)
            self.btnSair.place(relx= 0.51, rely= 0.61, relwidth= 0.34, relheight= 0.12)
            self.line2 = Label(self.frame03, bg="#09E376")
            self.line2.place(relx=0, rely=0, relwidth= 0.02, relheight= 1)
        
            self.win2.mainloop()     
    
    def VerificCodConfig(self):
        if self.win6 is None:
            self.win6 = Tk()
            self.win6.title("Esqueci Minha Senha")
            self.win6.geometry("400x400")
            self.win6.iconbitmap("images/logo_if.ico")
            self.win6.resizable(False, False)
            
            def Quit():
                self.win6.destroy()     
                self.win6 = None
                
            self.frame07 = Frame(self.win6, bg= "#202020")
            self.frame07.place(relx= 0, rely=0, relwidth= 1, relheight= 1)
            
            self.lbMes = Label(self.frame07, text= f"Codigo enviado para o email {self.emailCod[0:6]}{'*'*(len(self.emailCod)-5)}", background= "#202020", fg="white") 
            self.lbMes.place(relx= 0, rely= 0.20, relwidth= 1, relheight= 0.045)
            
            self.lbMsgCod = Label(self.frame07, background= "#202020", text= f"Verificar Codigo{' '*13}", fg= "White", font= ("arial", 18, "bold"))
            self.lbMsgCod.place(relx= 0.15, rely= 0.3, relwidth= 0.7, relheight= 0.1)
            
            self.enEmailCod1 = Entry(self.frame07, bd= 0, background= "#3E3E3E", font=("arial", 15), fg="white", justify= CENTER)
            self.enEmailCod1.place(relx= 0.15, rely= 0.41, relwidth= 0.1, relheight= 0.115)
            self.enEmailCod2 = Entry(self.frame07, bd= 0, background= "#3E3E3E", font=("arial", 15), fg="white", justify= CENTER)
            self.enEmailCod2.place(relx= 0.269, rely= 0.41, relwidth= 0.1, relheight= 0.115)
            self.enEmailCod3 = Entry(self.frame07, bd= 0, background= "#3E3E3E", font=("arial", 15), fg="white", justify= CENTER)
            self.enEmailCod3.place(relx= 0.39, rely= 0.41, relwidth= 0.1, relheight= 0.115)
            self.enEmailCod4 = Entry(self.frame07, bd= 0, background= "#3E3E3E", font=("arial", 15), fg="white", justify= CENTER)
            self.enEmailCod4.place(relx= 0.51, rely= 0.41, relwidth= 0.1, relheight= 0.115)
            self.enEmailCod5 = Entry(self.frame07, bd= 0, background= "#3E3E3E", font=("arial", 15), fg="white", justify= CENTER)
            self.enEmailCod5.place(relx= 0.629, rely= 0.41, relwidth= 0.1, relheight= 0.115)
            self.enEmailCod6 = Entry(self.frame07, bd= 0, background= "#3E3E3E", font=("arial", 15), fg="white", justify= CENTER)
            self.enEmailCod6.place(relx= 0.75, rely= 0.41, relwidth= 0.1, relheight= 0.115)
            
            
            self.btnVerific = Button(self.frame07, background= "white", bd= 0, text= "Verificar", relief= FLAT, fg= "#202020",
                                font= ("arial", 15, "bold"), command= self.VerificarCodigo)
            self.btnVerific.place(relx= 0.15, rely= 0.55, relwidth= 0.34, relheight= 0.12)
            
            self.btnSairMd = Button(self.frame07, background= "#FF0000", bd= 0, text= "Cancelar", relief= FLAT, fg= "white",
                                font= ("arial", 15, "bold"), command= Quit )
            self.btnSairMd.place(relx= 0.51, rely= 0.55, relwidth= 0.34, relheight= 0.12)
            self.line2 = Label(self.frame07, bg="#09E376")
            self.line2.place(relx=0, rely=0, relwidth= 0.02, relheight= 1)
    
    def VerificEmailConfig(self):
        if self.win5 is None:
            self.win5 = Tk()
            self.win5.title("Esqueci Minha Senha")
            self.win5.geometry("400x400")
            self.win5.iconbitmap("images/logo_if.ico")
            self.win5.resizable(False, False)
            
            def Quit():
                self.win5.destroy()     
                self.win5 = None
                
            self.frame06 = Frame(self.win5, bg= "#202020")
            self.frame06.place(relx= 0, rely=0, relwidth= 1, relheight= 1)
            
            self.lbMsgCod = Label(self.frame06, background= "#202020", text= f"Alterar Senha {' '*16}", fg= "White", font= ("arial", 18, "bold"))
            self.lbMsgCod.place(relx= 0.15, rely= 0.3, relwidth= 0.7, relheight= 0.1)
            
            self.lbEmailCod = Label(self.frame06, background= "#3E3E3E", text= f"E-mail {' '*81}", font= ("arial black", 7), fg= "white")
            self.lbEmailCod.place(relx= 0.15, rely= 0.415, relwidth= 0.7, relheight= 0.025)
            self.enEmailCod = Entry(self.frame06, bd= 0, background= "#3E3E3E", font=("arial", 12), fg="white")
            self.enEmailCod.place(relx= 0.15, rely= 0.44, relwidth= 0.7, relheight= 0.09)
            
            self.btnEnviarCod = Button(self.frame06, background= "white", bd= 0, text= "Alterar", relief= FLAT, fg= "#202020",
                                font= ("arial", 15, "bold"), command= self.EnviarCodigo)
            self.btnEnviarCod.place(relx= 0.15, rely= 0.55, relwidth= 0.34, relheight= 0.12)
            
            self.btnSairMd = Button(self.frame06, background= "#FF0000", bd= 0, text= "Cancelar", relief= FLAT, fg= "white",
                                font= ("arial", 15, "bold"), command= Quit )
            self.btnSairMd.place(relx= 0.51, rely= 0.55, relwidth= 0.34, relheight= 0.12)
            self.line2 = Label(self.frame06, bg="#09E376")
            self.line2.place(relx=0, rely=0, relwidth= 0.02, relheight= 1)
                
    
    def MudConfig(self):
        if self.win4 is None:
            self.win4 = Tk()
            self.win4.title("Esqueci Minha Senha")
            self.win4.geometry("400x400")
            self.win4.iconbitmap("images/logo_if.ico")
            self.win4.resizable(False, False)
            
            def Quit():
                self.win4.destroy()     
                self.win4 = None
                
            self.frame05 = Frame(self.win4, bg= "#202020")
            self.frame05.place(relx= 0, rely=0, relwidth= 1, relheight= 1)
            
            self.lbMsgMd = Label(self.frame05, background= "#202020", text= f"Alterar Senha {' '*16}", fg= "White", font= ("arial", 18, "bold"))
            self.lbMsgMd.place(relx= 0.15, rely= 0.2, relwidth= 0.7, relheight= 0.1)
            
            self.lbEmailMd = Label(self.frame05, background= "#3E3E3E", text= f"Nova Senha {' '*72}", font= ("arial black", 7), fg= "white")
            self.lbEmailMd.place(relx= 0.15, rely= 0.315, relwidth= 0.7, relheight= 0.025)
            self.enEmailMd = Entry(self.frame05, bd= 0, background= "#3E3E3E", font=("arial", 12), fg="white")
            self.enEmailMd.place(relx= 0.15, rely= 0.34, relwidth= 0.7, relheight= 0.09)
            
            self.lbSenhaMd = Label(self.frame05, background= "#3E3E3E", text= f"Verificar Senha {' '*66}", font= ("arial black", 7), fg= "white")
            self.lbSenhaMd.place(relx= 0.15, rely= 0.465, relwidth= 0.7, relheight= 0.025)
            self.enSenhaMd = Entry(self.frame05, bd= 0, background= "#3E3E3E", font=("arial", 12), fg="white")
            self.enSenhaMd.place(relx= 0.15, rely= 0.49, relwidth= 0.7, relheight= 0.09)
            
            self.btnCadMd = Button(self.frame05, background= "white", bd= 0, text= "Alterar", relief= FLAT, fg= "#202020",
                                font= ("arial", 15, "bold"), command= self.Alterar)
            self.btnCadMd.place(relx= 0.15, rely= 0.61, relwidth= 0.34, relheight= 0.12)
            
            self.btnSairMd = Button(self.frame05, background= "#FF0000", bd= 0, text= "Sair", relief= FLAT, fg= "white",
                                font= ("arial", 15, "bold"), command= Quit)
            self.btnSairMd.place(relx= 0.51, rely= 0.61, relwidth= 0.34, relheight= 0.12)
            self.line2 = Label(self.frame05, bg="#09E376")
            self.line2.place(relx=0, rely=0, relwidth= 0.02, relheight= 1)
    def LogConfig(self):

        if self.win3 is None:
            self.win3 = Tk()
            self.win3.title("Instituto Federal de Alagoas")
            self.win3.geometry("400x400")
            self.win3.iconbitmap("images/logo_if.ico")
            self.win3.resizable(False, False)
            self.frame04 = Frame(self.win3, background= "#202020")
            self.frame04.place(relx=0, rely= 0, relwidth= 1, relheight= 1)
            
            self.lbLog = Label(self.frame04, text= "Login Efetuado")
            self.lbLog.place(relx= 0.15, rely= 0.42, relwidth= 0.7, relheight= 0.075)
            self.win.destroy()
            self.win3.lift()
            self.win3.mainloop()   
    def Frames(self):
        
        self.frame01 = Frame(self.win, bg= "#202020")
        self.frame01.place(relx= 0.55, rely=0, relwidth= 0.45, relheight= 1)
        
        self.frame02 = Frame(self.win, bg= "#09E376")
        self.frame02.place(relx= 0, rely=0, relwidth= 0.55, relheight= 1)        
    def Widgets(self):
        
        self.fundo = PhotoImage(master= self.win, file="images/fundo_if.png")
        self.bg = Label(self.frame01, image= self.fundo)
        self.bg.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.lbMsg = Label(self.frame01, background= "#202020", text= f"Login", fg= "White", font= ("arial", 18, "bold"))
        self.lbMsg.place(relx= 0.15, rely= 0.27, relwidth= 0.16, relheight= 0.06)
        
        self.lbEmail = Label(self.frame01, background= "#3E3E3E", text= f"E-mail {' '*81}", font= ("arial black", 7), fg= "white")
        self.lbEmail.place(relx= 0.15, rely= 0.345, relwidth= 0.7, relheight= 0.025)
        self.enEmail = Entry(self.frame01, bd= 0, background= "#3E3E3E", font=("arial", 12), fg="white")
        self.enEmail.place(relx= 0.15, rely= 0.37, relwidth= 0.7, relheight= 0.075)
        
        self.lbSenha = Label(self.frame01, background= "#3E3E3E", text= f"Senha {' '*81}", font= ("arial black", 7), fg= "white")
        self.lbSenha.place(relx= 0.15, rely= 0.485, relwidth= 0.7, relheight= 0.025)
        self.enSenha = Entry(self.frame01, bd= 0, background= "#3E3E3E", font=("arial", 12), fg= "white", show= "*")
        self.enSenha.place(relx= 0.15, rely= 0.51, relwidth= 0.7, relheight= 0.075)
        
        self.btnLog = Button(self.frame01, background= "#09E376", bd= 0, text= "Entrar", relief= FLAT, fg= "white",
                             font= ("arial", 15, "bold"), command= self.Login)
        self.btnLog.place(relx= 0.15, rely= 0.62, relwidth= 0.34, relheight= 0.1)
        
        self.btnCad = Button(self.frame01, background= "white", bd= 0, text= "Cadastrar", relief= FLAT, fg= "#202020",
                             font= ("arial", 15, "bold"), command= self.CadastroConfig)
        self.btnCad.place(relx= 0.51, rely= 0.62, relwidth= 0.34, relheight= 0.1)
        
        self.btnEsq = Button(self.frame01, background= "#202020", bd= 0, text= "Esqueci minha senha", relief= FLAT, fg= "#2FB2FF",
                             activebackground= "#202020", activeforeground= "white", command= self.VerificEmailConfig)
        self.btnEsq.place(relx= 0.35, rely= 0.75, relwidth= 0.28, relheight= 0.025)
        
        # FRAME 02 #
        self.imagens = Label(self.frame02, image= self.img)
        self.imagens.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        self.line = Label(self.frame02, background= "#09E376")
        self.line.place(relx=0.97, rely= 0, relwidth= 0.03, relheight= 1)

Application()