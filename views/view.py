from cProfile import label
from tkinter import *
#Global
WIDTH, HEIGHT = 900,900

def login_page(root):
    root.geometry("350x350")
    root.resizable(False,False)
    Label(root, text="Welcome to Show Time!", padx=10,pady=10).grid(column=0,row=0, sticky=W)
    #Email
    Label(root, text="Email", padx=10,pady=10).grid(column=0,row=1, sticky=W)
    Entry(root,width=30,borderwidth=2).grid(column=1,row=1)
    #Password
    Label(root, text="Password", padx=10,pady=10).grid(column=0,row=2, sticky=W)
    Entry(root,width=30,borderwidth=2).grid(column=1,row=2)
    #Button
    Button(root,text="Login",width=10,height=2).grid(column=0,row=3)
    Button(root,text="Register",width=10,height=2).grid(column=1,row=3)
    root.mainloop()

def main():
    root = Tk()
    root.title("Show Time!")
    

    login_page(root)
    

    
