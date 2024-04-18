import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="zariya"
)

def back():
    root.destroy()
    import admin

def submit():
    if(name!="" and age!="0" and designation!=""):
        mycursor=mydb.cursor()
        sql="INSERT INTO ADMIN (NAME,AGE,DESIGNATION) VALUES (%s,%s,%s)"
        val=(name.get(),age.get(),designation.get())
        mycursor.execute(sql,val)
        mydb.commit()
        mydb.close()
        name.set(" ")
        age.set(" ")
        designation.set(" ")
    else:
        print ("wrong")


root =tk.Tk()
root.title("Sign up")
root.geometry("700x500")
root.resizable(width=False,height=True)

box=tk.Frame(root,bg="light pink")

box1=tk.Frame(box,bg="light green").place(width=500,height=400,x=50,y=50)

name=tk.StringVar()
age=tk.IntVar()
designation=tk.StringVar()

back=tk.Button(box1,text="Back",command=back).place(x=10,y=30)

l1=tk.Label(box1,text="Name",font="30").place(x=100,y=100)
l1=tk.Label(box1,text="Age",font="30").place(x=100,y=200)
l1=tk.Label(box1,text="Designation",font="30").place(x=100,y=300)

e_name=tk.Entry(box1,textvariable=name).place(x=320,y=100)
e_age=tk.Entry(box1,textvariable=age).place(x=320,y=200)
e_designation=tk.Entry(box1,textvariable=designation).place(x=320,y=300)

button=tk.Button(box1,text="Submit",command=submit).place(x=250,y=350)

box.place(width=700,height=500)
root.mainloop()