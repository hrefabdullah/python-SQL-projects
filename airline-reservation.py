from tkinter import *
import mysql.connector as sqlcon
import random as rdm

mydb = sqlcon.connect(host='localhost',user='root', passwd='1725', database='air_reservation')
mycur = mydb.cursor()

# mycur.execute('create database air_reservation')
# mycur.execute(' create table psngr_list(id INT PRIMARY KEY,name VARCHAR(50),class VARCHAR(20), flightDate DATE, Fly_from VARCHAR(20), Fly_to VARCHAR(20))')

def psngr_entry():

    entry_window = Toplevel()
    entry_window.title('Passenger Entry')
    entry_window.geometry('420x340')

    id_label = Label(entry_window,text='Passenger id')
    pid = Entry(entry_window)
    # name_label = Label(entry_window,text='Name')
    # pname = Entry(entry_window)
    

    id_label.grid(row=0,column=0)
    pid.grid(row=0,column=1)
    # name_label.grid(row=1,column=0)
    # pname.grid(row=1,column=1)

    id_ = int(input("Enter Aadhar Number: "))
    name = input("Enter Full Name: ")
    class_ = input('Ticket (Economy/Business/Luxury) : ')
    f_date = input("Enter flight date:")
    from_ = input("Fly from: ")
    to_ = input("Fly to: ")
    details = (id_,name,class_,f_date,from_,to_)

    def submit():
        query = 'insert into psngr_list(id,name,class,flightDate,Fly_from,Fly_to) values(%s,%s,%s,%s,%s,%s)'
        mycur.execute(query,details)
        mydb.commit()

    entry_window.mainloop()
def dispall():
    
    query = "Select * from psngr_list"
    mycursor.execute(query)   
    data = mycursor.fetchall()
    print("The passenger details are as follows : ")
    for x in data:
        print(x)
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
def dis_psngr():
    dis_id = int(input("Enter id of passenger: "))
    query = "Select * from psngr_list where id = %s"
    mycursor.execute(query,dis_id)   
    data = mycursor.fetchall()
    print("The passenger details are as follows : ")
    for x in data:
        print(x)

window = Tk()

window.title('Indian Airlines')
window.geometry('420x340')

Entry = Button(window,text='Add Passenger Data',command=psngr_entry)

Entry.grid(row=1,columnspan=1)

window.mainloop()