from operator import ne
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from turtle import st
import tkinter as tk
import controllers.controller as controller
import models.model as model

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

    #dropdown 


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
        cancel = Button(pop, text="Cancel", command = lambda: choice("cancel"), bg="gray")
        cancel.grid(row=7, column=2)

    def choice(option):
        pop.destroy()
        if option == "cancel":
            pop.destroy()
    #botao na area do user q mostra os bilhetes
    #porque é que no command = dropdown?
    #alterei o dropdown para clicker
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

# Menu temporário para testar as funcionalidades ###########################################
############################################################################################
############################################################################################
############################################################################################
def temp_main_menu():
    print("Indique uma opção\n")
    print("\t1) Registar Utilizador\n")
    print("\t2) Entrar como Utilizador Existente\n")
    print("\t3) Ver Espetáculos\n")
    print("\t4) Sair\n") 
    return int(input("Opção: "))

def temp_login():
    print("Iniciar Sessão\n")
    email = input("\tEmail: ")
    password = input("\tPassword: ")
    return controller.authenticate_user(email,password)

def temp_register():
    print("Registar Sessão\n")
    nome = input("\tNome Completo: ")
    email = input("\tEmail: ")
    password = input("\tPassword: ")
    return controller.registrate_user(nome,email,password)

def temp_user_area(user):
    print(f"Bem-vindo {user.getFullName()} à area de utilizador\n")
    print("As suas reservas:\n")
    #Ver todas as reservas com o ID deste utilizador
    for reservations in controller.model.Reservation_List:
        if(user.getID() == reservations.getUserID()):
            print(f"\t Reserva número {reservations.getID()}\n")
    return int(input("Escreva 1 para encerrar sessão OU 2 para ver espetáculos: "))

def temp_show(user):
    if(user == None): print("Sem sessão iniciada\n")
    else: print(f"Bem-vindo aos espetaculos {user.getFullName()}\n")
    for shows in controller.model.Show_List:
        print(f"Espetáculo {shows.getID()} - {shows.getShowName()}\n")
        print(f"\tData do espetáculo: {shows.getDate()}\n")
        if(shows.getCapacity()): print("\tEste espetáculo tem a lotação máxima\n")
        else: print(f"\tEste espetáculo tem {(shows.getSeatCount()/142) * 100}% da lotação máxima\n") # 142 é o espaço total de cada sala
        print(f"\tDescrição: {shows.getDescription()}\n")
        print(f"\tSala:")
        temp_show_room(shows.getRoom())
        print("\n")
    return int(input("Escreva 1 para voltar ao menu principal: "))

def temp_show_room(room):
    for l in room:
        for c in l:
            if(c == "N0"):
                print("[ ]",end="") 
            elif(c == "N1"):
                print("[ x ]",end="") 
            elif(c == "V0"):
                print("[VIP]",end="")
            elif(c == "V1"):
                print("[ x ]",end="") 
            elif(c == "NA"):
                print(" ",end="")
        print("\n")


def temp_menu():
    controller.start()
    session = None
    menu = 0 
    while(1):
        if(menu == 0): 
            menu = temp_main_menu()
        elif(menu == 1): 
            register = temp_register()
            if(register == 0):
                print("O email já existe!")
                menu = 0
            elif(register == 1):
                print("Registo feito com sucesso! Por favor inicie sessão com o seu email e password")
                menu = 0
        elif(menu == 2):
            login = temp_login()
            if(login == 0):
                print("O utilizador não existe")
                menu = 0
            elif(login == -1):
                print("Password errada")
                menu = 0
            else:
                print(f"Bem-vindo {login.getFullName()}")
                session = login
                menu = 5
        elif(menu == 3):
            if(temp_show(session) == 1):
                menu = 0
        elif(menu == 4):
            #controller.save()
            break
        elif(menu == 5):
            option = temp_user_area(session)
            if(option == 1): 
                session = None
                menu = 0
            elif(option == 2):
                menu = 3 
            

def main():
    temp_menu()