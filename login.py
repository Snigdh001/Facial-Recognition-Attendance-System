from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import face_recognition_system
import cv2
def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):

        self.var_Sque=StringVar()
        self.var_Sans=StringVar()
        self.var_newpassword=StringVar()

        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1280+0+0")

        bg=Image.open(r"E:\SNIGDH\College\Sem 6\Minor\Login\images\bg.jpg")
        bg=bg.resize((1920,1280),Image.ANTIALIAS)

        self.photoimgbg = ImageTk.PhotoImage(bg)
        lb_bg=Label(self.root,image=self.photoimgbg)
        lb_bg.place(x=0,y=0,relwidth=1,relheight=1)


        frame=Frame(self.root,bg="white")
        frame.place(x=790,y=170,width=340,height=450)

        img1=Image.open(r"E:\SNIGDH\College\Sem 6\Minor\Login\images\login.jpg")
        img1=img1.resize((340,130),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbimg1.place(x=790,y=140,width=340,height=130)


        get_str=Label(frame,text="Get Started",font=("arial",20,"bold"),fg="black",bg="white")
        get_str.place(x=100,y=95)

        #labels
        username=Label(frame,text="Username",font=("arial",15,"bold"),fg="black",bg="white")
        username.place(x=30,y=140)

        self.txtuser=ttk.Entry(frame,font=("arial",15,"bold"))
        self.txtuser.place(x=30,y=170,width=280)

        username=Label(frame,text="Password",font=("arial",15,"bold"),fg="black",bg="white")
        username.place(x=30,y=210)

        self.txtpass=ttk.Entry(frame,font=("arial",15,"bold"))
        self.txtpass.place(x=30,y=240,width=280)

        #loginbutton
        loginbtn=Button(frame,text="Login",command=self.login,font=("arial",15,"bold"),bd=2,relief=RIDGE,fg="black",bg="lightblue")
        loginbtn.place(x=120,y=280,width=100,height=40)

        #additional buttons
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("arial",12,"bold"),borderwidth=0,relief=RIDGE,fg="black",bg="white",activebackground="white")
        registerbtn.place(x=0,y=330,width=180)

        forgetbtn=Button(frame,text="Foget Password",command=self.forgot_password_window,font=("arial",12,"bold"),borderwidth=0,relief=RIDGE,fg="black",bg="white",activebackground="white")
        forgetbtn.place(x=0,y=360,width=180)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="" :
            messagebox.showerror("Error","All feild required",parent=self.root)
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="snigdh",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row== None:
                messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("Login","Access only admin",parent=self.root)
                if open_main>0:
                    self.new_window1=Toplevel(self.root)
                    self.app=face_recognition_system(self.new_window1)
                else :
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    
    #-----forget password-----
    def forget_password(self):
        if self.var_Sque.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.var_Sans.get()=="":
            messagebox.showerror("Error","Enter the answer to the security question",parent=self.root2)
        elif self.var_newpassword.get()=="":
            messagebox.showerror("Error","Enter New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="snigdh",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and security_ques=%s and security_ans=%s")
            value=(self.txtuser.get(),self.var_Sque.get(),self.var_Sans.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row== None:
                messagebox.showerror("Error","Enter the Corrent Answer",parent=self.root2)
            else :
                #print(self.var_newpassword.get())
                query=("update register set password=%s where email=%s")
                value=(self.var_newpassword.get(),self.txtuser.get(),)
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please login with new password",parent=self.root2)
                

        

    cv2.destroyAllWindows()

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter Email Id for reset password",parent=self.
        root)
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="snigdh",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid username",parent=self.
        root)
            else :
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("450x550+610+170")

                lb1=Label(self.root2,text="Forget Password",font=("arial",20,"bold"),fg="red")
                lb1.place(x=0,y=0,relwidth=1)

                Sque=Label(self.root2,text="Select Security Quetion",font=("arial",15,"bold"),fg="black")
                Sque.place(x=30,y=60)
                self.combo_Sque=ttk.Combobox(self.root2,textvariable=self.var_Sque,font=("arial",15,"bold"),state="readonly")
                self.combo_Sque["values"]=("Select","Your Birth Place","Your Pet Name")
                self.combo_Sque.place(x=30,y=100,width=250)
                self.combo_Sque.current(0)
                

                Sans=Label(self.root2,text="Security Answer",font=("arial",15,"bold"),fg="black")
                Sans.place(x=30,y=160)
                Sans_entry=ttk.Entry(self.root2,textvariable=self.var_Sans,font=("arial",15,"bold"))
                Sans_entry.place(x=30,y=200,width=250)

                newpassword=Label(self.root2,text="New Password",font=("arial",15,"bold"),fg="black")
                newpassword.place(x=30,y=260)
                newpassword_entry=ttk.Entry(self.root2,textvariable=self.var_newpassword,font=("arial",15,"bold"))
                newpassword_entry.place(x=30,y=300,width=250)

                btn=Button(self.root2,text="Submit",command=self.forget_password,font=("arial",15,"bold"),fg="black",bg="lightblue")
                btn.place(x=170,y=400)








class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1920x1280+0+0")

        #---------------Variable--------------------------------------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_Sque=StringVar()
        self.var_Sans=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()
        self.var_check=IntVar()

        bg=Image.open(r"E:\SNIGDH\College\Sem 6\Minor\Login\images\bg.jpg")
        bg=bg.resize((1920,1280),Image.ANTIALIAS)

        self.photoimgbg = ImageTk.PhotoImage(bg)
        lb_bg=Label(self.root,image=self.photoimgbg)
        lb_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=300,y=200,width=1200,height=600)

        register_lb=Label(frame,text="Register Here",font=("arial",20,"bold"),fg="red",bg="white")
        register_lb.place(x=20,y=20)
        
        # Label and Entry
        fname=Label(frame,text="First Name",font=("arial",15,"bold"),fg="black",bg="white")
        fname.place(x=40,y=80)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("arial",15,"bold"))
        fname_entry.place(x=40,y=110,width=250)

        lname=Label(frame,text="Last Name",font=("arial",15,"bold"),fg="black",bg="white")
        lname.place(x=320,y=80)
        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("arial",15,"bold"))
        lname_entry.place(x=320,y=110,width=250)

        contact=Label(frame,text="Contact No",font=("arial",15,"bold"),fg="black",bg="white")
        contact.place(x=40,y=160)
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("arial",15,"bold"))
        contact_entry.place(x=40,y=190,width=250)

        email=Label(frame,text="Email",font=("arial",15,"bold"),fg="black",bg="white")
        email.place(x=320,y=160)
        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("arial",15,"bold"))
        email_entry.place(x=320,y=190,width=250)

        Sque=Label(frame,text="Select Security Quetion",font=("arial",15,"bold"),fg="black",bg="white")
        Sque.place(x=40,y=240)
        self.combo_Sque=ttk.Combobox(frame,textvariable=self.var_Sque,font=("arial",15,"bold"),state="readonly")
        self.combo_Sque["values"]=("Select","Your Birth Place","Your Pet Name")
        self.combo_Sque.place(x=40,y=270,width=250)
        self.combo_Sque.current(0)
        

        Sans=Label(frame,text="Security Answer",font=("arial",15,"bold"),fg="black",bg="white")
        Sans.place(x=320,y=240)
        Sans_entry=ttk.Entry(frame,textvariable=self.var_Sans,font=("arial",15,"bold"))
        Sans_entry.place(x=320,y=270,width=250)

        Password=Label(frame,text="Password",font=("arial",15,"bold"),fg="black",bg="white")
        Password.place(x=40,y=320)
        Password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("arial",15,"bold"))
        Password_entry.place(x=40,y=350,width=250)

        confirm_password=Label(frame,text="Confirm Password",font=("arial",15,"bold"),fg="black",bg="white")
        confirm_password.place(x=320,y=320)
        confirm_password_entry=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("arial",15,"bold"))
        confirm_password_entry.place(x=320,y=350,width=250)

        #----------------------Checkbox---------------------------------------
        
        checkbtn=Checkbutton(frame,text="I agree the Team and Conditions",variable=self.var_check,font=("arial",12,"bold"),onvalue=1,offvalue=0,bg="white")
        checkbtn.place(x=40,y=400)

        #--------------Button--------------------------------
        img=Image.open(r"E:\SNIGDH\College\Sem 6\Minor\Login\images\register.jpg")
        img=img.resize((250,60),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=40,y=460,width=250,height=60)

        """img1=Image.open(r"E:\SNIGDH\College\Sem 6\Minor\Login\images\loginbtn.jpg")
        img1=img1.resize((250,60),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.login,borderwidth=0,cursor="hand2")
        b1.place(x=320,y=460,width=250,height=60)"""


    #---------------Function Declaration--------------------
    def register_data(self):
        
        if self.var_fname.get=="" or self.var_email.get()==""or self.var_Sque.get()=="Select"or self.var_Sans.get()=="":
            messagebox.showerror("Error","All fields Are required",parent=self.root)
        elif self.var_password.get()!= self.var_confirm_password.get():
            messagebox.showerror("Error","Entered Password & Confirm Password are not same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms and Conditions",parent=self.root)
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="snigdh",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None :
                messagebox.showerror("Error","User Already Registered, please try another email",parent=self.root)
                return
                
            else :
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_Sque.get(),
                self.var_Sans.get(),
                self.var_password.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Sucessfully",parent=self.root)

if __name__=="__main__":
    main()