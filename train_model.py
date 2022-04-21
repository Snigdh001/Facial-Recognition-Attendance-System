from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np



class Train_model:
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

        title_lb=Label(self.root,text="Train Model",font=("Arial",30,"bold"),bg="white",fg="black")
        title_lb.place(x=25,y=25,width=1870,height=45)

        img1=Image.open(r"E:\SNIGDH\College\Sem 6\Minor\Face Recognition Attendance System\images\training model.jpg")
        img1=img1.resize((960,300),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f1_lb=Label(self.root,image=self.photoimg1)
        f1_lb.place(x=25,y=70,width=1870,height=400)

        #Button
        img7=Image.open(r"E:\SNIGDH\College\Sem 6\Minor\Face Recognition Attendance System\images\7.jpg")
        img7=img7.resize((250,250),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.train_model,cursor="hand2")
        b1.place(x=835,y=480,width=250,height=250)

        b1=Button(bg_img,text="Train Model",command=self.train_model,cursor="hand2",font=("Arial",15,"bold"),bg="white",fg="black",)
        b1.place(x=835,y=730,width=250,height=50)

        #-----------------------------------------------------------
    def train_model(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        Faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #greyscale images
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            #print(imagenp,id)

            Faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #----------------Train the Classifier and Save------------------------------
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(Faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Model with DataSet is Completed ",parent=self.
        root)



            
if __name__ == "__main__":
    root=Tk()
    obj= Train_model(root)
    root.mainloop()