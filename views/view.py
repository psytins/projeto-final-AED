from operator import ne
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from turtle import st
import tkinter as tk
import controllers.controller as controller

background="#a6c8e0"

def login_page(parent=None):
    if(parent is not None):
        parent.destroy()
    root = Tk()
    root.title("Show Time! - Login")
    root.geometry("350x300")
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
    root = Tk()
    root.title("Show Time! - Área do utilizador")
    root.geometry("700x500")
    root.resizable(False,False)
    root.config(bg=background)
    
    #texto
    Label(root, text="Informações", font=("Verdana", 16), background="#7eb6de").grid(row=0, column=0, sticky=W)

    #pop up da info dos bilhetes
    def clicker():
        global pop
        pop = Toplevel(root)
        pop.title("Informações!")
        pop.geometry("400x200")
        pop.config(bg=background)
        
        pop_label1 = Label(pop, text="Nome do Espetáculo:", font=("Arial", 9), bg=background).grid(row=0, column=0, sticky=W)
        pop_label2 = Label(pop, text="Data do Espetáculo:", font=("Arial", 9), bg=background).grid(row=1, column=0, sticky=W)
        pop_label3 = Label(pop, text="Tipo de bilhete:", font=("Arial", 9), bg=background).grid(row=2, column=0, sticky=W)
        pop_label4 = Label(pop, text="Número de Bilhetes:", font=("Arial", 9), bg=background).grid(row=3, column=0, sticky=W)
        pop_label5 = Label(pop, text="Lugar:", font=("Arial", 9), bg=background).grid(row=4, column=0, sticky=W)
        pop_label6 = Label(pop, text="Preço do Bilhete:", font=("Arial", 9), bg=background).grid(row=5, column=0, sticky=W)
        pop_label7 = Label(pop, text=" ", bg=background).grid(row=6, column=0)
        cancel = Button(pop, text="Cancel.", command = lambda: choice("cancel"), bg="gray")
        cancel.grid(row=7, column=2)
        
    def choice(option):
        pop.destroy()
        if option == "cancel":
            pop.destroy()
    #botao na area do user q mostra os bilhetes
    Button(root, text="Bilhetes", command=clicker, width=30, height=3, font=("Arial", 11, "bold"), bg="#3d9adb").grid(column=0, row=3)
    
    #separacoes linhas
    Label(root, text=" ", bg=background).grid(row=8, column=0)
    Label(root, text=" ", bg=background).grid(row=9, column=0)
    
    #separacoes colunas !!!!!!!!POR FAVOR ARRANJAR OUTRA FORMA DE FAZER A SEPARACAO COM COLUNAS !!!!!!!!!!!
    Label(root, text="                                                               ", bg=background).grid(row=0, column=3)
    Label(root, text="                                                               ", bg=background).grid(row=1, column=3)
    Label(root, text="                                                               ", bg=background).grid(row=2, column=3)
    Label(root, text="                                                               ", bg=background).grid(row=3, column=3)
    Label(root, text="                                                               ", bg=background).grid(row=4, column=3)
    Label(root, text="                                                                                              ", bg=background).grid(row=5, column=3)
    #nome do user
    Label(root, text="User:", font=("Arial", 9), justify="right", bg=background).grid(row=4, column=9, sticky=NE)
    #imagem teatro
    #my_img = ImageTk.PhotoImage(Image.open("./data/espetaculos.jpg"))
    #my_label = Label(root, image=my_img, height=250, width=350).grid(row=5, column=0)
    #botao logout
    Button(root,text="Log Out",width=10,height=2, font=("Arial", 9, "bold"), background="red", command=root.quit).grid(column=20,row=5)
    #separacoes das linhas
    Label(root, text=" ", bg=background).grid(row=6, column=0)
    Label(root, text=" ", bg=background).grid(row=7, column=0)
    Label(root, text=" ", bg=background).grid(row=8, column=0)
    Label(root, text=" ", bg=background).grid(row=9, column=0)
    Label(root, text=" ", bg=background).grid(row=10, column=0)
    Label(root, text=" ", bg=background).grid(row=11, column=0)
    Label(root, text=" ", bg=background).grid(row=12, column=0)
    Label(root, text=" ", bg=background).grid(row=13, column=0)
    Label(root, text=" ", bg=background).grid(row=14, column=0)
    Label(root, text=" ", bg=background).grid(row=15, column=0)
    Label(root, text=" ", bg=background).grid(row=16, column=0)
    
    #botao pagina principal
    Button(root, text="Página Principal", width=12, height=2, bg="#50616e", command=root.quit).grid(row=14, column=20)
    root.mainloop()
def main():
    #login_page()
    user_area()