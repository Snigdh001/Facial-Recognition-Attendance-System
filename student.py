from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import traceback




class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")

        #------------------Variables-------------------------#
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_enroll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        #image bg 
        bg=Image.open(r"images\bg.jpg")
        bg=bg.resize((1920,1080),Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        main_frame=Frame(bg_img,bd=5)
        main_frame.place(x=50,y=50,width=1820,height=980)

        #left Label Frame
        Left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text='Student Information',font=("arial",12,"bold"))
        Left_frame.place(x=5,y=5,width=900,height=930)

        #-------------------Current course Frame-----------------------------#        
        Current_Course_frame=LabelFrame(Left_frame,bd=5,relief=RIDGE,text='Current Course',font=("arial",12,"bold"))
        Current_Course_frame.place(x=5,y=5,width=885,height=130)

        #Department 
        dep_label=Label(Current_Course_frame,text='Department',font=("arial",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_dep,font=("arial",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Engineering","Management","Pharmacy")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        #Course label
        dep_label=Label(Current_Course_frame,text='Course',font=("arial",12,"bold"))
        dep_label.grid(row=0,column=2,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_course,font=("arial",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Course","B.Tech","B.Com","B.Sc","B.Pharma","MBA","M.com")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        
        #Year label
        dep_label=Label(Current_Course_frame,text='Year',font=("arial",12,"bold"))
        dep_label.grid(row=1,column=0,padx=10,sticky=W)
        #year column
        dep_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_year,font=("arial",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Year","Year-1","Year-2","Year-3","Year-4")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Semester
        dep_label=Label(Current_Course_frame,text='Semester',font=("arial",12,"bold"))
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_sem,font=("arial",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        #-------------------Class Student Information-----------------------------#
        Class_Student_Frame=LabelFrame(Left_frame,bd=5,relief=RIDGE,text='Class Student Information',font=("arial",12,"bold"))
        Class_Student_Frame.place(x=5,y=140,width=885,height=755)
        
        #student id 
        studentid=Label(Class_Student_Frame,text='Student ID',font=("arial",12,"bold"))
        studentid.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        studentID_entry=ttk.Entry(Class_Student_Frame,textvariable=self.var_id,width=20,font=("arial",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #student Name 
        studentname=Label(Class_Student_Frame,text='Student Name',font=("arial",12,"bold"))
        studentname.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        studentname_entry=ttk.Entry(Class_Student_Frame,textvariable=self.var_name,width=20,font=("arial",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #Class Division 
        class_div=Label(Class_Student_Frame,text='Class Division',font=("arial",12,"bold"))
        class_div.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        class_div_combo=ttk.Combobox(Class_Student_Frame,textvariable=self.var_div,font=("arial",12,"bold"),state="readonly",width=18)
        class_div_combo["values"]=("1","2","3","4")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Enrollment no 
        enrollment_no=Label(Class_Student_Frame,text='Enrollment No',font=("arial",12,"bold"))
        enrollment_no.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        enrollment_no_entry=ttk.Entry(Class_Student_Frame,textvariable=self.var_enroll,width=20,font=("arial",12,"bold"))
        enrollment_no_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #Gender 
        gender=Label(Class_Student_Frame,text='Gender',font=("arial",12,"bold"))
        gender.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        gender_combo=ttk.Combobox(Class_Student_Frame,textvariable=self.var_gender,font=("arial",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Date of Birth
        DOB=Label(Class_Student_Frame,text='DOB',font=("arial",12,"bold"))
        DOB.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        DOB_entry=ttk.Entry(Class_Student_Frame,textvariable=self.var_dob,width=20,font=("arial",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Phone No 
        phone_no=Label(Class_Student_Frame,text='Phone No',font=("arial",12,"bold"))
        phone_no.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        phone_no_entry=ttk.Entry(Class_Student_Frame,textvariable=self.var_phone,width=20,font=("arial",12,"bold"))
        phone_no_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #Address
        Address=Label(Class_Student_Frame,text='Address',font=("arial",12,"bold"))
        Address.grid(row=3,column=2,padx=10,pady=10,sticky=W)
        Address_entry=ttk.Entry(Class_Student_Frame,textvariable=self.var_address,width=20,font=("arial",12,"bold"))
        Address_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        #Email
        email=Label(Class_Student_Frame,text='Email',font=("arial",12,"bold"))
        email.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        email_entry=ttk.Entry(Class_Student_Frame,textvariable=self.var_email,width=20,font=("arial",12,"bold"))
        email_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #Teacher
        teacher=Label(Class_Student_Frame,text='Teacher',font=("arial",12,"bold"))
        teacher.grid(row=4,column=2,padx=10,pady=10,sticky=W)
        teacher_entry=ttk.Entry(Class_Student_Frame,textvariable=self.var_teacher,width=20,font=("arial",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)

        # Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_Frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(Class_Student_Frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #button frame
        btn_frame=Frame(Class_Student_Frame,bd=5,relief=RIDGE)
        btn_frame.place(x=5,y=260,width=870,height=115)
        
        #Save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("arial",12,"bold"),bg="lightblue",fg="black",width=21,height=2)
        save_btn.grid(row=0,column=0)
        
        #Update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="lightblue",fg="black",width=21,height=2)
        update_btn.grid(row=0,column=1)

        #Delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",12,"bold"),bg="lightblue",fg="black",width=20,height=2)
        delete_btn.grid(row=0,column=2)
        
        #Reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="lightblue",fg="black",width=20,height=2)
        reset_btn.grid(row=0,column=3)
        
        take_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,font=("arial",12,"bold"),bg="lightblue",fg="black",width=21,height=2)
        take_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame,text="Update Photo",command=self.generate_dataset,font=("arial",12,"bold"),bg="lightblue",fg="black",width=21,height=2)
        update_photo_btn.grid(row=1,column=1)

        #----------------Right Label Frame---------------------#
        Right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text='Student Details',font=("arial",12,"bold"))
        Right_frame.place(x=910,y=5,width=900,height=930)

        #-------------------------------Image in Right columb---------------------------------#
        """
        img1=Image.open(r"images\1.jpg")
        img1=img1.resize((890,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f1_lb=Label(Right_frame,image=self.photoimg1)
        f1_lb.place(x=0,y=0,width=890,height=200)
        """
        #---------------------Search Frame----------------------#
        search_frame=LabelFrame(Right_frame,bd=5,relief=RIDGE,text='Search System',font=("arial",12,"bold"))
        search_frame.place(x=5,y=5,width=885,height=100)

        search_label=Label(search_frame,text='Search By',font=("arial",12,"bold"),bg="lightgreen",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("arial",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("arial",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("arial",12,"bold"),bg="lightblue",fg="black",width=12,height=1,padx=20)
        search_btn.grid(row=0,column=3)

        showall_btn=Button(search_frame,text="Show All",font=("arial",12,"bold"),bg="lightblue",fg="black",width=12,height=1, padx=20)
        showall_btn.grid(row=0,column=4)

        #-------------------------Table Frame----------------#
        table_frame=Frame(Right_frame,bd=5,relief=RIDGE,)
        table_frame.place(x=5,y=110,width=885,height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","enroll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("enroll",text="Enroll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Status")
        self.student_table["show"]="headings"

        #This line for each attribute for spacing in table_frame
        """self.student_table.column("dep",width="100")"""

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #-------------------------Functions Declarations ------------------------#
    def add_data(self):
        if (self.var_radio1.get()=="No"):
             messagebox.showerror("Error","Please Take photo Sample",parent=self.root)
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course"or self.var_year.get()=="Select Year"or self.var_radio1.get()=="No" or self.var_sem.get()=="Select Semester"or self.var_name.get()==""or self.var_id.get()=="" or self.var_enroll.get()=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)            
        else :
            try :
                conn=mysql.connector.connect(host="localhost", user="root", password="snigdh", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                                                        self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_year.get(),
                                                        self.var_sem.get(),
                                                        self.var_id.get(),
                                                        self.var_name.get(),
                                                        self.var_div.get(),
                                                        self.var_enroll.get(),
                                                        self.var_gender.get(),
                                                        self.var_dob.get(),
                                                        self.var_email.get(),
                                                        self.var_phone.get(),
                                                        self.var_address.get(),
                                                        self.var_teacher.get(),
                                                        self.var_radio1.get(),
                ))
                #todo choose yes no data face added
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #---------------------------Fetch Data in Table-------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", user="root", password="snigdh", database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)>-1:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()
            
        

    #---------------------get cursor---------------------------------------------
    def get_cursor(self,event=""):
        cursor_focus =self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_enroll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
    #-------------------Update Function----------------#
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_id.get()=="" or self.var_enroll.get()=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", user="root", password="snigdh", database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Student_ID=%s,Name=%s,Division=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Enrollment=%s",(
                                                        self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_year.get(),
                                                        self.var_sem.get(),
                                                        self.var_id.get(),
                                                        self.var_name.get(),
                                                        self.var_div.get(),
                                                        self.var_gender.get(),
                                                        self.var_dob.get(),
                                                        self.var_email.get(),
                                                        self.var_phone.get(),
                                                        self.var_address.get(),
                                                        self.var_teacher.get(),
                                                        self.var_radio1.get(),
                                                        self.var_enroll.get()==id+1,
                                                        
                    ) )
                
                else :
                    if not Update:
                        return 
                messagebox.showinfo("Scccess","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to str({es})",parent=self.root)
    #-------------------Delete Functions ------------------------#
    def delete_data(self):
        if self.var_enroll.get()=="":
            messagebox.showerror("Error","Enrollment must be required",parent=self.root)
        else :
            try:
                Delete=messagebox.askyesno("Student Delete","Do you want to delete this student?",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost", user="root", password="snigdh", database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Enrollment=%s;"
                    val=(self.var_enroll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return 

                messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due TO: {str(es)}",parent=self.root)
    #-------------------Reset----------------------------------------------------
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_div.set(""),
        self.var_enroll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    #-------------------Generate Data Set & take photo-------------------------
    def generate_dataset(self):
        
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_id.get()=="" or self.var_enroll.get()=="" or self.var_radio1.get()=="No":
            messagebox.showerror("Error","All Fields are required",parent=self.
        root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", user="root", password="snigdh", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id=id+1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Student_ID=%s,Name=%s,Division=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Enrollment=%s",(
                                                        self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_year.get(),
                                                        self.var_sem.get(),
                                                        self.var_id.get(),
                                                        self.var_name.get(),
                                                        self.var_div.get(),
                                                        self.var_gender.get(),
                                                        self.var_dob.get(),
                                                        self.var_email.get(),
                                                        self.var_phone.get(),
                                                        self.var_address.get(),
                                                        self.var_teacher.get(),
                                                        self.var_radio1.get(),
                                                        self.var_enroll.get()
                                            
                                                        ))  
                conn.commit()
                #self.reset_data()
                self.fetch_data()
                
                conn.close()

                #--------------Load pridefine data----------#
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(img,1.05,10)
                    #scaling factor= 1.3 for reducing size
                    # minimum neighbor=5 for better detection
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h+10,x:x+w+10]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while TRUE:
                    
                    en=self.var_enroll.get()[-6:]
                    # print(en)
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1

                        face=cv2.resize(face_cropped(my_frame),(400,400))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+en+"."+str(img_id)+".jpg"
                        # print(file_name_path)
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(254,254,254),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data set Completed!!!!!",parent=self.root)

            except Exception as es:
                #traceback.print_exc(es)
                messagebox.showerror("Error",f"Due to str({es})",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj= Student(root)
    root.mainloop()