from cgitb import text
from math import frexp
import string
from time import strftime
from datetime import datetime
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tkinter
import tkinter
from turtle import title
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from chatbot import ChatBot
from developer import Student1
from attendance import Attendance
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("face recognition system")
        

        # first image
        img=Image.open(r"college_images\Stanford.jpg")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lfl=Label(self.root,image=self.photoimg)
        f_lfl.place(x=0,y=0,width=450,height=100)

        # second image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lfl=Label(self.root,image=self.photoimg1)
        f_lfl.place(x=450,y=0,width=500,height=100)

        # third image
        img2=Image.open(r"college_images\u.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lfl=Label(self.root,image=self.photoimg2)
        f_lfl.place(x=950,y=0,width=500,height=100)

        # bg image
        img3=Image.open(r"college_images\bgimg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFRWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=35)

        # =============== time ====================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl=Label(title_lbl, font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # student button
        img4=Image.open(r"college_images\student.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=180,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=180,y=260,width=200,height=30)

        # Detect face button
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=260,width=200,height=30)

        # Attendance button
        img6=Image.open(r"college_images\report.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=720,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=720,y=260,width=200,height=30)

        # Help desk button
        img7=Image.open(r"college_images\chat1.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chat_data)
        b1.place(x=990,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.chat_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=990,y=260,width=200,height=30)

        # train button
        img8=Image.open(r"college_images\Train.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=180,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=180,y=520,width=200,height=30)

        # photos face button
        img9=Image.open(r"college_images\sample.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=520,width=200,height=30)

        # developer button
        img10=Image.open(r"college_images\images.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=720,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=720,y=520,width=200,height=30)

        # Exit button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=990,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=990,y=520,width=200,height=30)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


        # =======================function button==================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def chat_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Student1(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()