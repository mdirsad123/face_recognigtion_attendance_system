from ast import Delete
from importlib.resources import contents
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("face recognition system")

        # ============ variables===================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()



        # first image
        img=Image.open(r"college_images\smart.jpg")
        img=img.resize((700,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lfl=Label(self.root,image=self.photoimg)
        f_lfl.place(x=0,y=0,width=700,height=200)

        # second image
        img1=Image.open(r"college_images\clg.jpeg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lfl=Label(self.root,image=self.photoimg1)
        f_lfl.place(x=700,y=0,width=800,height=200)

        # bg image
        img3=Image.open(r"college_images\bgimg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="Attendance management system",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1430,height=35)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=40,width=1330,height=445)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendace details",font="comicsansns 11 bold")
        Left_frame.place(x=10,y=10,width=660,height=430)

        img_left=Image.open(r"college_images\clg.jpeg")
        img_left=img_left.resize((650,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lfl=Label(Left_frame,image=self.photoimg_left)
        f_lfl.place(x=5,y=0,width=650,height=100)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=100,width=650,height=305)

        # ==========================labes entry=========================================
        # Attendance id
        AttendanceId_label=Label(left_inside_frame,text="AttendanceId:",font="comicsansns 11 bold",bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font="comicsansns 11 bold")
        AttendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # roll
        rollLabel=Label(left_inside_frame,text="Roll:",font="comicsansns 11 bold",bg="white")
        rollLabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # name
        nameLabel=Label(left_inside_frame,text="Name:",font="comicsansns 11 bold",bg="white")
        nameLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # department
        deplabel=Label(left_inside_frame,text="Department:",font="comicsansns 11 bold",bg="white")
        deplabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # time
        timelabel=Label(left_inside_frame,text="Time:",font="comicsansns 11 bold",bg="white")
        timelabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # date
        date_label=Label(left_inside_frame,text="Date:",font="comicsansns 11 bold",bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Attendance
        attendance_label=Label(left_inside_frame,text="Attendance Status:",font="comicsansns 11 bold",bg="white")
        attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["value"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=245,width=645,height=40)
        

        save_btn=Button(btn_frame,text="Import csv",width=17,command=self.importCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",width=17,command=self.exportCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)








        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance details",font="comicsansns 11 bold")
        Right_frame.place(x=680,y=10,width=640,height=430)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=630,height=400)

        # ==========scroll bar table=========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id",text="Attendance id")
        self.AttendaceReportTable.heading("roll",text="Roll")
        self.AttendaceReportTable.heading("name",text="Name")
        self.AttendaceReportTable.heading("department",text="Department")
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("date",text="Date")
        self.AttendaceReportTable.heading("attendance",text="Attendance")

        self.AttendaceReportTable["show"]="headings"

        self.AttendaceReportTable.column("id",width=100)
        self.AttendaceReportTable.column("roll",width=100)
        self.AttendaceReportTable.column("name",width=100)
        self.AttendaceReportTable.column("department",width=100)
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("attendance",width=100)

        self.AttendaceReportTable.pack(fill=BOTH,expand=1)

        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # ================fetch data===============

    def fetchdata(self,row):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in row:
            self.AttendaceReportTable.insert("",END,values=i)
    #import csv file

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #export csv file
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open (fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        Cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(Cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    # ==================reset data=================
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")







if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()