from operator import indexOf
from tkinter import *
import controllers.controller as controller
#Window Settings ------------------------------------------------------------
#Window Size --> Tuple : (x,y) 
LOGIN_SIZE = (350,500) #Login Page
REGISTER_SIZE = (350,500) #Register Page
USER_AREA_SIZE = (700,500) #User Area Page
RESERVATION_INFO_SIZE = (500,200) #Reservation Info Page
CONFIRM_CHANGE_SIZE = (1100,500) #Confirm Seat Change Page
REFUND_RESERVATION_SIZE = (300,50) #Confirm Reservation Refund Page
SHOW_AREA_SIZE = (700,500) #Show Area Page 
SHOW_INFO_SIZE = (900,500) #Show Info Page 
ORDER_SIZE = (500,200) #Order Page
CONFIRM_ORDER_SIZE = (300,50) #Confirm Order Page
#Window Color
BG1="#a3a3a3"
###########################################################################
###########################################################################
###########################################################################
# LOGIN WINDOW ------------------------------------------------------------
def autenticate_user(parent,email,password):
    auth = controller.authenticate_user(email,password)
    if(auth == 0): 
        Label(parent, text="O utilizador não existe",pady=10,fg="red",width=35,anchor=W).grid(column=0,row=4, sticky=W)
    elif(auth == -1):
        Label(parent, text="A palavra passe está incorreta",pady=10,fg="red",width=35,anchor=W).grid(column=0,row=4, sticky=W)
    elif(auth == -2):
        Label(parent, text="Tem que preencher todos os espaços",pady=10,fg="red").grid(column=0,row=4, sticky=W)
    else:
        user_area(parent,auth)

def login_page(parent):
    geometry = controller.calculate_geometry(parent,LOGIN_SIZE)
    parent.destroy()
    root = Tk()
    root.title("Show Time! - Iniciar Sessão")
    root.geometry(geometry)
    root.resizable(False,False)
    Label(root, text="Bem-vindo ao Show Time!", padx=10,pady=10).place(x=10,y=10)
    #Email
    user_email = StringVar()
    Label(root, text="Email", padx=10,pady=10).place(x=10,y=50)
    Entry(root,width=30,borderwidth=2,textvariable=user_email).place(x=100,y=50)
    #Password
    user_password = StringVar()
    Label(root, text="Password", padx=10,pady=10).place(x=10,y=100)
    Entry(root,width=30,borderwidth=2, textvariable=user_password, show="*").place(x=100,y=100)
    #Button
    Button(root,text="Entrar",bg="#b2cadb",width=10,height=2,command=lambda:autenticate_user(root,user_email.get(),user_password.get())).place(x=10,y=150)
    Button(root,text="Registar",bg="#b2cadb",width=10,height=2,command=lambda:register_page(root)).place(x=100,y=150)
    Button(root,text="Voltar",bg="#b2cadb",command=lambda:show_area(root), width=10,height=2).place(x=10,y=300)
    Button(root,text="Entrar como Administrador",bg="#b2cadb",height=2).place(x=100,y=300)
    root.mainloop()
#------------------------------------------------------------------------------------------------------------------------
# REGISTER WINDOW ------------------------------------------------------------
def registrate_user(parent,email,name,password):
    control = controller.registrate_user(name,email,password)
    if(control == 0): 
        Label(parent, text="O email já existe",pady=10,width=35,anchor=W,fg="red").grid(column=0,row=6, sticky=W)
    elif(control == -1):
        Label(parent, text="Tem que preencher todos os espaços",pady=10,fg="red").grid(column=0,row=6, sticky=W)
    else:
        user_area(parent,control)

def register_page(parent): 
    geometry = controller.calculate_geometry(parent,REGISTER_SIZE)
    parent.destroy()
    root = Tk()
    root.title("Show Time! - Registo")
    root.geometry(geometry)
    root.resizable(False,False)
    Label(root, text="Bem-vindo/a ao Show Time!", padx=10,pady=10).grid(column=0,row=0, sticky=W)
    Label(root, text="Crie a sua conta!", padx=5,pady=6).grid(column=0,row=1, sticky=W)
    #Full Name
    regist_name = StringVar()
    Label(root, text="Nome Completo", padx=10,pady=10).grid(column=0,row=2, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=regist_name).grid(column=1,row=2)
    #Email
    regist_email = StringVar()
    Label(root, text="E-mail", padx=10,pady=10).grid(column=0,row=3, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=regist_email).grid(column=1,row=3)
    #Password
    regist_password = StringVar()
    Label(root, text="Password", padx=10,pady=10).grid(column=0,row=4, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=regist_password,show="*").grid(column=1,row=4)
    #Button
    Button(root,text="Registo",bg="#b2cadb",width=10,height=2,command=lambda:registrate_user(root,regist_email.get(),regist_name.get(),regist_password.get())).grid(column=0,row=5)
    Button(root,text="Já tenho conta",bg="#b2cadb",width=10,height=2,command=lambda:login_page(root)).grid(column=1,row=5)
    root.mainloop()
#------------------------------------------------------------------------------------------------------------------------
# USER AREA -----------------------------------------
def user_area(parent,session):
    geometry = controller.calculate_geometry(parent,USER_AREA_SIZE)
    parent.destroy()
    root = Tk()
    root.title(f"Show Time! - Área do utilizador - {session.getFullName()}")
    root.geometry(geometry)
    root.resizable(False,False)
    root.config(bg=BG1)
    #texto
    Label(root, text="Escolha o bilhete", font=("Verdana", 16), background="#7eb6de").grid(row=0, column=0, sticky=W)
    #separaçao
    Label(root, text=" ", bg=BG1).grid(row=1, column=0)
    #dropdown 
    #Get reservation 
    SHOW = list()
    for reservations in controller.model.Reservation_List:
        if(reservations.getUserID() == session.getID()):
            SHOW.append(f"#{reservations.getID()} - {reservations.getShowName()} [{reservations.getSeatNumber()}]")
    options = StringVar(root)
    if(len(SHOW) == 0): 
        options.set("Sem reservas")
        option_menu = OptionMenu(root, options,"Sem reservas")
    else: 
        options.set(SHOW[0]) # default value
        option_menu = OptionMenu(root, options, *SHOW)
    option_menu.grid(row=2,column=0,sticky=W)
    #botao na area do user para redirecionar para a info window
    Button(root, text="Ver Bilhete", command=lambda:reservation_info(root,session,options), width=30, height=3, font=("Arial", 11, "bold"), bg="#3d9adb").grid(column=0, row=3)
    #Informação do utilizador
    #nome do user
    Label(root, text=f"Bem-Vindo, {session.getFullName()}", font=("Arial", 9), justify="right", bg=BG1).place(x=510,y=10)
    #botao logout
    Button(root,text="Encerrar Sessão",width=15,height=2, font=("Arial", 9, "bold"), background="red", command=lambda:show_area(root)).place(x=570,y=30)
    #botao pagina principal
    Button(root, text="Ver Espetáculos", font=("Arial", 9, "bold"), width=15, height=2, bg="#3f6f91", command=lambda:show_area(root,session)).place(x=560,y=450)
    root.mainloop()

#pop up da info dos bilhetes - window
def reservation_info(parent,session,reservation):
    if(reservation.get() != "Sem reservas"):
        info_window = Toplevel(parent) # Criar uma página em cima da página atual
        reservation_id = reservation.get()[1:5]
        curr_reserv = None # Reservation Object
        curr_show = None #Show Object
        for reservations in controller.model.Reservation_List:
            if(reservations.getID() == reservation_id):
                curr_reserv = reservations # get respective reservation object
        for shows in controller.model.Show_List:
            if(shows.getID() == curr_reserv.getShowID()):
                curr_show = shows #get respective show object
        info_window.title(f"Informações - #{curr_reserv.getID()}")
        geometry = controller.calculate_geometry(parent,RESERVATION_INFO_SIZE)
        info_window.geometry(geometry)
        info_window.config(bg=BG1)
        Label(info_window, text=f"Nome do Espetáculo: {curr_reserv.getShowName()}", font=("Arial", 9), bg=BG1).grid(row=0, column=0, sticky=W)
        Label(info_window, text=f"Data do Espetáculo: {curr_show.getDate()}", font=("Arial", 9), bg=BG1).grid(row=1, column=0, sticky=W)
        Label(info_window, text=f"Tipo de bilhete: {curr_reserv.getSeatType()}", font=("Arial", 9), bg=BG1).grid(row=2, column=0, sticky=W)
        Label(info_window, text=f"Lugar: {curr_reserv.getSeatNumber()}", font=("Arial", 9), bg=BG1).grid(row=3, column=0, sticky=W)
        Label(info_window, text=f"Preço do Bilhete: {curr_reserv.getPrice()}€", font=("Arial", 9), bg=BG1).grid(row=4, column=0, sticky=W)
        Label(info_window, text=" ", bg=BG1).grid(row=5, column=0)
        Button(info_window, text="Alterar Lugar", command = lambda: confirm_seat_change(parent,session,info_window,curr_reserv,curr_show,curr_reserv.getSeatNumber()), bg="gray").grid(row=6, column=2)
        Button(info_window, text="Reembolsar", command = lambda: confirm_refund(parent,session,info_window,curr_reserv,curr_show,curr_reserv.getSeatNumber()), bg="gray").grid(row=6, column=3)
        Button(info_window, text="Cancel", command = lambda: choice(info_window,"cancel"), bg="gray").grid(row=6, column=4)

def confirm_refund(parent,session,info_window,reservation,show,seat_number):
    reservation_id = controller.clear_order(reservation,show,seat_number)
    confirm_refund_window = Toplevel(info_window)
    confirm_refund_window.title(f"Lugar Reembolsado - Este lugar já não lhe pertence!")
    geometry = controller.calculate_geometry(parent,REFUND_RESERVATION_SIZE)
    confirm_refund_window.geometry(geometry)
    confirm_refund_window.config(bg=BG1)
    Label(confirm_refund_window, text=f"Bilhete número #{reservation_id} reembolsado!", font=("Arial", 12), bg=BG1).grid(row=0, column=0, sticky=W)
    Button(confirm_refund_window, text="OK!", command = lambda: user_area(parent,session), bg="gray").grid(row=1, column=0)

def confirm_seat_change(parent,session,info_window,reservation,show,seat_number): 
    seat_change_window = Toplevel(info_window)
    seat_change_window.title(f"Alterar Reserva")
    geometry = controller.calculate_geometry(parent,CONFIRM_CHANGE_SIZE)
    seat_change_window.geometry(geometry)
    seat_change_window.config(bg=BG1)
    Label(seat_change_window, text=f"{session.getFullName()}, selecione um novo lugar:", font=("Arial", 12), bg=BG1).grid(row=0, column=0, sticky=W)
    Label(seat_change_window, text=f"O seu lugar: {seat_number}", font=("Arial", 12), bg=BG1).grid(row=1, column=0, sticky=W)
    Label(seat_change_window, text=f"Se deseja manter o seu lugar atual, clique no lugar a verde.", font=("Arial", 12), bg=BG1).grid(row=2, column=0, sticky=W)
    show_room(parent,session,seat_change_window,show,seat_number)
    controller.clear_order(reservation,show,seat_number)

#Opçoes na Window de info de bilhetes
def choice(parent,option):
    if option == "cancel":
        parent.destroy()
#------------------------------------------------------------------------------------------------------------------------
# SHOW AREA -----------------------------------------
def show_area(parent=None,session=None):
    if(parent is not None):
        geometry = controller.calculate_geometry(parent,SHOW_AREA_SIZE)
        parent.destroy()
    else:
        geometry = str(SHOW_AREA_SIZE[0])+"x"+str(SHOW_AREA_SIZE[1])
    root = Tk()
    root.title(f"Show Time! - Ver Espetáculo")
    root.geometry(geometry)
    root.resizable(False,False)
    root.config(bg=BG1)
    #texto
    Label(root, text="Escolha o espetáculo que queira ver", font=("Verdana", 16), background="#7dd1bf").grid(row=0, column=0, sticky=W)
    #separaçao
    Label(root, text=" ", bg=BG1).grid(row=1, column=0)
    #dropdown 
    #Get all shows 
    SHOW = list()
    for shows in controller.model.Show_List:
        SHOW.append(f"#{shows.getID()} - {shows.getShowName()} [{shows.getDate()}]")
    options = StringVar(root)
    if(len(SHOW) == 0): #Caso não exista espetáculos
        options.set("Sem Espetáculos")
        option_menu = OptionMenu(root, options,"Sem Espetáculos")
    else: 
        options.set(SHOW[0]) # default value
        option_menu = OptionMenu(root, options, *SHOW)
    option_menu.grid(row=2,column=0,sticky=W)
    #Botão para redirecionar 
    Button(root, text="Ver Espetáculo", command= lambda:show_info(root,session,options),width=30, height=3, font=("Arial", 11, "bold"), bg="#2a9c83").grid(column=0, row=3,sticky=W)
    #Info do user
    if(session == None):
        Label(root,text="Sem sessão iniciada", font=("Arial", 9), justify="right", bg=BG1).place(x=570,y=430)
        Button(root,text="Iniciar Sessão",width=15,height=2, font=("Arial", 9, "bold"), background="#5cedce", command=lambda:login_page(root)).place(x=580,y=453)
    else:
        Label(root, text=f"Bem-Vindo, {session.getFullName()}", font=("Arial", 9), justify="right", bg=BG1).place(x=510,y=10)
        #botao espaço utilizador
        Button(root,text="Espaço do Utilizador",width=16,height=2, font=("Arial", 9, "bold"), background="#5cedce", command=lambda:user_area(root,session)).place(x=560,y=450)
        #encerrar sessao
        Button(root,text="Encerrar Sessão",width=15,height=2, font=("Arial", 9, "bold"), background="red", command=lambda:show_area(root)).place(x=570,y=30)
    root.mainloop()

#pop up da info de cada espetáculo - window
def show_info(parent,session,show):
    if(show.get() != "Sem Espetáculos"):
        info_window = Toplevel(parent) # Criar uma página em cima da página atual
        show_id = int(show.get()[1:(indexOf(show.get(),"-")-1)])
        curr_show = None #Show Object
        for shows in controller.model.Show_List:
            if(shows.getID() == show_id):
                curr_show = shows #Get respective show object
        info_window.title(f"Informação do Espetáculo - #{curr_show.getID()}")
        geometry = controller.calculate_geometry(parent,SHOW_INFO_SIZE)
        info_window.geometry(geometry)
        info_window.config(bg=BG1)
        Label(info_window, text=f"Nome do Espetáculo: {curr_show.getShowName()}", font=("Arial", 9), bg=BG1).grid(row=0, column=0, sticky=W)
        Label(info_window, text=f"Data do Espetáculo: {curr_show.getDate()}", font=("Arial", 9), bg=BG1).grid(row=1, column=0, sticky=W)
        Label(info_window, text=f"Descrição: {curr_show.getDescription()}", font=("Arial", 9), bg=BG1).grid(row=2, column=0, sticky=W)
        # Tabela de Preços ---
        Label(info_window, text=f"----------------------------------------------", font=("Arial", 9), bg=BG1).grid(row=3, column=0, sticky=W)
        Label(info_window, text=f"Tabela de Preços", font=("Arial", 9), bg=BG1).grid(row=4, column=0, sticky=W)
        Label(info_window, text=f"Preço NORMAL - 4,00€", font=("Arial", 9), bg=BG1).grid(row=5, column=0, sticky=W)
        Label(info_window, text=f"Preço VIP - 12,00€", font=("Arial", 9), bg=BG1).grid(row=6, column=0, sticky=W)
        Label(info_window, text=f"----------------------------------------------", font=("Arial", 9), bg=BG1).grid(row=7, column=0, sticky=W)
        # -------
        Label(info_window, text=" ", bg=BG1).grid(row=8, column=0)
        if(session == None):
            Label(info_window, text="Inicie sessão para reservar bilhetes", font=("Arial", 9), bg=BG1).grid(row=9, column=0, sticky=W)
        else:
            show_room(parent,session,info_window,curr_show)
        Button(info_window, text="Cancel", command = lambda: choice(info_window,"cancel"), bg="gray").grid(row=20, column=0)

def show_room(parent,session,info_window,show,seat_change=None): #Print the room in form of buttons
    room = show.getRoom()
    for l in range(len(room)):
        Label(info_window, text=show.getSeatNumber((l,0))[0], font=("Arial", 9), bg=BG1).grid(row=l+5, column=4)
        for c in range(len(room[l])):
            if(l == 0): # Print seat numbers
                Label(info_window, text=show.getSeatNumber((l,c))[1:], font=("Arial", 9), bg=BG1).grid(row=l+4, column=c+5)
            seat_number = show.getSeatNumber((l,c))
            if(room[l][c] == "N0"):
                Button(info_window,text=" ",padx=16,pady=2,command=lambda seat_number=seat_number:order(parent,session,info_window,seat_number,show)).grid(column=c+5,row=l+5)
            elif(room[l][c] == "N1"):
                if(seat_change is not None and show.getSeatNumber((l,c)) == seat_change): 
                    Button(info_window,text=" ",bg='green',padx=16,pady=2,command=lambda seat_number=seat_number:order(parent,session,info_window,seat_number,show)).grid(column=c+5,row=l+5)
                else:
                    Button(info_window,text=" ",bg='red',padx=16,pady=2,state=DISABLED).grid(column=c+5,row=l+5)                
            elif(room[l][c] == "V0"):
                Button(info_window,text="VIP",padx=10,pady=2,command=lambda seat_number=seat_number:order(parent,session,info_window,seat_number,show)).grid(column=c+5,row=l+5)
            elif(room[l][c] == "V1"):
                if(seat_change is not None and show.getSeatNumber((l,c)) == seat_change): 
                    Button(info_window,text="VIP",bg='green',padx=16,pady=2,command=lambda seat_number=seat_number:order(parent,session,info_window,seat_number,show)).grid(column=c+5,row=l+5)
                else:
                    Button(info_window,text="VIP",bg='red',padx=16,pady=2,state=DISABLED).grid(column=c+5,row=l+5)  
            elif(room[l][c] == "NA"):
                pass

def order(parent,session,info_window,seat_number,show): #Order Confirmation Window
    order_window = Toplevel(info_window)
    order_window.title(f"Confirmar lugar {seat_number} - {show.getShowName()}")
    geometry = controller.calculate_geometry(info_window,ORDER_SIZE)
    order_window.geometry(geometry)
    order_window.config(bg=BG1)
    Label(order_window, text="Por Favor confirme a reserva deste bilhete:", font=("Arial", 12), bg=BG1).grid(row=0, column=0, sticky=W)
    Label(order_window, text=f"Reserva para o espetáculo |{show.getShowName()}| em nome de {session.getFullName()}", font=("Arial", 9), bg=BG1).grid(row=1, column=0, sticky=W)
    Label(order_window, text=f"Data do Espetáculo: {show.getDate()}", font=("Arial", 9), bg=BG1).grid(row=2, column=0, sticky=W)
    Label(order_window, text=f"Lugar: {seat_number}", font=("Arial", 9), bg=BG1).grid(row=3, column=0, sticky=W)
    Label(order_window, text=f"Tipo de Reserva: {show.getSeatType(seat_number)}", font=("Arial", 9), bg=BG1).grid(row=4, column=0, sticky=W)
    Label(order_window, text=f"Preço: {show.getPriceFromSeat(seat_number)}€", font=("Arial", 9), bg=BG1).grid(row=5, column=0, sticky=W)
    Label(order_window, text=" ", bg=BG1).grid(row=6, column=0)
    Button(order_window, text="Reservar", command = lambda:confirm_order(parent,session,order_window,seat_number,show), bg="gray").grid(row=20, column=1)
    Button(order_window, text="Cancelar", command = order_window.destroy, bg="gray").grid(row=20, column=3)

def confirm_order(parent,session,order_window,seat_number,show):
    reservation_id = controller.order_ticket(session,show,seat_number)
    confirm_order_window = Toplevel(order_window)
    confirm_order_window.title(f"Lugar Reservado!")
    geometry = controller.calculate_geometry(order_window,CONFIRM_ORDER_SIZE)
    confirm_order_window.geometry(geometry)
    confirm_order_window.config(bg=BG1)
    Label(confirm_order_window, text=f"Bilhete número #{reservation_id} reservado!", font=("Arial", 12), bg=BG1).grid(row=0, column=0, sticky=W)
    Button(confirm_order_window, text="OK!", command = lambda: user_area(parent,session), bg="gray").grid(row=1, column=0)
#------------------------------------------------------------------------------------------------------------------------
def main():
    controller.start()
    show_area()
    #controller.save()