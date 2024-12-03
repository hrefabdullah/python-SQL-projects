from tkinter import *
from tkinter import messagebox
import mysql.connector as sqlcon
import random as rdm

mydb = sqlcon.connect(host='localhost',user='root', passwd='1725', database='air_reservation')
mycur = mydb.cursor()

# mycur.execute('create database air_reservation')
# mycur.execute(' create table psngr_list(id INT PRIMARY KEY,name VARCHAR(50),class VARCHAR(20), flightDate DATE, Fly_from VARCHAR(20), Fly_to VARCHAR(20))')

def psngr_entry(): 

    def submit():

        id_ = pid.get()
        name = pname.get()
        class_ = pClass.get()
        f_date = pDate.get()
        from_ = pfrom.get()
        to_ = pto.get()
        details = (id_,name,class_,f_date,from_,to_)


        query = 'insert into psngr_list(id,name,class,flightDate,Fly_from,Fly_to) values(%s,%s,%s,%s,%s,%s)'
        mycur.execute(query,details)
        mydb.commit()

        messagebox.showinfo('Submitted','Passenger details are saved')
    def destroy():
        entry_window.destroy()

    entry_window = Toplevel()
    entry_window.title('Passenger Entry')
    entry_window.geometry('420x340')

    id_label = Label(entry_window,text='Passenger ID')
    pid = Entry(entry_window)
    name_label = Label(entry_window,text='Name')
    pname = Entry(entry_window)
    class_label = Label(entry_window,text='Class')
    pClass = Entry(entry_window)
    date_label = Label(entry_window,text='Flight date')
    pDate = Entry(entry_window)
    flyFrom_label = Label(entry_window,text='Fly from')
    pfrom = Entry(entry_window)
    flyto_label = Label(entry_window,text='Fly to')
    pto = Entry(entry_window)
    sbmtBtn = Button(entry_window,text='Submit',command=submit)
    mainMenuBtn = Button(entry_window,text='Main Menu',command=main)
    cancelBtn = Button(entry_window,text='Cancel',command=destroy)
    

    id_label.grid(row=1,column=1)
    pid.grid(row=1,column=2)
    name_label.grid(row=2,column=1)
    pname.grid(row=2,column=2)
    class_label.grid(row=3, column=1)
    pClass.grid(row=3,column=2)
    date_label.grid(row=4,column=1)
    pDate.grid(row=4,column=2)
    flyFrom_label.grid(row=5,column=1)
    pfrom.grid(row=5,column=2)
    flyto_label.grid(row=6,column=1)
    pto.grid(row=6,column=2)
    sbmtBtn.grid(row=8,column=1)
    mainMenuBtn.grid(row=8,column=2)
    cancelBtn.grid(row=8,column=3)


    
    entry_window.mainloop()

    dis_id = int(input("Enter id of passenger: "))
    query = "Select * from psngr_list where id = %s"
    mycursor.execute(query,dis_id)   
    data = mycursor.fetchall()
    print("The passenger details are as follows : ")
    for x in data:
        print(x)

def main():
    window = Tk()

    window.title('Indian Airlines')
    window.geometry('420x340')

    entryBtn = Button(window,text='Add Passenger Data',command=psngr_entry)

    entryBtn.grid(row=1,columnspan=1)

    window.mainloop()

main()