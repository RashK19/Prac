import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="zariya"
)

mycursor=mydb.cursor()

#for toggle 
# def see_password():
#     if password_box.cget("show") == "*":
#         password_box.config(show="")
#     else:
#         password_box.config(show="*")

def see_password():
    password_box.config(text=passvalue.get())   

def login():
    sql="SELECT * FROM ADMIN WHERE NAME= %s AND PASSWORD= %s"
    val=(unamevalue.get(),passvalue.get())
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    if result:
        root.destroy()
        import admin_portal
    else:
        wrong_box.config(text="wrong name and password")

def signup():
    root.destroy()
    import admin_signup

root=tk.Tk()
root.title("Admin Portal")
root.geometry("700x500")
root.resizable(width=False,height=False)

box=tk.Frame(root)

box1=tk.Frame(box,bg="light green")

l1=tk.Label(box1,text="Username",fg="black", bg="light green",font="5").place(x=50,y=80)
l2=tk.Label(box1,text="Password",fg="black",bg="light green",font="5").place(x=50,y=130)

unamevalue= tk.StringVar()
passvalue= tk.StringVar()

E_uname=tk.Entry(box1,textvariable=unamevalue).place(x=150,y=80)
E_password=tk.Entry(box1,textvariable=passvalue,show="*").place(x=150,y=130)

seepass=tk.Button(box1,text="see password",command=see_password).place(x=50,y=180)

password_box= tk.Label(box1,text="",bg="light green")
password_box.place(x=150, y=180)

submit=tk.Button(box1,text="Login",command=login).place(x=50,y=220)

signup=tk.Button(box1,text="Signup if not registered yet?",bg="light green",command=signup).place(x=50,y=300)

wrong_box=tk.Label(box1)
wrong_box.place(x=50,y=350)

box1.place(width=350,height=400,x=40,y=40)

box2=tk.Frame(box,bg="pink")

box2image= Image.open("projects/Zariya/Zariya software/images/logo.png")
maxsize=(350,400)
resized_img=box2image.resize(maxsize,Image.BICUBIC)
box2pic= ImageTk.PhotoImage(resized_img)
picture= tk.Label(box2,image=box2pic).place(x=400,y=90)

box2.place(width=300,height=350,x=400,y=90)

box.place(width=700,height=500)

root.mainloop()