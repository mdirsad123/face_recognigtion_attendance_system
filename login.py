from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import string
from time import strftime
from datetime import datetime
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


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("Login")

        # bg image
        lbl_bg=Image.open(r"college_images\bgimg.jpg")
        lbl_bg=lbl_bg.resize((1530,710),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(lbl_bg)

        bg_img=Label(self.root,image=self.bg)
        bg_img.place(x=0,y=0,width=1530,height=710)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=130,width=340,height=450)

        img1=Image.open(r"college_images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        labelimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        labelimg1.place(x=620,y=140,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100,)

        # ===============Label==================
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="white")
        username.place(x=70,y=155)

        self.textuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textuser.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        password.place(x=70,y=225)

        self.textpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textpass.place(x=40,y=250,width=270)

        # ===============Icon image=============
        img2=Image.open(r"college_images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        labelimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        labelimg2.place(x=540,y=285,width=25,height=25)

        img3=Image.open(r"college_images\lock.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        labelimg3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        labelimg3.place(x=540,y=355,width=25,height=25)

        #login button
        loginbtn=Button(frame,text="Login",bd=3,relief=RIDGE,command=self.login,font=("times new roman",15,"bold"),bg="red",fg="white",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registration button
        loginbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        loginbtn.place(x=13,y=350,width=160)

        #forgetpassbtn
        loginbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        loginbtn.place(x=8,y=380,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        self.var_email=StringVar()
        self.var_pass=StringVar()
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","all field required",parent=self.root)
        elif self.textuser.get()=="kapu" and self.textpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to md irsad",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sahil",database="Face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                        self.textuser.get(),
                                                        self.textpass.get()
                
                                                    ))
            row=my_cursor.fetchone()
            #=========print(row)
            if row==None:
                messagebox.showerror("Error","Invalid username & password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                    
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    # ==============================reset password==================================
    def reset_pass(self):
        if self.security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sahil",database="Face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.textuser.get(),self.security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Errir","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.textuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()










    # =============================forgot password window=========================
    def forgot_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","please enter the email address to forgot the password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sahil",database="Face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")


                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=0,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.security_Q["value"]=("Select","Your birth place","Your girlfriend name","Your pet name")
                self.security_Q.current(0)
                self.security_Q.place(x=50,y=110,width=220)
                

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=160)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=190,width=220)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=230)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=260,width=220)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=100,y=300)










# ==================================================register class========================================
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("Register")



        # =======================variables=================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.combo_security_Q=StringVar()
        

        #===================== bg image=================
        bg_lbl=Image.open(r"college_images\hackers2.jpg")
        bg_lbl=bg_lbl.resize((1530,710),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg_lbl)

        bg_img=Label(self.root,image=self.bg)
        bg_img.place(x=0,y=0,width=1530,height=710)

        # ====================left bg image====================
        left_lbl=Image.open(r"college_images\thought.jpg")
        
        self.bg1=ImageTk.PhotoImage(left_lbl)

        bg_img=Label(self.root,image=self.bg1)
        bg_img.place(x=50,y=100,width=470,height=500)

        #==============main frame=========================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=700,height=500)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #==============lebel and entry======================

        #----------------row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=220)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=220)

        #-------------------row 2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=220)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=220)

        #---------------------row3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.security_Q["value"]=("Select","Your birth place","Your girlfriend name","Your pet name")
        self.security_Q.current(0)
        self.security_Q.place(x=50,y=270,width=220)
        

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=220)

        #------------------row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=220)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=220)

        # ===================check button=======================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Term & Condition",font=("times new roman",11,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # ======================button=====================
        img=Image.open(r"college_images\register-now-button1.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,borderwidth=0,command=self.register_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        b1.place(x=25,y=420,width=200)

        img1=Image.open(r"college_images\loginpng.png")
        img1=img1.resize((200,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimg1,borderwidth=0,command=self.return_login,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        b2.place(x=330,y=427,width=200)

        # =======================function declaration=====================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirmpass must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree your term & condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sahil",database="Face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Succesfully",parent=self.root)

    def return_login(self):
        self.root.destroy()
        



# ========================================face recognition main class========================================
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
    main()