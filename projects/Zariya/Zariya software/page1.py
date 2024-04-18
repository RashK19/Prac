import tkinter as tk
from PIL import Image,ImageTk


def open_admin_portal():
    root1.destroy()
    import admin

def open_track_bin():
    root1.destroy()
    import track_bin

root1=tk.Tk()
root1.title("Zariya")
root1.geometry("700x500")
root1.resizable(width=False,height=False)
box=tk.Frame(root1)
box1=tk.Frame(box,bg="#006400")
#logo=Image.open("C:/Users/intel/OneDrive/Desktop/Prac/Projects/zariya/logo.png")
#picture= tk.Label(box1,image=logo).pack()

# Load the image
box1image = Image.open("C:/Users/intel/OneDrive/Desktop/Prac/Projects/zariya/logo.png")

# Resize the image proportionally
max_size = (100, 80)  # Define the maximum size for the resized image
resized_box1image = box1image.resize(max_size, Image.BICUBIC)

# Convert the image to Tkinter-compatible format
box1pic = ImageTk.PhotoImage(resized_box1image)

picture = tk.Label(root1, image=box1pic)
picture.place(x=0,y=0)

label=tk.Label(box1,text="A platform creating transperancy between the citizen and muncipality",bg="#006400",fg="white",font="bold 14").place(x=110,y=15)

box1.place(width=700,height=80)


box2=tk.Frame(box,bg="#FFFFFF")

worker=tk.Button(box2,text="Admin Portal",font="30",bg="#32CD32",command=open_admin_portal).place(x=40,y=100)
track=tk.Button(box2,text="Track bin vehicle",font="30",bg="#32CD32",command=open_track_bin).place(x=40,y=150)
worker=tk.Button(box2,text="Residents Portal",font="30",bg="#32CD32").place(x=40,y=200)

# Load the image
box2image = Image.open("C:/Users/intel/Downloads/zariya poster.png")

# Resize the image proportionally
max_size = (400, 350)  # Define the maximum size for the resized image
resized_image = box2image.resize(max_size, Image.BICUBIC)

# Convert the image to Tkinter-compatible format
box2pic = ImageTk.PhotoImage(resized_image)

picture = tk.Label(root1, image=box2pic)
picture.place(x=250,y=100)

box2.place(y=80,width=700,height=420)


box.place(width=700,height=500)
root1.mainloop()
