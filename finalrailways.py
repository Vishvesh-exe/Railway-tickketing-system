import tkinter as tk
from typing import List
import pyodbc
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from PIL import ImageTk,Image

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=(LocalDb)\MSSQLLocalDB;"
    "Database=test;"
    "Trusted_Connection=yes;"
)

def inquire():
    def last_exit():
        messagebox.showinfo("Checked!!","Thank you!!")
    def search():
        originn=origin_id.get()
        destinationn=destination_id.get()
        type=type_id.get()
        date=date_id.get()
        nooftickets=nooftickets_id.get()
        # origin_id.set("")
        # destination_id.set("")
        curr_search=conn.cursor()
        s1="select train.train_id,Time from train,weekly_schedule where From_place='%s'and To_place='%s' and type='%s' and DateofJourney='%s' and train.train_id=weekly_schedule.train_id "%(originn,destinationn,type,date)
        curr_search.execute(s1)
        count1=0
        anss=0
        name_id=0
        timee=0
        depart_time=0
        for i in curr_search:
            count1+=1
            anss=list(i)
            name_id=anss[0]
            timee=anss[1]
        if count1>0:
            root5.destroy()
            root6=Tk()
            root6.geometry('200x300')
            root6.title('Search results')
            curr_last=conn.cursor()
            curr_neww=conn.cursor()
            s2="select total_fare,train_name,train.train_id from train,fare where train.train_id=fare.train_id and train.train_id='%d'"%(name_id)
            s3="select departure_time from station where train_id='%d'"%(name_id)
            curr_last.execute(s2)
           
            for i in curr_last:
                checkk=list(i)
                fare_no=checkk[0]
                train_namee=checkk[1]
                train_idd=checkk[2]
                tot_fare=fare_no*nooftickets
                last_head1=Label(root6,text='Train Details').place(x=50,y=10)
                last_head2=Label(root6,text='Train Name-').place(x=10,y=40)
                last_head3=Label(root6,text='Train ID-').place(x=10,y=70)
                last_head4=Label(root6,text='Total Fare-').place(x=10,y=100)
                last_head5=Label(root6,text='Train Starting time-').place(x=10,y=130)
                last_head6=Label(root6,text=train_namee).place(x=100,y=40)
                last_head7=Label(root6,text=train_idd).place(x=100,y=70)
                last_head8=Label(root6,text=tot_fare).place(x=100,y=100)
                last_head9=Label(root6,text=timee).place(x=120,y=130)
                Button(root6,text='Done',borderwidth=4,command=last_exit).place(x=100,y=190)
            curr_last.close()
            curr_neww.execute(s3)
            for i in curr_neww:
                checkk_1=list(i)
                depart_time=checkk_1[0]
                last_head10=Label(root6,text="Train departure time-").place(x=10,y=160)
                last_head11=Label(root6,text=depart_time).place(x=130,y=160)

        else:
            messagebox.showinfo("Info","No trains available!!!")
            root5.destroy()
      
    
    def inquexit():
        messagebox.showinfo("Team login", "THANK YOU!!!")
        root5.destroy()



    
    root5=Tk()
    root5.geometry('400x500')
    root5.title('To search trains')
    origin_id=StringVar(root5)
    destination_id=StringVar(root5)
    type_id=StringVar(root5)
    date_id=StringVar(root5)
    nooftickets_id=IntVar(root5)
    headd1=Label(root5,text='Enter detials').place(x=150,y=20)
    headd=Label(root5,text='Enter origin').place(x=75,y=100)
    entry_1=Entry(root5,textvariable=origin_id).place(x=150,y=100)
    headd2=Label(root5,text='Enter destination').place(x=60,y=150)
    entry_2=Entry(root5,textvariable=destination_id).place(x=160,y=150)
    headd_3=Label(root5,text='Enter type').place(x=77,y=200)
    entry_3=Entry(root5,textvariable=type_id).place(x=150,y=200)
    headd_4=Label(root5,text='Enter date').place(x=77,y=250)
    entry_4=Entry(root5,textvariable=date_id).place(x=150,y=250)
    search_bu=Button(root5,text='SEARCH',borderwidth=4,command=search).place(x=130,y=350)
    headd_5=Label(root5,text="Enter no of tickets").place(x=55,y=300)
    entry_5=Entry(root5,textvariable=nooftickets_id).place(x=160,y=300)
    exit_bu=Button(root5,text='EXIT',borderwidth=4,command=inquexit).place(x=200,y=350)


root = tk.Tk()
root.geometry("600x600")
root.title("Input User Details")
img1=ImageTk.PhotoImage(Image.open(r"C:\Users\Sai Vishvesh\Downloads\Train1.png"))
mylabel=Label(root,image=img1)
mylabel.place(x=-3,y=0,relwidth=1,relheight=1)

def login():
    root3 = Tk()
    root3.geometry('400x250')

    head3 = Label(root3, text="PASSENGER login").place(x=120, y=50)
    head3_1 = Label(root3, text="Passenger ID").place(x=75, y=100)
    head3_2 = Label(root3, text="Password").place(x=75, y=150)

    def logininto():
        passenger_id = p_id.get()
        p_word = pass_word.get()
        p_id.set("")
        pass_word.set("")
        cur3=conn.cursor()
        s1="select id from user_reg where id='%s' and r_password='%s'" %(passenger_id,p_word)
        cur3.execute(s1)
        c=0  
        for i in cur3:
            ans=list(i)
            c+=1
        if c==1:
            messagebox.showinfo("User login", "successfully logged In")
            root3.destroy()
            root4 = Tk()
            root4.geometry('400x200')

            head4 = Label(root4, text="PASSENGER DETAIL").place(x=120, y=40)
            head4_1 = Label(root4, text=ans).place(x=175, y=80)
            fin_b=Button(root4,text='Search trains',borderwidth=4,command=inquire)
            fin_b.place(x=145,y=120)
        else:
            messagebox.showinfo("Invalid login", "Invalid credentials!")
            root3.destroy()
    def loginexit():
        messagebox.showinfo("User login", "THANK YOU!!!")
        root3.destroy()

    p_id = StringVar(root3)
    pass_word = StringVar(root3)

    entry3_1 = Entry(root3, textvariable=p_id).place(x=175, y=100)
    entry3_2 = Entry(root3, textvariable=pass_word, show='*').place(x=175, y=150)

    b3_1 = Button(root3, text="  LOGIN  ", borderwidth=4, command=logininto)
    b3_1.place(x=75, y=200)

    b3_2 = Button(root3, text="  EXIT  ", borderwidth=4, command=loginexit)
    b3_2.place(x=175, y=200)

    root3.mainloop()
def register():


    def exitt():
        messagebox.showinfo("THANK YOU FOR REGISTERING", "THANKS")
        root2.destroy()

    def passengerregister():

        a = passenger_id.get()
        b = password.get()
        cur_1 = conn.cursor()
        ins2 = "select * from user_reg where id= '%s' or r_password='%s'" %(a,b)
        cur_1.execute(ins2)
        count=0
        for i in cur_1:
            count+=1
        if count>0:
            messagebox.showinfo("Unsuccesfull", "Passenger ID or Passenger Name already exists! Try again")
            root2.destroy()
            return
        else:
            cur1=conn.cursor()
            ins="insert into user_reg(id,r_password) values('%s','%s')" %(a,b)
            cur1.execute(ins)
            conn.commit()
            passenger_id.set("")
            password.set("")
   

    root2 = Tk()
    root2.geometry('400x300')

    passenger_id = StringVar(root2)
    password = StringVar(root2)

    head2 = Label(root2,text="NEW PASSENGER REGISTRATION").place(x=110,y=50)
    head2_1 = Label(root2,text=" PASSENGER ID ").place(x=70,y=100)
    head2_2 = Label(root2,text=" PASSENGER PASSWORD ").place(x=30,y=150)

    entry2_1 = Entry(root2,textvariable = passenger_id).place(x=175,y=100)
    entry2_2 = Entry(root2,textvariable = password,show='*').place(x=175,y=150)

    b2_1 = Button(root2,text="Register",borderwidth = 4, command = passengerregister)
    b2_1.place(x=120,y=200)

    b2_2 = Button(root2,text="Exit",borderwidth = 4, command = exitt)
    b2_2.place(x=230, y=200)

    root2.mainloop()

def main_exit():
    messagebox.showinfo("Message","Thank you")
    root.destroy()


head1 = Label(root, text='For Passenger registration')
head1.place(x=155, y=255)

b1_1 = Button(root, text="Passenger regsitration", borderwidth=4, command=register)
b1_1.place(x=330, y=250)

headd1 = Label(root, text='For passenger Login')
headd1.place(x=170, y=305)

b1_2 = Button(root, text="Passenger Login", borderwidth=4, command=login)
b1_2.place(x=340, y=300)

b1_3 = Button(root, text="Exit", borderwidth=4, command=main_exit).place(x=270, y=370)

root.mainloop()
