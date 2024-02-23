from datetime import datetime
from tkinter import *
from tkinter import OptionMenu
import tkinter as tk
import sqlite3
from tkcalendar import Calendar

# DATABASE SECTION
crc = sqlite3.connect("student_info.db")
crc.execute('''CREATE TABLE IF NOT EXISTS student_data(
                Reg_Num varchar(20) PRIMARY KEY,
                Name varchar(20) NOT NULL,
                Department varchar(7),
                Section varchar(5),
                Gender varchar(6),
                Date_of_birth DATE);
            ''')
insertdata = '''INSERT INTO student_data VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');'''
showdata = '''SELECT * FROM student_data;'''

def show_data():
    result = crc.execute(showdata)
    result_win = Toplevel(root)
    result_win.geometry("1000x500")
    result_win['background']="#F0E9E8"
    i = 0
    for student in result:
        for j in range(len(student)):
            e = Entry(result_win, width=20, fg='black')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i+1

# UI SECTION
def label_data():
    name1 = t1.get()
    reg_num1 = t2.get()
    section1 = t4.get()
    return name1, reg_num1, section1
    
def dropdown_data():
    department1 = clicked.get()
    return department1
    
def gender_choice():
    gender1=""
    if(radio.get()==1):
        gender1="Male"
    elif(radio.get()==2):
        gender1="Female"
    elif(radio.get()==3):
        gender1="Other"
    return gender1
    
def dob_data():
    dob_str = cal.get_date()
    dob_dt = datetime.strptime(dob_str, "%m/%d/%y")
    dob_date = dob_dt.date()
    return dob_date
    
def insert_data():
    name1, reg_num1, section1 = label_data()
    department1 = dropdown_data()
    gender1 = gender_choice()
    dob_date = dob_data()
    insertdata_formatted = insertdata.format(reg_num1, name1, department1, section1, gender1, dob_date)
    crc.execute(insertdata_formatted)
    crc.commit()

root=tk.Tk()
root.title("Student Data Retriever")
root.geometry("1000x500")
root['background']='#F0E9E8'
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

l1=tk.Label(root,text="Enter your name: ",width=20,anchor=W)
l1.grid(row=0,padx=(10,0))
t1=tk.Entry(root)
t1.grid(row=0,column=1)

l2=tk.Label(root,text="Enter your Reg Num: ",width=20,anchor=W)
l2.grid(row=1,padx=(10,0))
t2=tk.Entry(root)
t2.grid(row=1,column=1)

l3=tk.Label(root,text="Enter your Department: ",width=20,anchor=W)
l3.grid(row=2,padx=(10,0))

options=["CTECH","CINTEL","EEE","OTHER"]

clicked=StringVar()
clicked.set("Department")

t3=OptionMenu(root, clicked,*options)
t3.grid(row=2,column=1)

l4=tk.Label(root,text="Enter your Gender: ",width=20,anchor=W)
l4.grid(row=6,padx=(10,0))

radio=IntVar()

rb1=Radiobutton(root,text="Male",variable=radio,value=1)
rb1.grid(row=6,column=1,sticky="W")

rb2=Radiobutton(root,text="Female",variable=radio,value=2)
rb2.grid(row=7,column=1,sticky="W")

rb3=Radiobutton(root,text="Other",variable=radio,value=3)
rb3.grid(row=8,column=1,sticky="W")

l4=tk.Label(root,text="Enter your DOB: ")
l4.grid(row=0,column=4)

cal=Calendar(root,selectmode="day",year=2023,month=1,day=1)
cal.grid(row=1,column=5)

l5=tk.Label(root,text="Enter your Section: ")
l5.grid(row=2,column=4)

t4=tk.Entry(root)
t4.grid(row=2,column=5)

b1 = tk.Button(root, text="Enter Data", command=insert_data,width=20)
b1.grid(row=8,column=5)

b2 = tk.Button(root, text="Show Table",command=show_data,width=20)
b2.grid(row=8,column=8)

root.mainloop()