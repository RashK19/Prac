import tkinter as tk
from PIL import Image,ImageTk

def see_password():
    password=passvalue.get()
    pass_box.set(password)

def login():
    if(unamevalue!=None and passvalue!=None):
        root.destroy()
        import admin_portal
    else:
        print("fill")

root=tk.Tk()
root.title("Admin Portal")
root.geometry("700x500")
root.resizable(width=False,height=False)

box=tk.Frame(root)

box1=tk.Frame(box,bg="light green")

l1=tk.Label(box1,text="Username",fg="black", bg="light green",font="5").place(x=50,y=80)
l2=tk.Label(box1,text="Password",fg="black",bg="light green",font="5").place(x=50,y=130)

unamevalue= tk.StringVar()
passvalue= tk.IntVar()
pass_box= tk.IntVar()

E_uname=tk.Entry(box1,textvariable=unamevalue).place(x=150,y=80)
E_password=tk.Entry(box1,textvariable=passvalue,show="*").place(x=150,y=130)

seepass=tk.Button(box1,text="see password",command=see_password).place(x=50,y=180)

password_box= tk.Button(box1,text="",textvariable=pass_box).place(x=150 ,y=180)

submit=tk.Button(box1,text="Login",command=login).place(x=50,y=220)

signup=tk.Button(box1,text="Signup if not registered yet?",bg="light green").place(x=50,y=300)

box1.place(width=350,height=400,x=40,y=40)

box2=tk.Frame(box,bg="pink")

box2image= Image.open("logo.png")
maxsize=(350,400)
resized_img=box2image.resize(maxsize,Image.BICUBIC)
box2pic= ImageTk.PhotoImage(resized_img)
picture= tk.Label(box2,image=box2pic).place(x=400,y=90)

box2.place(width=300,height=350,x=400,y=90)

box.place(width=700,height=500)

root.mainloop()