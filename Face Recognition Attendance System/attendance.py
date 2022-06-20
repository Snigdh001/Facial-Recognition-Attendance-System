from tkinter import*
from tkinter import ttk
from turtle import heading
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import mysql.connector
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog




mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")

        #--------------- text Variable-----------------------------------------------
        self.var_name=StringVar()
        self.var_enrollment=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_dep=StringVar()
        self.var_status=StringVar()

        #image bg 
        bg=Image.open(r"E:\SNIGDH\College\Sem 6\Minor\Face Recognition Attendance System\images\bg.jpg")
        bg=bg.resize((1920,1080),Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        main_frame=Frame(bg_img,bd=5)
        main_frame.place(x=50,y=50,width=1820,height=980)
        
        # Title
        title_lb=Label(self.root,text="Attendance Management",font=("Arial",30,"bold"),bg="white",fg="black")
        title_lb.place(x=0,y=0,width=1920,height=45)


        #left Label Frame
        Left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text='Student Attendance Information',font=("arial",12,"bold"))
        Left_frame.place(x=5,y=5,width=900,height=930)

        #left_inside _frame
        Left_Inside_Frame=LabelFrame(Left_frame,bd=5,relief=RIDGE,text='Class Student Information',font=("arial",12,"bold"))
        Left_Inside_Frame.place(x=5,y=5,width=880,height=890)
        
        #Labels and entry
        #Attendance Name
        Attendance_Name=Label(Left_Inside_Frame,text='Name',font=("arial",12,"bold"))
        Attendance_Name.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        Attendance_Name_entry=ttk.Entry(Left_Inside_Frame,width=20,textvariable=self.var_name,font=("arial",12,"bold"))
        Attendance_Name_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #Attendance Enrollment
        Attendance_Enrollment=Label(Left_Inside_Frame,text='Enrollment',font=("arial",12,"bold"))
        Attendance_Enrollment.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        Attendance_Enrollment_entry=ttk.Entry(Left_Inside_Frame,width=20,textvariable=self.var_enrollment,font=("arial",12,"bold"))
        Attendance_Enrollment_entry.grid(row=0,column=4,padx=10,pady=10,sticky=W)

        #Attendance Date
        Attendance_Date=Label(Left_Inside_Frame,text='Date',font=("arial",12,"bold"))
        Attendance_Date.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        Attendance_Date_entry=ttk.Entry(Left_Inside_Frame,width=20,textvariable=self.var_date,font=("arial",12,"bold"))
        Attendance_Date_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Attendance Time
        Attendance_Time=Label(Left_Inside_Frame,text='Time:',font=("arial",12,"bold"))
        Attendance_Time.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        Attendance_Time_entry=ttk.Entry(Left_Inside_Frame,width=20,textvariable=self.var_time,font=("arial",12,"bold"))
        Attendance_Time_entry.grid(row=1,column=4,padx=10,pady=10,sticky=W)

        #Department
        Attendance_Department=Label(Left_Inside_Frame,text='Department:',font=("arial",12,"bold"))
        Attendance_Department.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        Attendance_Department_entry=ttk.Entry(Left_Inside_Frame,width=20,textvariable=self.var_dep,font=("arial",12,"bold"))
        Attendance_Department_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Attendance
        attendanceLabel=Label(Left_Inside_Frame,text="Status",font=("arial",12,"bold"))
        attendanceLabel.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        self.atten_status=ttk.Combobox(Left_Inside_Frame,textvariable=self.var_status,font=("arial",12,"bold"),state="readonly",width=18)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=2,column=4,padx=10,pady=10,sticky=W)

        #button frame
        btn_frame=Frame(Left_Inside_Frame,bd=5,relief=RIDGE)
        btn_frame.place(x=5,y=260,width=860,height=63)
        
        #Import button
        save_btn=Button(btn_frame,text="Import CSV",command=self.importcsv,font=("arial",12,"bold"),bg="lightblue",fg="black",width=21,height=2)
        save_btn.grid(row=0,column=0)
        
        #Export button
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportcsv,font=("arial",12,"bold"),bg="lightblue",fg="black",width=20,height=2)
        update_btn.grid(row=0,column=1)

        #Update button
        delete_btn=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="lightblue",fg="black",width=20,height=2)
        delete_btn.grid(row=0,column=2)
        
        #Reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reser_data,font=("arial",12,"bold"),bg="lightblue",fg="black",width=20,height=2)
        reset_btn.grid(row=0,column=3)
        
        #Right Label Frame
        Right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text='Attendance',font=("arial",12,"bold"))
        Right_frame.place(x=910,y=5,width=900,height=930)

        #left_inside _frame
        table_frame=LabelFrame(Right_frame,bd=5,relief=RIDGE,text='Attendance Table',font=("arial",12,"bold"))
        table_frame.place(x=5,y=5,width=880,height=890)

        # ----------Scroll Bar Table ----------
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("name","dep","enrollment","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("enrollment",text="Enrollment")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("status",text="Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("enrollment",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("status",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        global mydata
        mydata.clear()
        fln="List.csv"
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #--------------Fetch Data ------------------------------

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import CSV
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #export CSV
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data Exported to "+os.path.basename(fln)+" Successfully",parent=self.
        root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    # ----------------------------------------------------------------
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_name.set(rows[0])
        self.var_enrollment.set(rows[1])
        self.var_date.set(rows[2])
        self.var_time.set(rows[3])
        self.var_dep.set(rows[4])
        self.var_status.set(rows[5])

    def reser_data(self):
        self.var_name.set("")
        self.var_enrollment.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_dep.set("")
        self.var_status.set("Status")

    def update_status(self):
        pass
if __name__ == "__main__":
    root=Tk()
    obj= Attendance(root)
    root.mainloop()