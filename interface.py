# -*- coding: utf-8 -*-
"""
Code for GUI using Tkinter
"""

import tkinter as tk
from tkinter import filedialog, RIGHT, messagebox
from PIL import ImageTk, Image
import miner

dates=filename=""

LARGE_FONT=("Times","15","bold")
SMALL_FONT=("Verdana","10","bold")

class Control(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = Start(container, self)
        self.frames[Start] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Start)
        self.resizable(False, False)
        #self.iconbitmap('icon.ico')

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.config(background='white')
        frame.tkraise()
        
    def close_window(self):
        self.destroy()
        
        
class Start(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        load = Image.open("logo.jpg")
        render = ImageTk.PhotoImage(load)
        
        img = tk.Label(self, image=render, bg="black")
        img.image = render
        img.place(x=85,y=5)
        img.pack()
        
        label = tk.Label(self, text="Hello!",bg="white", fg="blue", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        """
        csvLabel = tk.Label(self ,text = "Enter Description:",  bg="white", fg="black", font=SMALL_FONT)
        csvLabel.pack(pady=10,padx=10)
        dates = tk.Entry(self, width=50)
        dates.pack()
        """
        
        zoom_chat = tk.Button(self, text='Click to select PDF files',font=SMALL_FONT,  width=25, command = lambda : self.uploadz(controller)) 
        zoom_chat.pack(pady=10,padx=10)
        
        done_button = tk.Button(self, text="Done", bg='blue', fg='white', font=LARGE_FONT, command=lambda: self.startexe(controller))
        done_button.pack(side=RIGHT,padx=5, pady=5)
        
    def uploadz(self, controller):
        global filename
        filety= [("pdf files", "*.pdf")]
        filename = filedialog.askopenfilename(parent=self,title='PDF file',filetypes=filety)
        if filename != "":
            tk.messagebox.showinfo(title="Success", message="Well done! File selected.")
        else:
            tk.messagebox.showerror(title="Error", message="File not chosen. Try again.")
        
        
    def startexe(self, controller):
        """
        if dates == "":
            tk.messagebox.showerror(title="Error", message="Please enter a description.")
        else:
            """
        try:
            miner.main(filename)
        except:
            tk.messagebox.showerror(title="Error", message="Error")
        if messagebox.askyesno("Done","Thank you. Do you want to close this app?"):
            controller.close_window()
        else:
            controller.show_frame(Start)
            
app = Control()
app.title('OCR App') 
app.geometry("500x260+300+300")
app.configure(bg='black')
app.mainloop()