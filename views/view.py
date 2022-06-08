from operator import indexOf
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import models.model as model
import controllers.controller as controller

background="#bbbbbb"

def autenticate_user(parent,email,password):
    auth = controller.authenticate_user(email,password)
    if(auth == 0): 
        Label(parent, text="O utilizador não existe", padx=10,pady=10).grid(column=0,row=4, sticky=W)
    elif(auth == -1):
        Label(parent, text="A palavra passe está incorreta", padx=10,pady=10).grid(column=0,row=4, sticky=W)
    else:
        user_area(parent,auth)

def registrate_user(parent,email,name,password):
    control = controller.registrate_user(name,email,password)
    if(control == 0): 
        Label(parent, text="O email já existe", padx=10,pady=10).grid(column=0,row=6, sticky=W)
    else:
        user_area(parent,control)

def login_page(parent):
    parent.destroy()
    root = Tk()
    root.title("Show Time! - Login")
    root.geometry("350x300")
    root.resizable(False,False)
    Label(root, text="Welcome to Show Time!", padx=10,pady=10).grid(column=0,row=0, sticky=W)
    #Email
    user_email = StringVar()
    Label(root, text="Email", padx=10,pady=10).grid(column=0,row=1, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=user_email).grid(column=1,row=1)
    #Password
    user_password = StringVar()
    Label(root, text="Password", padx=10,pady=10).grid(column=0,row=2, sticky=W)
    Entry(root,width=30,borderwidth=2, textvariable=user_password, show="*").grid(column=1,row=2)
    #Button
    Button(root,text="Login",width=10,height=2,command=lambda:autenticate_user(root,user_email.get(),user_password.get())).grid(column=0,row=3)
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
    regist_name = StringVar()
    Label(root, text="Full Name", padx=10,pady=10).grid(column=0,row=2, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=regist_name).grid(column=1,row=2)
    #Email
    regist_email = StringVar()
    Label(root, text="Email", padx=10,pady=10).grid(column=0,row=3, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=regist_email).grid(column=1,row=3)
    #Password
    regist_password = StringVar()
    Label(root, text="Password", padx=10,pady=10).grid(column=0,row=4, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=regist_password,show="*").grid(column=1,row=4)
    #Button
    Button(root,text="Register",width=10,height=2,command=lambda:registrate_user(root,regist_email.get(),regist_name.get(),regist_password.get())).grid(column=0,row=5)
    Button(root,text="Login",width=10,height=2,command=lambda:login_page(root)).grid(column=1,row=5)
    root.mainloop()
# USER AREA -----------------------------------------
def user_area(parent,session):
    parent.destroy()
    root = Tk()
    root.title(f"Show Time! - Área do utilizador - {session.getFullName()}")
    root.geometry("700x500")
    root.resizable(False,False)
    root.config(bg=background)
    #texto
    Label(root, text="Escolha o bilhete", font=("Verdana", 16), background="#7eb6de").grid(row=0, column=0, sticky=W)
    #dropdown 
    #Get shows 
    SHOW = list()
    for reservations in controller.model.Reservation_List:
        if(reservations.getUserID() == session.getID()):
            SHOW.append(f"#{reservations.getID()} - {reservations.getShowName()} [{reservations.getSeatNumber()}]")
    options = StringVar(root)
    if(len(SHOW) == 0): 
        options.set("None")
        option_menu = OptionMenu(root, options,"None")
    else: 
        options.set(SHOW[0]) # default value
        option_menu = OptionMenu(root, options, *SHOW)
    option_menu.grid(row=1,column=0,sticky=W)

    #pop up da info dos bilhetes - window
    def reservation_info():
        if(options.get() != "None"):
            global info_window
            info_window = Toplevel(root) # Criar uma página em cima da página atual
            reservation_id = options.get()[1:5]
            curr_reserv = None # Reservation Object
            curr_show = None #Show Object
            for reservations in controller.model.Reservation_List:
                if(reservations.getID() == reservation_id):
                    curr_reserv = reservations # get respective reservation object
            for shows in controller.model.Show_List:
                if(shows.getID() == curr_reserv.getShowID()):
                    curr_show = shows #get respective show object
            info_window.title(f"Informações - #{curr_reserv.getID()}")
            info_window.geometry("400x200")
            info_window.config(bg=background)
            Label(info_window, text=f"Nome do Espetáculo: {curr_reserv.getShowName()}", font=("Arial", 9), bg=background).grid(row=0, column=0, sticky=W)
            Label(info_window, text=f"Data do Espetáculo: {curr_show.getDate()}", font=("Arial", 9), bg=background).grid(row=1, column=0, sticky=W)
            Label(info_window, text=f"Tipo de bilhete: {curr_reserv.getSeatType()}", font=("Arial", 9), bg=background).grid(row=2, column=0, sticky=W)
            Label(info_window, text=f"Lugar: {curr_reserv.getSeatNumber()}", font=("Arial", 9), bg=background).grid(row=3, column=0, sticky=W)
            Label(info_window, text=f"Preço do Bilhete: {curr_reserv.getPrice()}", font=("Arial", 9), bg=background).grid(row=4, column=0, sticky=W)
            Label(info_window, text=" ", bg=background).grid(row=5, column=0)
            Button(info_window, text="Cancel", command = lambda: choice("cancel"), bg="gray").grid(row=6, column=2)

    #Opçoes na Window de info de bilhetes
    def choice(option):
        if option == "cancel":
            info_window.destroy()
    #botao na area do user para redirecionar para a info window
    Button(root, text="Ver Bilhete", command=reservation_info, width=30, height=3, font=("Arial", 11, "bold"), bg="#3d9adb").grid(column=0, row=2)
    #Informação do utilizador
    #nome do user
    Label(root, text=f"Bem-Vindo: {session.getFullName()}", font=("Arial", 9), justify="right", bg=background).grid(row=4, column=0, sticky=W)
    #imagem teatro
    #my_img = ImageTk.PhotoImage(Image.open("./data/espetaculos.jpg"))
    #my_label = Label(root, image=my_img, height=250, width=350).grid(row=5, column=0)
    #botao logout
    Button(root,text="Encerrar Sessão",width=10,height=2, font=("Arial", 9, "bold"), background="red", command=lambda:show_area(root)).grid(column=0,row=5, sticky=W)
    #botao pagina principal
    Button(root, text="Ver Espetáculos", width=12, height=2, bg="#50616e", command=lambda:show_area(root,session)).grid(row=6, column=0,sticky=W)
    root.mainloop()
# SHOW AREA -----------------
def show_area(parent=None,session=None):
    if(parent is not None):
        parent.destroy()
    root = Tk()
    root.title(f"Show Time! - Ver Espetáculo")
    root.geometry("700x500")
    root.resizable(False,False)
    root.config(bg=background)
    #texto
    Label(root, text="Escolha o espetáculo que queira ver", font=("Verdana", 16), background="#7eb6de").grid(row=0, column=0, sticky=W)
    #dropdown 
    #Get all shows 
    SHOW = list()
    for shows in controller.model.Show_List:
        SHOW.append(f"#{shows.getID()} - {shows.getShowName()} [{shows.getDate()}]")
    options = StringVar(root)
    if(len(SHOW) == 0): #Caso não exista espetáculos
        options.set("None")
        option_menu = OptionMenu(root, options,"None")
    else: 
        options.set(SHOW[0]) # default value
        option_menu = OptionMenu(root, options, *SHOW)
    option_menu.grid(row=1,column=0,sticky=W)

    def confirm_order(seat_number,show):
        reservation_id = controller.order_ticket(session,show,seat_number)
        global confirm_order_window
        confirm_order_window = Toplevel(order_window)
        confirm_order_window.title(f"Lugar Reservado!")
        confirm_order_window.geometry("300x300")
        confirm_order_window.config(bg=background)
        Label(confirm_order_window, text=f"Bilhete número {reservation_id} reservado!", font=("Arial", 12), bg=background).grid(row=0, column=0, sticky=W)
        Button(confirm_order_window, text="OK!", command = lambda: user_area(root,session), bg="gray").grid(row=1, column=0)

    def order(seat_number,show): #Order Confirmation Window
        global order_window
        order_window = Toplevel(info_window)
        order_window.title(f"Confirmar lugar {seat_number} - {show.getShowName()}")
        order_window.geometry("500x300")
        order_window.config(bg=background)
        Label(order_window, text="Por Favor confirme a reserva deste bilhete:", font=("Arial", 12), bg=background).grid(row=0, column=0, sticky=W)
        Label(order_window, text=f"Reserva para o espetáculo |{show.getShowName()}| em nome de {session.getFullName()}", font=("Arial", 9), bg=background).grid(row=1, column=0, sticky=W)
        Label(order_window, text=f"Data do Espetáculo: {show.getDate()}", font=("Arial", 9), bg=background).grid(row=2, column=0, sticky=W)
        Label(order_window, text=f"Lugar: {seat_number}", font=("Arial", 9), bg=background).grid(row=3, column=0, sticky=W)
        Label(order_window, text=f"Tipo de Reserva: {show.getSeatType(seat_number)}", font=("Arial", 9), bg=background).grid(row=4, column=0, sticky=W)
        Label(order_window, text=f"Preço: {show.getPriceFromSeat(seat_number)}€", font=("Arial", 9), bg=background).grid(row=5, column=0, sticky=W)
        Label(order_window, text=" ", bg=background).grid(row=6, column=0)
        Button(order_window, text="Reservar", command = lambda:confirm_order(seat_number,show), bg="gray").grid(row=20, column=1)
        Button(order_window, text="Cancelar", command = order_window.destroy, bg="gray").grid(row=20, column=3)

    def show_room(show): #Print the room in form of buttons
        room = show.getRoom()
        for l in range(len(room)):
            for c in range(len(room[l])):
                seat_number = show.getSeatNumber((l,c))
                if(room[l][c] == "N0"):
                    Button(info_window,text=" ",padx=16,pady=2,command=lambda seat_number=seat_number:order(seat_number,show)).grid(column=c+5,row=l+5)
                elif(room[l][c] == "N1"):
                    Button(info_window,text=" ",bg='red',padx=16,pady=2,state=DISABLED).grid(column=c+5,row=l+5)
                elif(room[l][c] == "V0"):
                    Button(info_window,text="VIP",padx=10,pady=2,command=lambda seat_number=seat_number:order(seat_number,show)).grid(column=c+5,row=l+5)
                elif(room[l][c] == "V1"):
                    Button(info_window,text="VIP",bg='red',padx=10,pady=2,state=DISABLED).grid(column=c+5,row=l+5)
                elif(room[l][c] == "NA"):
                    pass

    #pop up da info de cada espetáculo - window
    def show_info():
        if(options.get() != "None"):
            global info_window
            info_window = Toplevel(root) # Criar uma página em cima da página atual
            show_id = int(options.get()[1:(indexOf(options.get(),"-")-1)])
            curr_show = None #Show Object
            for shows in controller.model.Show_List:
                if(shows.getID() == show_id):
                    curr_show = shows #Get respective show object
            info_window.title(f"Informação do Espetáculo - #{curr_show.getID()}")
            info_window.geometry("900x600")
            info_window.config(bg=background)
            Label(info_window, text=f"Nome do Espetáculo: {curr_show.getShowName()}", font=("Arial", 9), bg=background).grid(row=0, column=0, sticky=W)
            Label(info_window, text=f"Data do Espetáculo: {curr_show.getDate()}", font=("Arial", 9), bg=background).grid(row=1, column=0, sticky=W)
            Label(info_window, text=f"Descrição: {curr_show.getDescription()}", font=("Arial", 9), bg=background).grid(row=2, column=0, sticky=W)
            Label(info_window, text=" ", bg=background).grid(row=3, column=0)
            if(session == None):
                Label(info_window, text=f"Inicie sessão para reservar bilhetes", font=("Arial", 9), bg=background).grid(row=4, column=0, sticky=W)
            else:
                show_room(curr_show)
            Button(info_window, text="Cancel", command = lambda: choice("cancel"), bg="gray").grid(row=20, column=3)
    
    def choice(option):
        if option == "cancel":
            info_window.destroy()
    #Botão para redirecionar 
    Button(root, text="Ver Espetáculo", command=show_info, width=30, height=3, font=("Arial", 11, "bold"), bg="#3d9adb").grid(column=0, row=2)
    #nome do user
    if(session == None):
        Label(root, text="Sem sessão iniciada", font=("Arial", 9), justify="right", bg=background).grid(row=3, column=0, sticky=W)
        Button(root,text="Iniciar Sessão",width=10,height=2, font=("Arial", 9, "bold"), background="red", command=lambda:login_page(root)).grid(column=0,row=5, sticky=W)
    else:
        Label(root, text=f"Bem-Vindo: {session.getFullName()}", font=("Arial", 9), justify="right", bg=background).grid(row=3, column=0, sticky=W)
        Button(root,text="Espaço do Utilizador",width=10,height=2, font=("Arial", 9, "bold"), background="red", command=lambda:user_area(root,session)).grid(column=0,row=5, sticky=W)
        Button(root,text="Encerrar Sessão",width=10,height=2, font=("Arial", 9, "bold"), background="red", command=lambda:show_area(root)).grid(column=0,row=6, sticky=W)
    root.mainloop()

def main():
    controller.start()
    show_area()
    #controller.save()