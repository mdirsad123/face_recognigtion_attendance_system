from importlib.resources import path
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from tkinter.tix import COLUMN
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector.connection
import cv2
import os
import numpy as np





class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x750+0+0")
        self.root.title("face recognition system")
        
        
        
        
        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        
        img_top=Image.open(r"college_images\face-recognition.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lfl=Label(self.root,image=self.photoimg_top)
        f_lfl.place(x=0,y=55,width=1530,height=325)
        
       # Button
        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier, font=("times new roman",30,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)
        
        img_botton=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img_botton=img_botton.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_botton)
        
        f_lfl=Label(self.root,image=self.photoimg_bottom)
        f_lfl.place(x=0,y=440,width=1530,height=325)
        
        
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')   #gray scale image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
        
             
            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)    
        
        #============Train the classifier and save ============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
        
        
        
        








if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()