import tkinter as tk
from PIL import Image,ImageTk
def worker_reg():
    root=tk.Toplevel()
    root.title("Worker Registration")
    root.geometry("700x500")
    root.resizable(width=False,height=False)
    box=tk.Frame(root,bg="light green")

    box1=tk.Frame(root,bg="pink")

    

    box1.place(y=40,x=20, width=350,height=400)

    box2=tk.Frame(root,bg="light green",padx=100)

    box2image = Image.open("worker.png")

    # Resize the image proportionally
    max_size = (200, 300)  # Define the maximum size for the resized image
    resized_box1image = box2image.resize(max_size, Image.BICUBIC)

    # Convert the image to Tkinter-compatible format
    box2pic = ImageTk.PhotoImage(resized_box1image)

    picture = tk.Label(root, image=box2pic)
    picture.place(x=360,y=40)

    box2.place(x=330,y=40,width=340,height=400)

    box.place(width=700,height=500)
    root.mainloop()
#worker_reg()