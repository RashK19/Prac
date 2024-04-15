import tkinter as tk
import webview
from PIL import Image,ImageTk

def track_bin():
    root=tk.Toplevel()
    root.title("Track Bin")
    root.geometry("700x500")

    def googlemap():
        url="https://maps.app.goo.gl/MHYGUV4A2e9iVzTX7"
        webbrowser.open(url)

    tk.Button(root,text="open loc",command=googlemap).place(width=200,height=200)

    root.resizable(width=False,height=False)
    root.mainloop()
track_bin()