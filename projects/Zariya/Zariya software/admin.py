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

def back():
    root2.destroy()
    import page1

def see_password():
    password_box.config(text=passvalue.get())   

def login():
    sql="SELECT * FROM ADMIN WHERE NAME= %s AND PASSWORD= %s"
    val=(unamevalue.get(),passvalue.get())
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    if result:
        root2.destroy()
        import admin_portal
    else:
        wrong_box.config(text="wrong name and password")

def signup():
    root2.destroy()
    import admin_signup

root2=tk.Tk()
root2.title("Admin Portal")
root2.geometry("700x500")
root2.resizable(width=False,height=False)

box=tk.Frame(root2)

#heading start
box1=tk.Frame(box,bg="green")

# Load the image
box1image = Image.open("C:/Users/intel/OneDrive/Desktop/Prac/Projects/zariya/logo.png")

# Resize the image proportionally
max_size = (100, 80)  # Define the maximum size for the resized image
resized_box1image = box1image.resize(max_size, Image.BICUBIC)

# Convert the image to Tkinter-compatible format
box1pic = ImageTk.PhotoImage(resized_box1image)

picture = tk.Label(root2, image=box1pic)
picture.place(x=0,y=0)

label=tk.Label(box1,text="A platform creating transperancy between the citizen and muncipality",bg="green",fg="white",font="bold 14").place(x=110,y=15)

box1.place(width=700,height=80)
#heading end



box2=tk.Frame(box,bg="#D3D3D3")

back=tk.Button(box2,text="Back",command=back).place(x=10,y=30)

l1=tk.Label(box2,text="Username",fg="black", bg="#C0C0C0",font="5").place(x=50,y=80)
l2=tk.Label(box2,text="Password",fg="black",bg="#C0C0C0",font="5").place(x=50,y=130)

unamevalue= tk.StringVar()
passvalue= tk.StringVar()

E_uname=tk.Entry(box2,textvariable=unamevalue).place(x=150,y=80)
E_password=tk.Entry(box2,textvariable=passvalue,show="*").place(x=150,y=130)

seepass=tk.Button(box2,text="see password",command=see_password).place(x=50,y=180)

password_box= tk.Label(box2,text="",bg="#D3D3D3")
password_box.place(x=150, y=180)

submit=tk.Button(box2,text="Login",command=login).place(x=50,y=220)

signup=tk.Button(box2,text="Signup if not registered yet?",bg="light green",command=signup).place(x=50,y=300)

wrong_box=tk.Label(box2)
wrong_box.place(x=50,y=350)

box2.place(width=350,height=450,x=0,y=80)

box3=tk.Frame(box,bg="pink")

box3image= Image.open("projects/Zariya/Zariya software/images/logo.png")
maxsize=(350,400)
resized_img=box3image.resize(maxsize,Image.BICUBIC)
box3pic= ImageTk.PhotoImage(resized_img)
picture= tk.Label(box3,image=box3pic).place(x=400,y=90)

box3.place(width=360,height=450,x=350,y=80)

box.place(width=700,height=500)

root2.mainloop()