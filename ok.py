from tkinter import *

OPTIONS = [
"hello_world",
"save_file",
"create_object"
] #etc


def hello_world():
    print("Hello World")
    pass


def save_file():
    print("File Saved")
    pass


def create_object():
    print("Object Created")
    pass


def picker():
    if variable.get() == "hello_world":
        hello_world()
    if variable.get() == "save_file":
        save_file()
    if variable.get() == "create_object":
        create_object()


root = Tk()
root.geometry("100x100")
root.title("Dropdown demo")

variable = StringVar(root)
variable.set(OPTIONS[0]) # default value

om = OptionMenu(root, variable, *OPTIONS)
om.pack()

caller_button = Button(text="Call function", command=lambda: picker())
caller_button.pack(pady=10)


mainloop()