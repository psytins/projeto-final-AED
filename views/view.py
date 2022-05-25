from operator import ne
from tkinter import *
from turtle import st
import controllers.controller as controller
#from PIL import ImageTk,Image

def login_page(parent=None):
    if(parent is not None):
        parent.destroy()
    root = Tk()
    root.title("Show Time! - Login")
    root.geometry("350x350")
    root.resizable(False,False)
    Label(root, text="Welcome to Show Time!", padx=10,pady=10).grid(column=0,row=0, sticky=W)
    #Email
    Label(root, text="Email", padx=10,pady=10).grid(column=0,row=1, sticky=W)
    Entry(root,width=30,borderwidth=2).grid(column=1,row=1)
    #Password
    Label(root, text="Password", padx=10,pady=10).grid(column=0,row=2, sticky=W)
    Entry(root,width=30,borderwidth=2, show="*").grid(column=1,row=2)
    #Button
    Button(root,text="Login",width=10,height=2).grid(column=0,row=3)
    Button(root,text="Register",width=10,height=2,command=lambda:register_page(root)).grid(column=1,row=3)
    root.mainloop()

def register_page(parent): 
    parent.destroy()
    root = Tk()
    root.title("Show Time! - Register")
    root.geometry("350x500")
    root.resizable(False,False)
    Label(root, text="Welcome to Show Time!", padx=10,pady=10).grid(column=0,row=0, sticky=W)
    Label(root, text="Please register", padx=5,pady=6).grid(column=0,row=1, sticky=W)
    #Full Name
    Label(root, text="Full Name", padx=10,pady=10).grid(column=0,row=2, sticky=W)
    Entry(root,width=30,borderwidth=2).grid(column=1,row=2)
    #Email
    Label(root, text="Email", padx=10,pady=10).grid(column=0,row=3, sticky=W)
    Entry(root,width=30,borderwidth=2).grid(column=1,row=3)
    #Password
    Label(root, text="Password", padx=10,pady=10).grid(column=0,row=4, sticky=W)
    Entry(root,width=30,borderwidth=2, show="*").grid(column=1,row=4)
    #Button
    Button(root,text="Register",width=10,height=2).grid(column=0,row=5)
    Button(root,text="Login",width=10,height=2,command=lambda:login_page(root)).grid(column=1,row=5)
    root.mainloop()

def user_area():
    
    #parent.destroy()
    root = Tk()
    root.title("Show Time! - Área do utilizador")
    root.geometry("700x500")
    root.resizable(False,False)
    #texto
    Label(root, text="Os seus Bilhetes", font=("Arial", 14), background="gray").grid(row=0, column=0)
    #separaçao linha
    Label(root, text=" ").grid(row=1, column=0)
    #info dos bilhetes
    Label(root, text="Nome do Espetáculo:", font=("Arial", 9), justify="right").grid(row=2, column=0, sticky=W)
    Label(root, text="Data do Espetáculo:", font=("Arial", 9), justify="right").grid(row=3, column=0, sticky=W)
    Label(root, text="Tipo de bilhete:", font=("Arial", 9), justify="right").grid(row=4, column=0, sticky=W)
    Label(root, text="Número de Bilhetes:", font=("Arial", 9), justify="right").grid(row=5, column=0, sticky=W)
    Label(root, text="Lugar:", font=("Arial", 9), justify="right").grid(row=6, column=0, sticky=W)
    Label(root, text="Preço do Bilhete:", font=("Arial", 9), justify="right").grid(row=7, column=0, sticky=W)
    #separacoes linhas
    Label(root, text=" ").grid(row=8, column=0)
    Label(root, text=" ").grid(row=9, column=0)
    #info dos bilhetes 2
    Label(root, text="Nome do Espetáculo:", font=("Arial", 9), justify="right").grid(row=10, column=0, sticky=W)
    Label(root, text="Data do Espetáculo:", font=("Arial", 9), justify="right").grid(row=11, column=0, sticky=W)
    Label(root, text="Tipo de bilhete:", font=("Arial", 9), justify="right").grid(row=12, column=0, sticky=W)
    Label(root, text="Número de Bilhetes:", font=("Arial", 9), justify="right").grid(row=13, column=0, sticky=W)
    Label(root, text="Lugar:", font=("Arial", 9), justify="right").grid(row=14, column=0, sticky=W)
    Label(root, text="Preço do Bilhete:", font=("Arial", 9), justify="right").grid(row=15, column=0, sticky=W)
    #separacoes colunas
    Label(root, text="            ").grid(row=0, column=1)
    Label(root, text="            ").grid(row=1, column=2)
    Label(root, text="            ").grid(row=2, column=3)
    Label(root, text="            ").grid(row=3, column=4)
    Label(root, text="            ").grid(row=4, column=5)
    Label(root, text="            ").grid(row=5, column=6)
    Label(root, text="            ").grid(row=6, column=7)
    Label(root, text="            ").grid(row=7, column=8)
    Label(root, text="            ").grid(row=8, column=9)
    #nome do user
    Label(root, text="User:", font=("Arial", 9), justify="right").grid(row=8, column=9, sticky=NE)
    #imagem perfil VER COMO FZR
    #ImageTk(root, file="perfil.ppm").grid(row=0, column= 10, sticky=E)
    #perfil = PhotoImage(file="./data/perfil.ppm") // , image=perfil,
    #botao logout
    Button(root,text="Log Out",width=10,height=2, font=("Arial", 9, "bold"), justify="right", background="red").grid(column=20,row=9, sticky=NE)
    root.mainloop()

def main():
    #login_page()
    user_area()
