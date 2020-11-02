# -*- coding: utf-8 -*-
"""
Interface for Mapper application
"""

# -*- coding: utf-8 -*-
"""
Code for GUI using Tkinter
"""

import tkinter as tk
from tkinter import filedialog, RIGHT, messagebox
from PIL import ImageTk, Image
import coord, putData

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
        
        image = tk.Button(self, text='Click to select an Image',font=SMALL_FONT,  width=25, command = lambda : self.uploadz(controller)) 
        image.pack(pady=10,padx=10)
        
        Label1 = tk.Label(self ,text = "Enter condition (eg. Hard/Soft):",  bg="black", fg="white", font=SMALL_FONT)
        Label1.pack(pady=10,padx=10)
        cond = tk.Entry(self, width=50)
        cond.pack()
        
        Label2 = tk.Label(self ,text = "Enter page no. (eg. 1/2):",  bg="black", fg="white", font=SMALL_FONT)
        Label2.pack(pady=10,padx=10)
        pg = tk.Entry(self, width=50)
        pg.pack()
        
        Label3 = tk.Label(self ,text = "Enter number of teeth (eg. 37/43):",  bg="black", fg="white", font=SMALL_FONT)
        Label3.pack(pady=10,padx=10)
        teeth = tk.Entry(self, width=50)
        teeth.pack()
        
        done_button = tk.Button(self, text="Done", bg='blue', fg='white', font=LARGE_FONT, command=lambda: self.startexe(cond.get(),pg.get(),teeth.get(),controller))
        done_button.pack(side=RIGHT,padx=5, pady=5)
        
    def uploadz(self, controller):
        global filename
        filety= [("image", ".jpeg"),
                 ("image", ".png"),
                 ("image", ".jpg"),]
        filename = filedialog.askopenfilename(parent=self,title='Image',filetypes=filety)
        if filename != "":
            tk.messagebox.showinfo(title="Success", message="Well done! File selected.")
        else:
            tk.messagebox.showerror(title="Error", message="File not chosen. Try again.")
        
        
    def startexe(self, cond, pg, teeth, controller):
        
        if cond == "" or pg == "" or teeth == "":
            tk.messagebox.showerror(title="Error", message="Please enter the description.")
        else:
            try:
                topx,topy,botx,boty=coord.main(filename)
                putData.main(cond,pg,teeth,topx,topy,botx,boty)
            except:
                tk.messagebox.showerror(title="Error", message="Error")
            if messagebox.askyesno("Done","Do you wish to close this app?"):
                controller.close_window()
            else:
                controller.show_frame(Start)
            
app = Control()
app.title('Mapper App') 
app.geometry("500x450+300+300")
app.configure(bg='black')
app.mainloop()