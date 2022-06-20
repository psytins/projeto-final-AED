import math
from operator import indexOf
from tkinter import *
from tkinter.messagebox import showinfo, showwarning #Pop up message box
from tkcalendar import Calendar #Data picker
from datetime import *
import controllers.controller as controller
#Window Settings ------------------------------------------------------------
#Window Sizes --> Tuple : (x,y) 
LOGIN_SIZE = (350,500) #Login Page
REGISTER_SIZE = (350,500) #Register Page
CREATE_SHOW_SIZE = (400,500) #Register Page
USER_AREA_SIZE = (700,500) #User Area Page
RESERVATION_INFO_SIZE = (500,200) #Reservation Info Page
CONFIRM_CHANGE_SIZE = (1100,500) #Confirm Seat Change Page
SHOW_AREA_SIZE = (700,500) #Show Area Page 
SHOW_INFO_SIZE = (900,500) #Show Info Page 
ORDER_SIZE = (500,200) #Order Page
#Window Colors
BG1 = "#a3a3a3"
BG2="#d1d1d1"
###########################################################################
###########################################################################
###########################################################################
# LOGIN WINDOW ------------------------------------------------------------
def autenticate_user(parent,email,password,admin):
    auth = controller.authenticate_user(email,password,admin)
    if(auth == 0): 
        Label(parent, text="O utilizador não existe",pady=10,fg="red",bg=BG2,width=35,anchor=W).place(x=10,y=200)
    elif(auth == -1):
        Label(parent, text="A palavra passe está incorreta",pady=10,fg="red",bg=BG2,width=35,anchor=W).place(x=10,y=200)
    elif(auth == -2):
        Label(parent, text="É favor preencher todos os campos",pady=10,fg="red",bg=BG2,anchor=W).place(x=10,y=200)
    elif(auth == -3):
        Label(parent, text="Acesso interdito",pady=10,fg="red",bg=BG2,anchor=W,width=35).place(x=10,y=200)
    else:
        user_area(parent,auth)

def login_page(parent):
    geometry = controller.calculate_geometry(parent,LOGIN_SIZE)
    parent.destroy()
    root = Tk()
    root.title("Show Time! - Iniciar Sessão")
    root.geometry(geometry)
    root.resizable(False,False)
    root.config(bg=BG2)
    Label(root,text="Bem-vindo ao Show Time!",bg=BG2,padx=10,pady=10).place(x=10,y=10)
    #Email
    user_email = StringVar()
    Label(root,text="Email",bg=BG2,padx=10,pady=10).place(x=10,y=50)
    Entry(root,width=30,borderwidth=2,textvariable=user_email).place(x=100,y=50)
    #Password
    user_password = StringVar()
    Label(root,text="Password",bg=BG2,padx=10,pady=10).place(x=10,y=100)
    Entry(root,width=30,borderwidth=2,textvariable=user_password,show="*").place(x=100,y=100)
    #Button
    Button(root,text="Entrar",bg="#b2cadb",width=10,height=2,command=lambda:autenticate_user(root,user_email.get(),user_password.get(),False)).place(x=10,y=150)
    Button(root,text="Registar",bg="#b2cadb",width=10,height=2,command=lambda:register_page(root)).place(x=265,y=150)
    Button(root,text="Voltar",bg="#a19c9c",command=lambda:show_area(root), width=10,height=2).place(x=10,y=450)
    Button(root,text="Entrar como Administrador",bg="#fff275",height=2,command=lambda:login_page_admin(root)).place(x=190,y=450)
    root.mainloop()

def login_page_admin(parent):
    geometry = controller.calculate_geometry(parent,LOGIN_SIZE)
    parent.destroy()
    root = Tk()
    root.title("Show Time! - Iniciar Sessão - Administrador")
    root.geometry(geometry)
    root.resizable(False,False)
    root.config(bg=BG2)
    Label(root,text="Bem-vindo Administrador!",bg=BG2,padx=10,pady=10).place(x=10,y=10)
    #Email
    user_email = StringVar()
    Label(root,text="Email",bg=BG2,padx=10,pady=10).place(x=10,y=50)
    Entry(root,width=30,borderwidth=2,textvariable=user_email).place(x=100,y=50)
    #Password
    user_password = StringVar()
    Label(root,text="Password", bg=BG2,padx=10,pady=10).place(x=10,y=100)
    Entry(root,width=30,borderwidth=2, textvariable=user_password, show="*").place(x=100,y=100)
    #Button
    Button(root,text="Entrar",bg="#b2cadb",width=10,height=2,command=lambda:autenticate_user(root,user_email.get(),user_password.get(),True)).place(x=10,y=150)
    Button(root,text="Voltar",bg="#a19c9c",command=lambda:login_page(root), width=10,height=2).place(x=10,y=450)
    root.mainloop()
#------------------------------------------------------------------------------------------------------------------------
# REGISTER WINDOW ------------------------------------------------------------
def registrate_user(parent,email,name,password):
    control = controller.registrate_user(name,email,password)
    if(control == 0): 
        Label(parent, text="O email já existe",pady=10,fg="red",bg=BG2,anchor=W).place(x=10,y=250)
    elif(control == -1):
        Label(parent, text="É favor preencher todos os campos",pady=10,fg="red",bg=BG2,anchor=W).place(x=10,y=250)
    else:
        showinfo("Email registado com sucesso",f"Bem-vindo {name} ao Show Time!\n\nJá pode ter acesso livre à reserva de bilhetes para os seus espetáculos preferidos.")
        user_area(parent,control)

def register_page(parent): 
    geometry = controller.calculate_geometry(parent,REGISTER_SIZE)
    parent.destroy()
    root = Tk()
    root.title("Show Time! - Registo")
    root.geometry(geometry)
    root.resizable(False,False)
    root.config(bg=BG2)
    Label(root, text="Bem-vindo/a ao Show Time!", bg=BG2, padx=10,pady=10).grid(column=0,row=0, sticky=W)
    Label(root, text="Crie a sua conta!", bg=BG2, padx=5,pady=6).grid(column=0,row=1, sticky=W)
    #Full Name
    regist_name = StringVar()
    Label(root, text="Nome Completo", padx=10,pady=10, bg=BG2).grid(column=0,row=2, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=regist_name).grid(column=1,row=2)
    #Email
    regist_email = StringVar()
    Label(root, text="E-mail", bg=BG2, padx=10,pady=10).grid(column=0,row=3, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=regist_email).grid(column=1,row=3)
    #Password
    regist_password = StringVar()
    Label(root, text="Password", bg=BG2, padx=10,pady=10).grid(column=0,row=4, sticky=W)
    Entry(root,width=30,borderwidth=2,textvariable=regist_password,show="*").grid(column=1,row=4)
    #Button
    Button(root,text="Registo",bg="#b2cadb",width=10,height=2,command=lambda:registrate_user(root,regist_email.get(),regist_name.get(),regist_password.get())).grid(column=0,row=5)
    Button(root,text="Já tenho conta",bg="#b2cadb",width=12,height=2,command=lambda:login_page(root)).grid(column=1,row=5)
    root.mainloop()
#------------------------------------------------------------------------------------------------------------------------
# USER AREA -----------------------------------------
def admin_panel(parent,type,info): #type is "d" or "m" or "y"
    if(type=="d"):
        Label(parent, text=f"{controller.get_day_total_price(info)}€",fg="white",bg="#ff8c42",font=("Verdana", 12,"bold"),width=5).place(x=10,y=120)
    elif(type=="m"):
        updated_info = datetime.strptime(info,"%B").strftime("%m") #Pass e.g January to 01
        Label(parent, text=f"{controller.get_month_total_price(updated_info)}€",fg="white",bg="#ff8c42",font=("Verdana", 12,"bold"),width=5).place(x=10,y=215)
    elif(type=="y"):
        updated_info = datetime.strptime(info,"%Y").strftime("%y") #Pass e.g 2022 to 22
        Label(parent, text=f"{controller.get_year_total_price(updated_info)}€",fg="white",bg="#ff8c42",font=("Verdana", 12,"bold"),width=5).place(x=10,y=310)

def user_area(parent,session):
    geometry = controller.calculate_geometry(parent,USER_AREA_SIZE)
    parent.destroy()
    root = Tk()
    root.title(f"Show Time! - Área do utilizador - {session.getFullName()}")
    root.geometry(geometry)
    root.resizable(False,False)
    root.config(bg=BG1)
    if session.isAdmin() == True:
        Label(root, text="Ferramentas de Administrador", font=("Verdana", 16), bg="#fff275").place(x=5,y=5)
        #Admin Panel
        #Get dates - Day
        dates_day_list = list()
        dates_month_list = list()
        dates_year_list = list()
        default_date_day = StringVar()
        default_date_month = StringVar()
        default_date_year = StringVar()
        for shows in controller.model.Show_List:
            if shows.getDate() not in dates_day_list:
                dates_day_list.append(shows.getDate())
            if datetime.strptime(shows.getDate()[3:5],"%m").strftime("%B") not in dates_month_list:
                dates_month_list.append(datetime.strptime(shows.getDate()[3:5],"%m").strftime("%B")) #To show e.g January instead of 01
            if datetime.strptime(shows.getDate()[6:10],"%y").strftime("%Y") not in dates_year_list:
                dates_year_list.append(datetime.strptime(shows.getDate()[6:10],"%y").strftime("%Y")) #To show e.g 2022 instead of 22
        Label(root,bg="#ff8c42",height=21,width=31).place(x=5,y=50)
        Label(root, text="Ver total de vendas",font=("Verdana",12,"bold"),bg="#ff8c42",fg="white").place(x=8,y=60)
        #Sales by Day -----------
        if(len(dates_day_list) != 0): default_date_day.set(dates_day_list[0])       
        else: 
            dates_day_list.append("Sem datas")
            default_date_day.set("Sem datas")    
        Label(root, text="Por Dia",fg="white",bg="#ff8c42",font=("Verdana",9)).place(x=10,y=100)
        Label(root, text="0.00€",fg="white",bg="#ff8c42",font=("Verdana", 12,"bold"),width=5).place(x=10,y=120)
        OptionMenu(root,default_date_day,*dates_day_list).place(x=10,y=145)
        Button(root, text="Atualizar",command=lambda:admin_panel(root,"d",default_date_day.get()),width=7,height=1,bg="#fff275").place(x=150,y=145)
        #--------
        #Sales by Month -----------
        if(len(dates_month_list) != 0): default_date_month.set(dates_month_list[0])
        else: 
            dates_month_list.append("Sem datas")
            default_date_month.set("Sem datas")    
        Label(root, text="Por Mês",fg="white",bg="#ff8c42",font=("Verdana",9)).place(x=10,y=195)
        Label(root, text="0.00€",fg="white",bg="#ff8c42",font=("Verdana", 12,"bold"),width=5).place(x=10,y=215)
        OptionMenu(root,default_date_month,*dates_month_list).place(x=10,y=240)
        Button(root, text="Atualizar",command=lambda:admin_panel(root,"m",default_date_month.get()),width=7,height=1,bg="#fff275").place(x=150,y=240)
        #--------
        #Sales by Year -----------
        if(len(dates_year_list) != 0): default_date_year.set(dates_year_list[0])
        else: 
            dates_year_list.append("Sem datas")
            default_date_year.set("Sem datas")  
        Label(root, text="Por Ano",fg="white",bg="#ff8c42",font=("Verdana",9)).place(x=10,y=290)
        Label(root, text="0.00€",fg="white",bg="#ff8c42",font=("Verdana", 12,"bold"),width=5).place(x=10,y=310)
        OptionMenu(root,default_date_year,*dates_year_list).place(x=10,y=335)
        Button(root,text="Atualizar",command=lambda:admin_panel(root,"y",default_date_year.get()),width=7,height=1,bg="#fff275").place(x=150,y=335)
        #--------
        #User Number -----------
        Label(root,bg="#6c8ead",height=10,width=31).place(x=250,y=50)
        Label(root, text="Utilizadores Registados",font=("Verdana",12,"bold"),bg="#6c8ead",fg="white").place(x=258,y=60)     
        Label(root, text=f"{controller.get_all_users()}",fg="white",bg="#6c8ead",font=("Verdana", 18)).place(x=260,y=90)
        #--------
        #Show Number -----------
        Label(root,bg="#a23e48",height=10,width=31).place(x=250,y=214)
        Label(root, text="Reservas Registadas",font=("Verdana",12,"bold"),bg="#a23e48",fg="white").place(x=258,y=224)   
        Label(root, text=f"{controller.get_all_reservations()}",fg="white",bg="#a23e48",font=("Verdana", 18)).place(x=260,y=254)
        #--------
        #botao para adicionar o espetaculo FAZER A FUNÇAO PARA ADICIONAR OS ESPETACULOS
        Button(root, text="Adicionar Espetáculo", width=30,height=3,command=lambda:create_show_page(root,session),font=("Arial", 11, "bold"), bg="#fff275").place(x=10,y=425)
    else:
        #texto
        Label(root, text="A sua lista de reservas", font=("Verdana", 16), background="#7eb6de").grid(row=0, column=1, sticky=W)
        #separaçao
        Label(root, text=" ", bg=BG1).grid(row=1, column=0)
        Label(root, text=" ", bg=BG1).grid(row=1, column=1)
        #List Box  
        #Create a scrollbar
        scrollbar = Scrollbar(root)
        scrollbar.grid(row=2,column=2)
        #Create List Box
        reservation_list_box = Listbox(root,yscrollcommand=scrollbar.set,width=100,height=20)
        for reservations in controller.model.Reservation_List:
            if(reservations.getUserID() == session.getID()):
                reservation_list_box.insert(END, f"#{reservations.getID()} - {reservations.getShowName()} [{reservations.getSeatNumber()}] - {reservations.getPrice()}€")
        reservation_list_box.grid(row=2,column=1,sticky=W)
        scrollbar.config(command=reservation_list_box.yview) #Join the scrollbar with the listbox
        #separaçao
        Label(root, text=" ", bg=BG1).grid(row=3, column=1)
        Button(root, text="Consultar reserva", command=lambda:list_box_to_reservation(root,session,reservation_list_box), width=30, height=3, font=("Arial", 11, "bold"), bg="#3d9adb").grid(column=1, row=4)
    #Informação do utilizador
    #nome do user
        Label(root, text=f"Total de reservas: {controller.get_user_total_price(session)}€", font=("Arial", 9), justify="right", bg=BG1).place(x=400,y=25)
    Label(root, text=f"Bem-Vindo {session.getFullName()}", font=("Arial", 9), justify="right", bg=BG1).place(x=400,y=5)
    #botao logout
    Button(root,text="Encerrar Sessão",width=15,height=2, font=("Arial", 9, "bold"), background="red", command=lambda:show_area(root)).place(x=570,y=5)
    #botao pagina principal
    Button(root, text="Ver Espetáculos", font=("Arial", 9, "bold"), width=15, height=2, bg="#3f6f91", command=lambda:show_area(root,session)).place(x=570,y=450)
    root.mainloop()

#receives a list box and return the selected reservation
def list_box_to_reservation(root,session,list_box):
    if(list_box.curselection() != ()): #Assuming only one reservation belongs to the tuple
        i = list_box.curselection()[0] #get selected index in list box
        reservation_id = list_box.get(i)[1:5] #Clean the string and get the show ID
        for reservations in controller.model.Reservation_List:
            if(reservations.getID() == reservation_id):
                curr_reserv = reservations #Get respective show object
    else:
        curr_reserv = None #Show Object
    reservation_info(root,session,curr_reserv)

#pop up da info dos bilhetes - window
def reservation_info(parent,session,reservation):
    if(reservation is not None):
        info_window = Toplevel(parent) # Criar uma página em cima da página atual
        curr_show = None #Get Show Object
        for shows in controller.model.Show_List:
            if(shows.getID() == reservation.getShowID()):
                curr_show = shows #get respective show object
        info_window.title(f"Informações - #{reservation.getID()}")
        geometry = controller.calculate_geometry(parent,RESERVATION_INFO_SIZE)
        info_window.geometry(geometry)
        info_window.config(bg=BG1)
        Label(info_window, text=f"Nome do Espetáculo: {reservation.getShowName()}", font=("Arial", 9), bg=BG1).grid(row=0, column=0, sticky=W)
        Label(info_window, text=f"Data do Espetáculo: {curr_show.getDate()}", font=("Arial", 9), bg=BG1).grid(row=1, column=0, sticky=W)
        Label(info_window, text=f"Tipo de bilhete: {reservation.getSeatType()}", font=("Arial", 9), bg=BG1).grid(row=2, column=0, sticky=W)
        Label(info_window, text=f"Lugar: {reservation.getSeatNumber()}", font=("Arial", 9), bg=BG1).grid(row=3, column=0, sticky=W)
        Label(info_window, text=f"Preço do Bilhete: {reservation.getPrice()}€", font=("Arial", 9), bg=BG1).grid(row=4, column=0, sticky=W)
        Label(info_window, text=" ", bg=BG1).grid(row=5, column=0)
        Button(info_window, text="Alterar Lugar", command = lambda: confirm_seat_change(parent,info_window,session,reservation,curr_show,reservation.getSeatNumber()), bg="gray").grid(row=6, column=2)
        Button(info_window, text="Reembolsar", command = lambda: confirm_refund(parent,info_window,session,reservation,curr_show,reservation.getSeatNumber()), bg="gray").grid(row=6, column=3)
        Button(info_window, text="Cancelar", command = lambda: choice(info_window,"cancel"), bg="gray").grid(row=6, column=4)
    else:
        showinfo("Informação","Por favor selecione uma reserva, ou reserve um bilhete na área dos espetáculos.")

def confirm_refund(parent,toplevel_window,session,reservation,show,seat_number):
    reservation_id = controller.clear_order(reservation,show,seat_number)
    showinfo("Lugar Reembolsado",f"Bilhete #{reservation_id} reembolsado!\n\n{session.getFullName()}, o seu bilhete foi reembolsado com sucesso.",parent=toplevel_window)
    user_area(parent,session)

def confirm_seat_change(parent,toplevel_window,session,reservation,show,seat_number): #can be better
    seat_change_window = Toplevel(toplevel_window)
    seat_change_window.title(f"Alterar Reserva")
    geometry = controller.calculate_geometry(parent,CONFIRM_CHANGE_SIZE)
    seat_change_window.geometry(geometry)
    seat_change_window.config(bg=BG1)
    Label(seat_change_window, text=f"{session.getFullName()}, selecione um novo lugar:", font=("Arial", 12), bg=BG1).grid(row=0, column=0, sticky=W)
    Label(seat_change_window, text=f"O seu lugar: {seat_number}", font=("Arial", 12), bg=BG1).grid(row=1, column=0, sticky=W)
    Label(seat_change_window, text=f"Se deseja manter o seu lugar atual, clique no lugar a verde.", font=("Arial", 12), bg=BG1).grid(row=2, column=0, sticky=W)
    show_room(parent,session,seat_change_window,show,seat_number)
    controller.clear_order(reservation,show,seat_number)

def create_show_page(parent,session,show=None): #show parameter (receives a show object) is not none when the admin creates a show 
                                                #through "add another date" button, in show info
    root = Toplevel(parent)
    root.title("Criar espetáculo")
    geometry = controller.calculate_geometry(parent,CREATE_SHOW_SIZE)
    root.geometry(geometry)
    root.resizable(False,False)
    root.config(bg=BG2)
    Label(root, text="Insira as informações do espetáculo",font=("Verdana", 12),bg=BG2, padx=5,pady=5).place(x=10,y=10)
    #Show Name
    Label(root, text="Nome do Espetáculo", bg=BG2, padx=10,pady=10).place(x=10,y=40)
    label_show_name = Entry(root,width=30,borderwidth=2)
    label_show_name.place(x=200,y=50)
    #Date
    Label(root, text="Data do Espetáculo", bg=BG2, padx=10,pady=10).place(x=10,y=100)
    calendar = Calendar(root,selectmode='day',year=2022,month=1,day=1) #Create Calendar object
    calendar.place(x=190,y=100,width=200,height=190)
    #Show Description
    Label(root, text="Descrição do Espetáculo", bg=BG2, padx=10,pady=10).place(x=10,y=310)
    label_show_description = Text(root,height=5)
    label_show_description.place(x=200,y=320,width=190)
    #Populate data if show is not none
    if(show is not None):
        label_show_name.insert(0,show.getShowName())
        label_show_description.delete(1.0,"end") #Good practice -> erase all in Text Widget before insert new text
        label_show_description.insert(1.0,show.getDescription())
    #Button
    Button(root,text="Adicionar Espetáculo",bg="#b2cadb",width=20,height=2,command=lambda:confirm_show_creation(parent,root,session,label_show_name.get(),calendar.get_date(),label_show_description.get("1.0",END))).place(x=10,y=450)
    Button(root,text="Cancelar",bg="#b2cadb",width=10,height=2,command=lambda:choice(root,"cancel")).place(x=200,y=450)
    root.mainloop()

def confirm_show_creation(parent,toplevel_window,session,show_name,show_date,show_description):
    controll = controller.create_show(show_name,show_date,show_description) #Create show and add it to the show list
    if(controll == -1):
        showwarning("Erro!","Dê o nome ao espetáculo!",parent=toplevel_window)
    elif(controll != -1):
        showinfo("Espetáculo inserido!",f'O espetáculo "{show_name}" foi inserido!',parent=toplevel_window)
        show_area(parent,session)

def confirm_show_deletion(parent,toplevel_window,session,show):
    show_id = controller.clear_show(show)
    controller.clear_order_by_show_id(show_id) #delete all related reservations
    showinfo("Espetáculo removido!",f'O espetáculo "{show.getShowName()}" foi removido!',parent=toplevel_window)
    show_area(parent,session)

#---------------------------------------------------
#Opçoes na Window de info de bilhetes
def choice(parent,option):
    if option == "cancel":
        parent.destroy()
#------------------------------------------------------------------------------------------------------------------------
# SHOW AREA -----------------------------------------
def show_area(parent=None,session=None):
    root = Tk()
    if(parent is not None):
        geometry = controller.calculate_geometry(parent,SHOW_AREA_SIZE)
        parent.destroy()
    else:
        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen
        #Calculate the x and y to pop the window in the middle of the screen
        x = int((ws/2) - (SHOW_AREA_SIZE[0]/2))
        y = int((hs/2) - (SHOW_AREA_SIZE[1]/2))
        geometry = str(SHOW_AREA_SIZE[0])+"x"+str(SHOW_AREA_SIZE[1])+"+"+str(x)+"+"+str(y)
    root.title(f"Show Time! - Ver Espetáculo")
    root.geometry(geometry)
    root.resizable(False,False)
    root.config(bg=BG1)
    #texto
    Label(root, text="Espetáculos Disponíveis", font=("Verdana", 16), background="#7dd1bf").grid(row=0, column=1, sticky=W)
    #separaçao
    Label(root, text=" ", bg=BG1).grid(row=1, column=1)
    Label(root, text="", bg=BG1).grid(row=2, column=0)
    #List Box  
    #Create a scrollbar
    scrollbar = Scrollbar(root)
    scrollbar.grid(row=2,column=2)
    #Create List Box
    show_list_box = Listbox(root,yscrollcommand=scrollbar.set,width=100,height=20)
    for shows in controller.model.Show_List:
        show_list_box.insert(END, f"#{shows.getID()} - {shows.getShowName()} na data {shows.getDate()} com {math.ceil((shows.getSeatCount()/shows.getFullCapacity())*100)}% de ocupação")
    show_list_box.grid(row=2,column=1,sticky=W)
    scrollbar.config(command=show_list_box.yview) #Join the scrollbar with the listbox
    #separaçao
    Label(root, text=" ", bg=BG1).grid(row=3, column=1)
    #Botão para redirecionar
    Button(root, text="Consultar espetáculo", command=lambda:list_box_to_show(root,session,show_list_box),width=30, height=3, font=("Arial", 11, "bold"), bg="#2a9c83").grid(column=1, row=4)
    #Info do user
    if(session == None):
        Label(root,text="Sem sessão iniciada", font=("Arial", 9), justify="right", bg=BG1).place(x=570,y=430)
        Button(root,text="Iniciar Sessão",width=15,height=2, font=("Arial", 9, "bold"), background="#5cedce", command=lambda:login_page(root)).place(x=580,y=453)
    else:
        Label(root, text=f"Bem-Vindo {session.getFullName()}", font=("Arial", 9), justify="right", bg=BG1).place(x=400,y=5)
        Label(root, text=f"Data de hoje: {datetime.now():%d/%m/%y}", font=("Arial", 9), justify="right", bg=BG1).place(x=400,y=25)
        #botao espaço utilizador
        Button(root,text="Espaço do Utilizador",width=16,height=2,wraplength=100,font=("Arial", 9, "bold"), background="#5cedce", command=lambda:user_area(root,session)).place(x=560,y=450)
        #encerrar sessao
        Button(root,text="Encerrar Sessão",width=15,height=2, font=("Arial", 9, "bold"), background="red", command=lambda:show_area(root)).place(x=570,y=5)
    root.mainloop()

#receives a list box and return the selected show
def list_box_to_show(root,session,list_box):
    if(list_box.curselection() != ()): #Assuming only one show belongs to the tuple
        i = list_box.curselection()[0] #get selected index in list box
        show_id = int(list_box.get(i)[1:(indexOf(list_box.get(i),"-")-1)]) #Clean the string and get the show ID
        for shows in controller.model.Show_List:
            if(shows.getID() == show_id):
                curr_show = shows #Get respective show object
    else:
        curr_show = None #Show Object
    show_info(root,session,curr_show)

#pop up da info de cada espetáculo - window
def show_info(parent,session,show):
    if(show is not None):
        info_window = Toplevel(parent) # Criar uma página em cima da página atual
        info_window.title(f"Informação do Espetáculo - #{show.getID()}")
        geometry = controller.calculate_geometry(parent,SHOW_INFO_SIZE)
        info_window.geometry(geometry)
        info_window.config(bg=BG1)
        Label(info_window, text=f"Nome do Espetáculo: {show.getShowName()}", font=("Arial", 9), bg=BG1).grid(row=0, column=0, sticky=W)
        Label(info_window, text=f"Data do Espetáculo: {show.getDate()}", font=("Arial", 9), bg=BG1).grid(row=1, column=0, sticky=W)
        Label(info_window, text=f"Descrição: {show.getDescription()}", font=("Arial", 9), bg=BG1).grid(row=2, column=0, sticky=W)
        # Tabela de Preços ---
        Label(info_window, text=f"----------------------------------------------", font=("Arial", 9), bg=BG1).grid(row=3, column=0, sticky=W)
        Label(info_window, text=f"Tabela de Preços:", font=("Arial", 9), bg=BG1).grid(row=4, column=0, sticky=W)
        Label(info_window, text=f"Preço NORMAL - 4,00€", font=("Arial", 9), bg=BG1).grid(row=5, column=0, sticky=W)
        Label(info_window, text=f"Preço VIP - 12,00€", font=("Arial", 9), bg=BG1).grid(row=6, column=0, sticky=W)
        Label(info_window, text=f"----------------------------------------------", font=("Arial", 9), bg=BG1).grid(row=7, column=0, sticky=W)
        # -------
        Label(info_window, text=" ", bg=BG1).grid(row=8, column=0)
        if(session == None):
            Label(info_window, text="Inicie sessão para reservar bilhetes", font=("Arial", 9), bg=BG1).grid(row=9, column=0, sticky=W)
        elif(session.isAdmin() == True):
            show_room(parent,session,info_window,show)
            Button(info_window,wraplength=150,height=2,text="Adicionar nova data para este espetáculo",bg="gray",command=lambda:create_show_page(parent,session,show)).place(x=10,y=300)
            Button(info_window,height=2,text="Remover este espetáculo", bg="gray",command=lambda:confirm_show_deletion(parent,info_window,session,show)).place(x=10,y=350)
        else:
            show_room(parent,session,info_window,show)
        Button(info_window,text="Voltar",width=10,height=2,command=lambda:choice(info_window,"cancel"),bg="gray").place(x=10,y=450)
    else:
        showinfo("Informação","Por favor selecione um espetáculo, ou aguarde por novos espetáculos.")

def show_room(parent,session,info_window,show,seat_change=None): #Print the room in form of buttons
    room = show.getRoom()
    for l in range(len(room)):
        Label(info_window, text=show.getSeatNumber((l,0))[0], font=("Arial", 9), bg=BG1).grid(row=l+5, column=4)
        for c in range(len(room[l])):
            if(l == 0): # Print seat numbers
                Label(info_window, text=show.getSeatNumber((l,c))[1:], font=("Arial", 9), bg=BG1).grid(row=l+4, column=c+5)
            seat_number = show.getSeatNumber((l,c))
            if(room[l][c] == "N0"):
                if(session.isAdmin() == True):
                    Button(info_window,text=" ",padx=16,pady=2,state=DISABLED).grid(column=c+5,row=l+5)
                else:
                    Button(info_window,text=" ",padx=16,pady=2,command=lambda seat_number=seat_number:order(parent,session,info_window,seat_number,show)).grid(column=c+5,row=l+5)
            elif(room[l][c] == "N1"):
                if(seat_change is not None and show.getSeatNumber((l,c)) == seat_change): 
                    Button(info_window,text=" ",bg='green',padx=16,pady=2,command=lambda seat_number=seat_number:order(parent,session,info_window,seat_number,show)).grid(column=c+5,row=l+5)
                else:
                    Button(info_window,text=" ",bg='red',padx=16,pady=2,state=DISABLED).grid(column=c+5,row=l+5)                
            elif(room[l][c] == "V0"):
                if(session.isAdmin() == True):
                    Button(info_window,text="VIP",padx=10,pady=2,state=DISABLED).grid(column=c+5,row=l+5)
                else:
                    Button(info_window,text="VIP",padx=10,pady=2,command=lambda seat_number=seat_number:order(parent,session,info_window,seat_number,show)).grid(column=c+5,row=l+5)
            elif(room[l][c] == "V1"):
                if(seat_change is not None and show.getSeatNumber((l,c)) == seat_change): 
                    Button(info_window,text="VIP",bg='green',padx=10,pady=2,command=lambda seat_number=seat_number:order(parent,session,info_window,seat_number,show)).grid(column=c+5,row=l+5)
                else:
                    Button(info_window,text="VIP",bg='red',padx=10,pady=2,state=DISABLED).grid(column=c+5,row=l+5)  
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
    Button(order_window, text="Reservar", command = lambda:confirm_order(parent,order_window,session,seat_number,show), bg="gray").grid(row=20, column=1)
    Button(order_window, text="Cancelar", command = order_window.destroy, bg="gray").grid(row=20, column=3)

def confirm_order(parent,toplevel_window,session,seat_number,show):
    reservation_id = controller.order_ticket(session,show,seat_number)
    showinfo("Lugar Reservado!",f"Bilhete #{reservation_id} foi reservado!",parent=toplevel_window)
    user_area(parent,session)
#------------------------------------------------------------------------------------------------------------------------
def main():
    controller.start()
    show_area()
    controller.save()