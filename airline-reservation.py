# Import all necessary libararies
from tkinter import *
from tkinter import messagebox
import mysql.connector as sqlcon

# Set up connection with mySQL local server
mydb = sqlcon.connect(host='localhost',user='root', passwd='1725', database='air_reservation') #database must be written after executing code on line 11
mycur = mydb.cursor()

# mycur.execute('create database air_reservation') - only once
# mycur.execute(' create table psngr_list(id INT PRIMARY KEY,name VARCHAR(48),class VARCHAR(20), flightDate DATE, Fly_from VARCHAR(20), Fly_to VARCHAR(20))') - only once

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
    entry_window.geometry('420x440')
    entry_window.configure(bg='#e1e3e1')

    pForm = Label(entry_window,text='Passenger Entry Form',font=('ariel',14),bg='#e1e3e1')
    id_label = Label(entry_window,text='Passenger ID : ',font=('ariel',11),bg='#e1e3e1')
    pid = Entry(entry_window)
    name_label = Label(entry_window,text='Full Name : ',font=('ariel',11),bg='#e1e3e1')
    pname = Entry(entry_window)
    class_label = Label(entry_window,text='Ticket Class : ',font=('ariel',11),bg='#e1e3e1')
    pClass = Entry(entry_window)
    date_label = Label(entry_window,text='Flight date : ',font=('ariel',11),bg='#e1e3e1')
    pDate = Entry(entry_window)
    flyFrom_label = Label(entry_window,text='Fly from : ',font=('ariel',11),bg='#e1e3e1')
    pfrom = Entry(entry_window)
    flyto_label = Label(entry_window,text='Fly to : ',font=('ariel',11),bg='#e1e3e1')
    pto = Entry(entry_window)
    sbmtBtn = Button(entry_window,text='Submit',command=submit,width=11)
    cancelBtn = Button(entry_window,text='Exit',command=destroy,width=11)
    
    pForm.place(relx=0.27,rely=0.05)
    id_label.place(relx=0.23,rely=0.20)
    pid.place(relx=0.48,rely=0.20)
    name_label.place(relx=0.23,rely=0.30)
    pname.place(relx=0.48,rely=0.30)
    class_label.place(relx=0.23,rely=0.40)
    pClass.place(relx=0.48,rely=0.40)
    date_label.place(relx=0.23,rely=0.50)
    pDate.place(relx=0.48,rely=0.50)
    flyFrom_label.place(relx=0.23,rely=0.60)
    pfrom.place(relx=0.48,rely=0.60)
    flyto_label.place(relx=0.23,rely=0.70)
    pto.place(relx=0.48,rely=0.70)
    sbmtBtn.place(relx=0.28,rely=0.85)
    cancelBtn.place(relx=0.52,rely=0.85)


    
    entry_window.mainloop()

def update_info():

    def fDateUpdate():

        def confirmDUpdate():
            psngr_entry = uID_entry.get()
            update = uEntry.get()
            query = 'update psngr_list set flightDate = %s where id = %s'
            data = (update,psngr_entry)
            mycur.execute(query,data)
            mydb.commit()

            query = "Select * from psngr_list where id = %s"
            mycur.execute(query,(psngr_entry,))
            data = mycur.fetchall()
            v = []
            n = 0
            y = 0.48
            details_arr = ['ID : ','Name : ','Class : ','Date : ','Fly from : ','Fly to : ']
            for x in data:
                v.append(x)
            for i in v:
                for j in i:
                    Label1 = Label(update_window,text=(('{} {}').format(details_arr[n],j)),font=('Ariel',14),width=30,bg='#e1e3e1')
                    Label1.place(relx=0.1,rely=y)
                    y += 0.06
                    n += 1

            
        uID = Label(update_window,text='Enter the ID of Passenger             : ',font=('ariel',10),bg='#e1e3e1')
        uID_entry = Entry(update_window)
        uLabel = Label(update_window,text='Enter New date                     : ',font=('ariel',10),bg='#e1e3e1')
        uEntry = Entry(update_window)
        confirmUpdate = Button(update_window,text='Confirm',command=confirmDUpdate)



        uID.place(relx=0.1,rely=0.22)
        uID_entry.place(relx=0.5,rely=0.22)
        uLabel.place(relx=0.1,rely=0.28)
        uEntry.place(relx=0.5,rely=0.28)
        confirmUpdate.place(relx=0.1,rely=0.35)

    def classUpdate():

        def confirmCUpdate():
            psngr_entry = uID_entry.get()
            update = uEntry.get()
            query = 'update psngr_list set class = %s where id = %s'
            data = (update,psngr_entry)
            mycur.execute(query,data)
            mydb.commit()

            query = "Select * from psngr_list where id = %s"
            mycur.execute(query,(psngr_entry,))
            data = mycur.fetchall()
            v = []
            n = 0
            y = 0.48
            details_arr = ['ID : ','Name : ','Class : ','Date : ','Fly from : ','Fly to : ']
            for x in data:
                v.append(x)
            for i in v:
                for j in i:
                    Label1 = Label(update_window,text=(('{} {}').format(details_arr[n],j)),font=('Ariel',14),width=30,bg='#e1e3e1')
                    Label1.place(relx=0.1,rely=y)
                    y += 0.06
                    n += 1

            
        uID = Label(update_window,text='Enter the ID of Passenger                  : ',font=('ariel',10),bg='#e1e3e1')
        uID_entry = Entry(update_window)
        uLabel = Label(update_window,text='Enter updated class                     : ',font=('ariel',10),bg='#e1e3e1')
        uEntry = Entry(update_window)
        confirmUpdate = Button(update_window,text='Confirm',command=confirmCUpdate)


        uID.place(relx=0.1,rely=0.22)
        uID_entry.place(relx=0.5,rely=0.22)
        uLabel.place(relx=0.1,rely=0.28)
        uEntry.place(relx=0.5,rely=0.28)
        confirmUpdate.place(relx=0.1,rely=0.35)

    def boardingUpdate():

        def confirmffUpdate():
            psngr_entry = uID_entry.get()
            update = uEntry.get()
            query = 'update psngr_list set Fly_from = %s where id = %s'
            data = (update,psngr_entry)
            mycur.execute(query,data)
            mydb.commit()

            query = "Select * from psngr_list where id = %s"
            mycur.execute(query,(psngr_entry,))
            data = mycur.fetchall()
            v = []
            n = 0
            y = 0.48
            details_arr = ['ID : ','Name : ','Class : ','Date : ','Fly from : ','Fly to : ']
            for x in data:
                v.append(x)
            for i in v:
                for j in i:
                    Label1 = Label(update_window,text=(('{} {}').format(details_arr[n],j)),font=('Ariel',14),width=30,bg='#e1e3e1')
                    Label1.place(relx=0.1,rely=y)
                    y += 0.06
                    n += 1


            
        uID = Label(update_window,text='Enter the ID of Passenger                  : ',font=('ariel',10),bg='#e1e3e1')
        uID_entry = Entry(update_window)
        uLabel = Label(update_window,text='Fly from                                : ',font=('ariel',10),bg='#e1e3e1')
        uEntry = Entry(update_window)
        confirmUpdate = Button(update_window,text='Confirm',command=confirmffUpdate)


        uID.place(relx=0.1,rely=0.22)
        uID_entry.place(relx=0.5,rely=0.22)
        uLabel.place(relx=0.1,rely=0.28)
        uEntry.place(relx=0.5,rely=0.28)
        confirmUpdate.place(relx=0.1,rely=0.35)

    def landingUpdate():

        def confirmftUpdate():
            psngr_entry = uID_entry.get()
            update = uEntry.get()
            query = 'update psngr_list set Fly_to = %s where id = %s'
            data = (update,psngr_entry)
            mycur.execute(query,data)
            mydb.commit()

            query = "Select * from psngr_list where id = %s"
            mycur.execute(query,(psngr_entry,))
            data = mycur.fetchall()
            v = []
            n = 0
            y = 0.48
            details_arr = ['ID : ','Name : ','Class : ','Date : ','Fly from : ','Fly to : ']
            for x in data:
                v.append(x)
            for i in v:
                for j in i:
                    Label1 = Label(update_window,text=(('{} {}').format(details_arr[n],j)),font=('Ariel',14),width=30,bg='#e1e3e1')
                    Label1.place(relx=0.1,rely=y)
                    y += 0.06
                    n += 1

            



            # if mycur.rowcount>0:
            #     messagebox.showinfo('Updated','Landing place has been updated')

            
        uID = Label(update_window,text='Enter the ID of Passenger                   : ',font=('ariel',10),bg='#e1e3e1')
        uID_entry = Entry(update_window)
        uLabel = Label(update_window,text='Fly to                                   : ',font=('ariel',10),bg='#e1e3e1',)
        uEntry = Entry(update_window)
        confirmUpdate = Button(update_window,text='Confirm',command=confirmftUpdate)


        uID.place(relx=0.1,rely=0.22)
        uID_entry.place(relx=0.5,rely=0.22)
        uLabel.place(relx=0.1,rely=0.28)
        uEntry.place(relx=0.5,rely=0.28)
        confirmUpdate.place(relx=0.1,rely=0.35)

    def destroyUpdate():
        update_window.destroy()

    update_window = Toplevel()
    update_window.title('Update Information')
    update_window.geometry('440x540')
    update_window.config(bg='#e1e3e1')

    updateLabel = Label(update_window,text='What would you like to Update? ',font=('ariel',14),bg='#e1e3e1')
    fDateBtn = Button(update_window,text='Flight Date',width=10,command=fDateUpdate)
    classBtn = Button(update_window,text='Ticket Class',width=10,command=classUpdate)
    boardingBtn = Button(update_window,text='Boarding',width=10,command=boardingUpdate)
    landingBtn = Button(update_window,text='Landing',width=10,command=landingUpdate)
    uExitBtn = Button(update_window,text='Exit',width=10,command=destroyUpdate)

    updateLabel.place(relx=0.2,rely=0.05)
    fDateBtn.place(relx=0.08,rely=0.14)
    classBtn.place(relx=0.31,rely=0.14)
    boardingBtn.place(relx=0.53,rely=0.14)
    landingBtn.place(relx=0.74,rely=0.14)
    uExitBtn.place(relx=0.4,rely=0.9)

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
                    Label1 = Label(display_window,text=(('{} {}').format(details_arr[n],j)),font=('Ariel',16),width=50,bg='#e1e3e1')
                    Label1.place(relx=0.12,rely=y)
                    y += 0.07
                    n += 1
            spaceLabel = Label(display_window,text='--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',width=90,pady=10,bg='#e1e3e1')
            spaceLabel.place(relx=0.10,rely=0.72)
            spaceLabel1 = Label(display_window,text='---------------------------------------------------------------------------------------------------------------',width=70,pady=10,bg='#e1e3e1')
            spaceLabel1.place(relx=0.25,rely=0.99)
            spaceLabel2 = Label(display_window,text='-----------------------------------------------------------------------------------',width=70,pady=10,bg='#e1e3e1')
            spaceLabel2.place(relx=0.25,rely=1.037)
            spaceLabel3 = Label(display_window,text='-----------------------------------------------------------------------------------',width=70,pady=10,bg='#e1e3e1')
            spaceLabel3.place(relx=0.25,rely=1.23)

        ask_id = Label(display_window,text='Enter ID of passenger : ',font=('ariel',12),bg='#e1e3e1')
        idEntry = Entry(display_window,width=23)
        chkIdBtn = Button(display_window,text='Continue',command=idSubmit)


        ask_id.place(relx=0.03,rely=0.097)
        idEntry.place(relx=0.26,rely=0.1)
        chkIdBtn.place(relx=0.03,rely=0.17)


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
                Label1 = Label(display_window,text=(('{} - {}').format(n+1,i)),font=('Ariel',12),bg='#e1e3e1')
                Label1.place(relx=0.17,rely=y)
                y += 0.07
                n += 1
               
    def destroyDis():
        display_window.destroy()
        

    display_window = Toplevel()

    display_window.title('Check details')
    display_window.geometry('800x400')
    display_window.config(bg='#e1e3e1')

    chkAllBtn = Button(display_window,text='All Passengers details',command=dispall,font=('ariel',10))
    chkBtn = Button(display_window,text='Check Passenger details',command=dis_psngr,font=('ariel',10))
    exitBtn = Button(display_window,text='Exit',command=destroyDis,font=('ariel',10))

    chkAllBtn.grid(row=1,column=1)
    chkBtn.grid(row=1,column=2)
    exitBtn.grid(row=1,column=3)

    display_window.mainloop()

def deleteInfo():

    def exitDeletion():
        delete_window.destroy()

    def checkID():
        passId = dID_entry.get()
        queryDisp = "Select * from psngr_list where id = %s"
        mycur.execute(queryDisp,(passId,))
        data1 = mycur.fetchall()
        v = []
        n = 0
        y = 0.38
        details_arr = ['ID : ','Name : ','Class : ','Date : ','Fly from : ','Fly to : ']
        for x in data1:
            v.append(x)
            for i in v:
                for j in i:
                    Label1 = Label(delete_window,text=(('{} {}').format(details_arr[n],j)),font=('Ariel',14),width=30,bg='#e1e3e1')
                    Label1.place(relx=0.1,rely=y)
                    y += 0.06
                    n += 1
        

    def ConfirmDelete():
        passId = dID_entry.get()
        query = 'Delete from psngr_list where id=%s'
        mycur.execute(query,(passId,))
        mydb.commit()
        messagebox.showinfo('Removed','Deleted info successfully')

    delete_window = Toplevel()
    delete_window.title('Delete information')
    delete_window.geometry('440x440')
    delete_window.config(bg='#e1e3e1')

    deleteTitle = Label(delete_window,text="Delete Infomation",font=('ariel',14,'bold'),bg='#e1e3e1')
    dID = Label(delete_window,text='Enter the ID of Passenger : ',font=('ariel',10),bg='#e1e3e1')
    dID_entry = Entry(delete_window)
    checkId = Button(delete_window,text='check',command=checkID)
    deleteExit = Button(delete_window, text='Exit',command=exitDeletion)
    deletionBtn = Button(delete_window, text='Delete',command=ConfirmDelete)


    deleteTitle.place(relx=0.33,rely=0.07)
    dID.place(relx=0.08,rely=0.2)
    dID_entry.place(relx=0.47,rely=0.2)
    checkId.place(relx=0.78,rely=0.189)
    deleteExit.place(relx=0.50,rely=0.80)
    deletionBtn.place(relx=0.40,rely=0.8)


def main():
    window = Tk()

    def exit_():
        window.destroy()

    window.title('Indian Airlines')
    window.geometry('480x400')
    window.config(bg='#e1e3e1')

    titleLabel = Label(window,text='Airline Reservation Server',font=('Ariel',22,'bold'),bg='#e1e3e1')
    tagLabel = Label(window,text='A Database for all International or Domestic flights',font=('Ariel',9),bg='#e1e3e1')
    entryBtn = Button(window,text='Add Passenger Data',font=('Ariel',10),command=psngr_entry,width=20,height=2)
    displayBtn = Button(window,text='Check deatils',font=('Ariel',10),command=display,width=20,height=2)
    updateBtn = Button(window,text='Update Info',font=('Ariel',10),command=update_info,width=20,height=2)
    Exit = Button(window,text='Exit',font=('Ariel',10),command=exit_,width=20,height=2)
    copyrightLabel = Label(window,text='Copyright © 2024 Abdullah',bg='#e1e3e1',font=('ariel',9))
    deleteBtn = Button(window, text="Delete Info",font=('Ariel',10),command=deleteInfo,width=20,height=2)

    titleLabel.place(relx=0.12,rely=0.1)
    tagLabel.place(relx=0.2,rely=0.21)
    entryBtn.place(relx=0.1,rely=0.4)
    displayBtn.place(relx=0.55,rely=0.4)
    updateBtn.place(relx=0.1,rely=0.55)
    deleteBtn.place(relx=0.55,rely=0.55)
    Exit.place(relx=0.3, rely=0.7)
    copyrightLabel.place(relx=0.03,rely=0.9)

    window.mainloop()



main()