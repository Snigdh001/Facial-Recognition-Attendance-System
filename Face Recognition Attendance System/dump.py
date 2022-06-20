from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk



class face_detector:
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



if __name__ == "__main__":
    root=Tk()
    obj= face_detector(root)
    root.mainloop()