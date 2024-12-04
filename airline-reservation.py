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


def update_info():
    psngr_id = int(input('Enter passenger ticket no. : '))
    change = input("Update -- Name(n) - Class(c) - Flight date(d) - boarding(b) - Landing(l) : ")
    if change == "n" :
        new_name = input("Enter new name: ")
        data = (new_name, psngr_id)
        query = 'update psngr_list set name = %s where id=%s'
    elif change == "c":
        new_class = input("Enter new class: ")
        data = (new_class,psngr_id)
        query = 'replace class where id=%s as %s'
    elif change == "d":
        new_fdate = input("Enter new date")
        data = (new_fdate, psngr_id)
        query = 'replace flightDate where id=%s as %s'
    elif change == "b":
        new_boarding = input("Enter new boarding location: ")
        data = (new_boarding, psngr_id)
        query = 'replace name where id=%s as %s'
    elif change == "l":
        new_landing = input("Enter new landing location: ")
        data = (new_landing, psngr_id)
        query = 'replace name where id=%s as %s'
    else:
        print("Invalid Input")
    
    mycur.execute(query,data)
    mydb.commit()

def display():

    def dis_psngr():

        def idSubmit():
            dis_id = (idEntry.get(),)
            query = "Select * from psngr_list where id = %s"
            mycur.execute(query,dis_id)   
            data = mycur.fetchall()
            v = []
            n = 0
            y = 0.3
            details_arr = ['ID : ','Name : ','Class : ','Date : ','Fly from : ','Fly to : ']
            for x in data:
                v.append(x)
            for i in v:
                for j in i:
                    Label1 = Label(display_window,text=(('{} {}').format(details_arr[n],j)),font=('Ariel',16),width=50)
                    Label1.place(relx=0.12,rely=y)
                    y += 0.07
                    n += 1
            

        ask_id = Label(display_window,text='Enter ID of passenger : ')
        idEntry = Entry(display_window)
        chkIdBtn = Button(display_window,text='Continue',command=idSubmit)


        ask_id.grid(row=3,column=1)
        idEntry.grid(row=3,column=2)
        chkIdBtn.grid(row=4,column=1)


    def dispall():

        query = "Select * from psngr_list"
        mycur.execute(query)   
        data = mycur.fetchall()
        v = []
        n = 0
        y = 0.3
        for x in data:
            v.append(x)
        for i in v:
                Label1 = Label(display_window,text=(('{} - {}').format(n+1,i)),font=('Ariel',12))
                Label1.place(relx=0.17,rely=y)
                y += 0.07
                n += 1
               

        

    display_window = Toplevel()

    display_window.title('Check details')
    display_window.geometry('800x400')

    chkAllBtn = Button(display_window,text='All Passengers details',command=dispall)
    chkBtn = Button(display_window,text='Check Passenger details',command=dis_psngr)

    chkAllBtn.grid(row=1,column=1)
    chkBtn.grid(row=1,column=2)

    display_window.mainloop()

def main():
    window = Tk()

    window.title('Indian Airlines')
    window.geometry('430x340')

    entryBtn = Button(window,text='Add Passenger Data',command=psngr_entry,width=20,height=2)
    displayBtn = Button(window,text='Check deatils',command=display,width=20,height=2)
    updateBtn = Button(window,text='Update Info',command=display,width=20,height=2)
    About = Button(window,text='More Info',command=display,width=20,height=2)

    entryBtn.place(relx=0.10,rely=0.1)
    displayBtn.place(relx=0.54,rely=0.1)
    updateBtn.place(relx=0.10,rely=0.25)
    About.place(relx=0.54,rely=0.25)

    window.mainloop()

main()