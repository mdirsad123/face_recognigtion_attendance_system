from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector.connection
from datetime import datetime
import cv2
import os
import numpy as np





class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("FACE RECOGNITION")  
         

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        # 1st image
        img_top=Image.open(r"college_images\face_detector1.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lfl=Label(self.root,image=self.photoimg_top)
        f_lfl.place(x=0,y=49,width=650,height=650)
        
        
        
        # 2nd image
        img_botton=Image.open(r"college_images\fg.jpg")
        img_botton=img_botton.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_botton)
        
        f_lfl=Label(self.root,image=self.photoimg_bottom)
        f_lfl.place(x=650,y=49,width=750,height=650)

        # Button
        b1_1=Button(f_lfl,text="Face Recognition",cursor="hand2",command=self.face_recog, font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=280,y=590,width=200,height=40)

        #================= Attendance Mark ================== 
     
    def mark_attendance(self,i,r,n,d):
        with open("irsad.csv","r+",newline="\n") as f:
            myDataList=f.readline()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n Id:{i} , Roll:{r} , Name:{n} , Department:{d} , Time:{dtString} , Date:{d1} , Present")
                
            

      
        #================= Face Recognition ==================   
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                  
                
                 
                conn=mysql.connector.connect(host="localhost",username="root",password="sahil",database="Face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                
                
                
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]
                    
            return coord
            
        def recognize(img,clf,faceCasCade):
            coord=draw_boundary(img,faceCasCade,1.1,10,(255,255,255),"Face",clf)                
            return img
            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
            
        video_cap=cv2.VideoCapture(0)
            
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
                
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()  