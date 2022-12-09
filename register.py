from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector


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
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        b1.place(x=25,y=420,width=200)

        img1=Image.open(r"college_images\loginpng.png")
        img1=img1.resize((200,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimg1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        b2.place(x=330,y=427,width=200)

        # =======================function declaration=====================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="":
            messagebox.showerror("Error","All Field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirmpass must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree your term & condition")
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
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)"(
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
            messagebox.showinfo("Success","Register Succesfully")








if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()