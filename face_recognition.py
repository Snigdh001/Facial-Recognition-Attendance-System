from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import numpy as np
from time import strftime
from datetime import datetime




class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")

        #image bg 
        bg=Image.open(r"E:\SNIGDH\College\Sem 6\Minor\Face Recognition Attendance System\images\bg.jpg")
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
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((N not in name_list ) and (E not in name_list ) and (D not in name_list )):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{N},{E},{D},{dtString},{d1},Present")
            else :
                pass

        #-----------Face recognition----------
    def face_recog(self):

        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            cordi=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w+10,y+h+10),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                print(clf.predict(gray_image[y:y+h,x:x+w]))

                conn=mysql.connector.connect(host="localhost", user="root", password="snigdh", database="face_recognition")
                my_cursor=conn.cursor()

                try:
                    my_cursor.execute("select Name from student where Student_ID="+str(id))
                    N=my_cursor.fetchone()
                    N="+".join(N)

                    my_cursor.execute("select Department from student where Student_ID="+str(id))
                    D=my_cursor.fetchone()
                    D="+".join(D)

                    my_cursor.execute("select Enrollment from student where Student_ID="+str(id))
                    E=my_cursor.fetchone()
                    E="+".join(E)

                except Exception as es:
                    messagebox.showerror("Error executing",f"Due to str: {es}",parent=self.root)
                    video_cap.release() 
                    
                if confidence>50:
                    cv2.putText(img,f"Name:{N}",(x,y-75),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Department:{D}",(x,y-15),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Enrollment:{E}",(x,y-45),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
                    self.mark_attendance(N,D,E)
                else :
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(img,"Unknown Face",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)
                cordi=[x,y,w,y]

            return cordi
        
        def recognition(img,clf,faceCascade):
            cordi=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognition(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj= Face_Recognition(root)
    root.mainloop()