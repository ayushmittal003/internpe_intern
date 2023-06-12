from tkinter import *
from time import strftime

root=Tk()
root.geometry("300x100")
root.title("Digital clock by Ayush")

def ayush():
    string=strftime("%H:%M:%S %p")
    lable.config(text=string)
    lable.after(1000,ayush)

lable=Label(root,font=("calibari",20,"bold"),bg="black",fg="cyan")
lable.pack(anchor="center",ipadx=30,ipady=30)

ayush()

root.mainloop()
