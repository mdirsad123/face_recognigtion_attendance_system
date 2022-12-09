from tkinter import*
from tkinter import ttk
from tkinter.tix import COLUMN
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector.connection






class Student1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("face recognition system")
        
        
        title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        
        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1530,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lfl=Label(self.root,image=self.photoimg_top)
        f_lfl.place(x=0,y=50,width=1500,height=630)
        
        #frame
        main_frame=Frame(f_lfl,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=480,height=630)
        
        
        img_top1=Image.open(r"college_images\bg1.jpg")
        img_top1=img_top1.resize((450,600),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lfl=Label(main_frame,image=self.photoimg_top1)
        f_lfl.place(x=0,y=0,width=450,height=500)
        
        
         #Developer info.
        dev_label=Label(main_frame,text="Design and Develop by Sahil & Gulshan",font=("times new roman",18,"bold"),bg="white",fg="Blue")
        dev_label.place(x=0,y=505)
        
        dev_label=Label(main_frame,text="Python Developers",font=("times new roman",18,"bold"),bg="white",fg="Black")
        dev_label.place(x=0,y=535)
        
        dev_label=Label(main_frame,text="Email: sahilpython78@gmail.com",font=("times new roman",18,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=565)

        dev_label=Label(main_frame,text="Contact: 8409718735",font=("times new roman",18,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=595)
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Student1(root)
    root.mainloop()