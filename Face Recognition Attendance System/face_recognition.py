from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import numpy as np
from time import strftime
from datetime import datetime

from zmq import NULL




class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")

        #image bg 
        bg=Image.open(r"images\bg.jpg")
        bg=bg.resize((1920,1080),Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        b1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_recog, font=("Arial", 15, "bold"),
                    bg="white", fg="black")
        b1.place(x=835, y=700, width=250, height=60)

        #-----------------------------------------------------Mark Attendance-----------------
    def mark_attendance(self,N,E,D):
        with open("List.csv","r+",newline="\n") as f:
            myDataList=[NULL]
            myDataList=f.readlines()
            name_list=[]
            #print(myDataList)
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
                """ name_list.append(entry[1])
                name_list.append(entry[2])
                name_list.append(entry[4])"""

                #print(name_list)
                #or ((N in name_list) and (E in name_list) and (D in name_list) and (datetime.now().strftime("%d/%m/%Y") not in name_list)))
            if((N not in name_list ) and (E not in name_list ) and (D not in name_list )) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{N},{E},{D},{dtString},{d1},Present\n")
            else :
                pass

        #-----------Face recognition----------
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            cordi=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", user="root", password="snigdh", database="face_recognition")
                my_cursor=conn.cursor()
                #print(id,type(id))
                my_cursor.execute("select Name from student where Enrollment like '%{}'".format(id))    
                N=my_cursor.fetchone()
                N="+".join(N)


                my_cursor.execute("select Department from student where Enrollment like '%{}'".format(id))
                D=my_cursor.fetchone()
                D="+".join(D)

                my_cursor.execute("select Enrollment from student where Enrollment like '%{}'".format(id))
                E=my_cursor.fetchone()
                E="+".join(E)
                    
                if confidence>80:
                    cv2.putText(img,f"Name:{N}",(x,y-75),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{D}",(x,y-15),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Enrollment:{E}",(x,y-45),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(N,D,E)
                else :
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
                
                cordi=[x,y,w,h]

            return cordi
        
        def recognize(img,clf,faceCascade):
            cordi=draw_boundray(img,faceCascade,1.05,10,(255,255,255),"Face",clf)
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
    obj= Face_Recognition(root)
    root.mainloop()