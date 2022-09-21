from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from student import Student
from train_model import Train_model
import cv2
from face_recognition import Face_Recognition
from attendance import Attendance
import tkinter
import os
from time import strftime
from datetime import datetime


class face_recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")


        #image 1
        img1=Image.open(r"images\1.jpg")
        img1=img1.resize((960,300),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f1_lb=Label(self.root,image=self.photoimg1)
        f1_lb.place(x=0,y=0,width=960,height=300)

        #image 2
        img2=Image.open(r"images\2.jpg")
        img2=img2.resize((960,300),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f1_lb=Label(self.root,image=self.photoimg2)
        f1_lb.place(x=960,y=0,width=960,height=300)

        #image bg 
        bg=Image.open(r"images\bg.jpg")
        bg=bg.resize((1920,980),Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=300,width=1920,height=980)
        
        #TITLE TEXT
        title_lb=Label(bg_img,text="Face Recognition Attendance System",font=("Arial",30,"bold"),bg="white",fg="black",)
        title_lb.place(x=0,y=0,width=1920,height=45)

        #------------------------------Time Clock--------------------------------------------------
        def time():
            string=strftime("%H:%M:%S %p")
            lb1.config(text=string)
            lb1.after(1000,time)

        lb1=Label(title_lb,font=('Arial',16,'bold'),background='white',foreground='black')
        lb1.place(x=0,y=0,width=150,height=42)
        time()
        

        # STUDENT BUTTON
        img3=Image.open(r"images\3.jpg")
        img3=img3.resize((180,180),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        b1=Button(bg_img,image=self.photoimg3,command=self.student_details,cursor="hand2")
        b1.place(x=170,y=100,width=180,height=180)

        b1=Button(bg_img,text="Student",command=self.student_details,cursor="hand2",font=("Arial",15,"bold"),bg="white",fg="black",)
        b1.place(x=170,y=280,width=180,height=40)

        #FACE DETECTOR
        img4=Image.open(r"images\4.jpg")
        img4=img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.recognizer)
        b1.place(x=450,y=100,width=180,height=180)

        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.recognizer,font=("Arial",15,"bold"),bg="white",fg="black",)
        b1.place(x=450,y=280,width=180,height=40)

        #Student Face Data
        img5=Image.open(r"images\5.jpg")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_dataset)
        b1.place(x=730,y=100,width=180,height=180)

        b1=Button(bg_img,text="Image Data",cursor="hand2",command=self.train_dataset,font=("Arial",15,"bold"),bg="white",fg="black",)
        b1.place(x=730,y=280,width=180,height=40)


        #Attendance
        img6=Image.open(r"images\6.jpg")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_date)
        b1.place(x=1010,y=100,width=180,height=180)

        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_date,font=("Arial",15,"bold"),bg="white",fg="black",)
        b1.place(x=1010,y=280,width=180,height=40)

        #TRAIN MACHINE
        img7=Image.open(r"images\7.jpg")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.train_model,cursor="hand2")
        b1.place(x=1290,y=100,width=180,height=180)

        b1=Button(bg_img,text="Train Model",command=self.train_model,cursor="hand2",font=("Arial",15,"bold"),bg="white",fg="black",)
        b1.place(x=1290,y=280,width=180,height=40)

        #QUIT
        img8=Image.open(r"images\8.jpg")
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.pr_exit)
        b1.place(x=1570,y=100,width=180,height=180)

        b1=Button(bg_img,text="Logout",cursor="hand2",command=self.pr_exit,font=("Arial",15,"bold"),bg="white",fg="black",)
        b1.place(x=1570,y=280,width=180,height=40)


    #---------------------Functions Button--------------------------#
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_model(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_model(self.new_window)

    def train_dataset(self):
        os.startfile("Data")

    def recognizer(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_date(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def pr_exit(self):
        self.pr_exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to Logout?",parent=self.
        root)
        if self.pr_exit>0:
            self.root.destroy()
        else :
            return 

    



if __name__ == "__main__":
    root=Tk()
    obj= face_recognition_system(root)
    root.mainloop()
