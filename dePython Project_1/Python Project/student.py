from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Student_add:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x1920+0+0")
        # self.root.iconbitmap("img/title_logo.png")
        self.root.title("STUDENT DETAIL ")

#=================variables=================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_subject=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
       
        

#=================title=================s
        header = Label(root,text="STUDENT DETAIL",bg="white",fg="purple",font=("verdana", 36,"bold"))
        header.pack(fill=X)

        # t_img=Image.open("img/title_l")
        # t_img=t_img.resize((96,96), Image.Resampling.LANCZOS)
        # self.title_img = ImageTk.PhotoImage(t_img) 
        # title_img_Label=Label(header,image = self.title_img,bg="white")
        # title_img_Label.pack(side=LEFT,padx=20,pady=5)



        main_frame=Frame(bd=2,bg="white")
        main_frame.place(x=10,y=130,width=1346,height=494)

 #=================left lable frame=================
        left_frame=LabelFrame(main_frame,bd=2,bg='white', relief= RIDGE,fg="purple",text="Student Details",font=("comicsansns",12,"italic"))
        left_frame.place(x=10,y=10,width=570,height=375)


        left_inside_frame=Frame(left_frame,bd=4,bg='white')
        left_inside_frame.place(x=0,y=10,width=565,height=300)

#=================Enrollment Number=================
        attendaceID_lable=Label(left_inside_frame,text="Enrollment No.",font=("comicsansns",14,"italic"),fg="purple",bg="white")
        attendaceID_lable.grid(row=0,column=0,pady=5,sticky=W)

        attendaceID_entry=ttk.Entry(left_inside_frame,width=16,textvariable=self.var_atten_id,font=("comicsansns",12,"italic"))
        attendaceID_entry.grid(row=0,column=1,pady=5,padx=20,sticky=W)

#=================Rollno=================
        rollLable=Label(left_inside_frame,text="RollNo",font=("comicsansns",14,"italic"),fg="purple",bg="white")
        rollLable.grid(row=1,column=0,pady=8,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,width=16,textvariable=self.var_atten_roll,font=("comicsansns",12,"italic"))
        atten_roll.grid(row=1,column=1,pady=8,padx=20,sticky=W)

#=================Name=================
        nameLable=Label(left_inside_frame,text="Name",font=("comicsansns",14,"italic"),fg="purple",bg="white")
        nameLable.grid(row=2,column=0,pady=8,sticky=W)

        atten_nam=ttk.Entry(left_inside_frame,width=16,textvariable=self.var_atten_name,font=("comicsansns",12,"italic"))
        atten_nam.grid(row=2,column=1,pady=8,padx=20,sticky=W)

#=================Department=================
        depLable=Label(left_inside_frame,text="Department",font=("comicsansns",14,"italic"),fg="purple",bg="white")
        depLable.grid(row=3,column=0,pady=8,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=16,textvariable=self.var_atten_dep,font=("comicsansns",12,"italic"))
        atten_dep.grid(row=3,column=1,pady=8,padx=20,sticky=W)
#=================Subject=================
        subjectLable=Label(left_inside_frame,text="Subject",font=("comicsansns",14,"italic"),fg="purple",bg="white")
        subjectLable.grid(row=4,column=0,pady=8,sticky=W)

        atten_subject=ttk.Entry(left_inside_frame,width=16,textvariable=self.var_atten_subject,font=("comicsansns",12,"italic"))
        atten_subject.grid(row=4,column=1,pady=8,padx=20,sticky=W)

#=================Date=================
        dateLable=Label(left_inside_frame,text="Date",font=("comicsansns",14,"italic"),fg="purple",bg="white")
        dateLable.grid(row=5,column=0,pady=8,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=16,textvariable=self.var_atten_date,font=("comicsansns",12,"italic"))
        atten_date.grid(row=5,column=1,pady=8,padx=20,sticky=W)


#=================button frames=================

        btn_frame=Frame(left_frame,bd=2,bg='white')
        btn_frame.place(x=50,y=300,width=500,height=30)

        save_btn=Button(btn_frame,text="Save",command=self.add_students,width=13,font=("comicsansns",11,"italic"),bg="purple",fg="white")
        save_btn.grid(row=0,column=0,padx=5)

        update_btn=Button(btn_frame,text="Update",command=self.update_student,width=13,font=("comicsansns",11,"italic"),bg="purple",fg="white")
        update_btn.grid(row=0,column=1,padx=5)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("comicsansns",11,"italic"),bg="purple",fg="white")
        reset_btn.grid(row=0,column=3,padx=8)


#=================RIGHT lable frame=================
        right_frame=LabelFrame(main_frame,bd=2,bg='white', fg="purple",relief= RIDGE,text="Attendance Details",font=("comicsansns",12,"italic"))
        right_frame.place(x=590,y=10,width=740,height=470)
        

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=720,height=430)

# ========================Scrollbar=========================

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","subject","date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Enrollment No")
        self.AttendanceReportTable.heading("roll",text="RollNo")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("subject",text="Subject")
        self.AttendanceReportTable.heading("date",text="Date")

        self.AttendanceReportTable["show"]="headings"

        

        self.AttendanceReportTable.column("id",width=110)
        self.AttendanceReportTable.column("roll",width=110)
        self.AttendanceReportTable.column("name",width=110)
        self.AttendanceReportTable.column("department",width=110)
        self.AttendanceReportTable.column("subject",width=110)
        self.AttendanceReportTable.column("date",width=110)
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease-1>",self.get_cursor)

# ======================== fetch data =========================

    def fetch_data(self):
                
        con=mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="attendance")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for row in rows:
                self.AttendanceReportTable.insert('',END,values=row)
        con.commit()
        con.close()

#import csv.........................
       
    def add_students(self):
                if self.var_atten_roll.get()=="":
                                messagebox.showerror("Error","All fields are required!!!")
                                
                else:
                        con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="",database="attendance")
                        cur=con.cursor()
                        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.var_atten_id.get(),
                                                                                        self.var_atten_roll.get(),
                                                                                        self.var_atten_name.get(),
                                                                                        self.var_atten_dep.get(),
                                                                                        self.var_atten_subject.get(),
                                                                                        self.var_atten_date.get(),
                                                                                        self.var_atten_attendance.get()))
                        con.commit()
                        self.fetch_data()
                        con.close()
                        messagebox.showinfo("sucess","record has been inserted")



                

#export csv...................

    def update_student(self):

        if self.var_atten_roll.get()=="":
               messagebox.showerror("Error","All fields are required!!!")
        else:
                con=mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="attendance")
                cur=con.cursor()
                cur.execute("update students set Enrollment_No=%s,Name=%s,Department=%s,Subject=%s,Date=%s,Status=%s where RollNo=%s",(self.var_atten_id.get(),
                                                                                                                                        self.var_atten_name.get(),
                                                                                                                                        self.var_atten_dep.get(),
                                                                                                                                        self.var_atten_subject.get(),
                                                                                                                                        self.var_atten_date.get(),
                                                                                                                                        self.var_atten_attendance.get(),
                                                                                                                                        self.var_atten_roll.get()))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("sucess","record has been updated")
                
     

    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         contents=self.AttendanceReportTable.item(cursor_row)
         row=contents['values']
         self.var_atten_id.set(row[0])
         self.var_atten_roll.set(row[1])
         self.var_atten_name.set(row[2])
         self.var_atten_dep.set(row[3])
         self.var_atten_subject.set(row[4])
         self.var_atten_date.set(row[5])
         self.var_atten_attendance.set(row[6])


    def reset_data(self):
         self.var_atten_id.set("")
         self.var_atten_roll.set("")
         self.var_atten_name.set("")
         self.var_atten_dep.set("")
         self.var_atten_subject.set("")
         self.var_atten_date.set("")
         self.var_atten_attendance.set("")


 
if __name__=="__main__":
    root=Tk()
    obj=Student_add(root)
    root.mainloop() 