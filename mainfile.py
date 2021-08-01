def addstudent():
    def submitadd():
        id = idval.get() 
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d-%m-%Y")
        try:
            strr = 'insert into studentdata2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel("Notification",'Added Successfully and Want to Clear Entries',parent=addroot)
            if res==True:
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            print('Error')
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry("470x470+220+200")
    addroot.title("Add Student")
    addroot.config(bg="red")
    addroot.iconbitmap("database.ico")
    addroot.resizable(False,False)
    '''Add Student Labels'''
    idlabel = Label(addroot,text="Enter Roll No :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text="Enter Name :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text="Mobile no :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    emaillabel = Label(addroot,text="Enter Email :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    adresslabel = Label(addroot,text="Enter Address :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    adresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text="Enter Gender :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text="Enter D.O.B :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    '''Entries'''
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    dobentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    ##add button
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground="orange",bg="red",command=submitadd)
    submitbtn.place(x=150,y=415)
    addroot.mainloop()

def searchstudent():
    def search():
        pass
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry("470x540+220+200")
    searchroot.title("Search Student")
    searchroot.config(bg="red")
    searchroot.iconbitmap("database.ico")
    searchroot.resizable(False,False)
    '''Search Student Labels'''
    idlabel = Label(searchroot,text="Enter Roll No :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text="Enter Name :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text="Mobile no :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    emaillabel = Label(searchroot,text="Enter Email :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    adresslabel = Label(searchroot,text="Enter Address :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    adresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text="Enter Gender :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(searchroot,text="Enter D.O.B :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(searchroot,text="Enter Date :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    '''Entries'''
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    addressentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    dobentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    ##add button
    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground="orange",bg="red",command=search)
    submitbtn.place(x=150,y=490)
    searchroot.mainloop()
def deletestudent():
    print("Student Added")
def updatestudent():
    def update():
        pass
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry("470x600+220+100")
    updateroot.title("Update Student")
    updateroot.config(bg="red")
    updateroot.iconbitmap("database.ico")
    updateroot.resizable(False,False)
    '''Search Student Labels'''
    idlabel = Label(updateroot,text="Enter Roll No :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text="Enter Name :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text="Mobile no :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    emaillabel = Label(updateroot,text="Enter Email :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    
    adresslabel = Label(updateroot,text="Enter Address :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    adresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text="Enter Gender :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(updateroot,text="Enter D.O.B :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text="Enter Date :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
    timelabel = Label(updateroot,text="Enter Time :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)

    '''Entries'''
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    dobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    timeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    timeentry.place(x=250,y=490)
    ##add button
    submitbtn = Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground="orange",bg="red",command=update)
    submitbtn.place(x=150,y=540)
    updateroot.mainloop()
def showstudent():
    print("Student Added")
def exportstudent():
    print("Student Added")
def exitstudent():
    res = messagebox.askyesnocancel('Notification: ',"Do you want to exit")
    if (res==True):
        root.destroy()
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data entered is wrong.Try Again')
            return
        try:
            strr = 'create database studentmanagementsystem2'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem2'
            mycursor.execute(strr)
            strr = 'create table studentdata2(Id int,Name varchar(20),MobileNo varchar(12),Email varchar(30),Address varhar(100),Gender varchar(50),D.O.B varchar(50),Added Date varchar(20),Added Time varchar(20)'
            mycursor.execute(strr)
            strr = 'alter table studentdata2 modify column Id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata2 modify column Id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo("Notificaton","Created and Connected Successfully",parent=dbroot)
        except:
            strr = 'use studentmanagementsystem2'
            mycursor.execute(strr)
            messagebox.showinfo("Notificaton","Connected Successfully",parent=dbroot)
        dbroot.destroy()
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry("470x250+800+230")
    dbroot.iconbitmap("database.ico")
    dbroot.resizable(False,False)
    dbroot.config(bg="skyblue")
    '''Connect Label'''
    hostlabel = Label(dbroot,text="Enter host : ",bg="blue",font=('times',20,'bold'),relief=RIDGE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)
    
    userlabel = Label(dbroot,text="Username : ",bg="blue",font=('times',20,'bold'),relief=RIDGE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)
    
    passwordlabel = Label(dbroot,text="Password : ",bg="blue",font=('times',20,'bold'),relief=RIDGE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)
    '''Entries'''
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)
    
    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)
    
    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    '''Buttons'''
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),width=20,relief=GROOVE,bg="red",activebackground="orange",command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d-%m-%Y")
    clock.config(text='Date :'+date_string+'\n'+"Time :"+time_string)
    clock.after(200,tick)



def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count= -1
        text=''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        count+=1
        
        
        SliderLabel.config(text=text)
        
    
    SliderLabel.after(100,IntroLabelTick)

'''End of function'''
from tkinter import * 
import time
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
'''Main File'''
root = Tk()
count = 0
text = ''
root.title("Student Management Sotware")
root.config(bg="silver")
root.geometry("1174x700+200+50")
root.iconbitmap("degree.ico")
root.resizable(False,False)
''' End of Main File'''

'''Creating Frames'''
#DataEntry Frame
DataEntryFrame = Frame(root,bg='darkgrey',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
  #Frame of Methods:
frontlabel = Label(DataEntryFrame,text="Functionality: ",width=30,font=('roman',22,'bold'),bg="darkgrey")
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('arial',20,'bold'),bd=6,bg="silver",activebackground="red",command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('arial',20,'bold'),bd=6,bg="silver",activebackground="red",command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

delbtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('arial',20,'bold'),bd=6,bg="silver",activebackground="red",command=deletestudent)
delbtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('arial',20,'bold'),bd=6,bg="silver",activebackground="red",command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('arial',20,'bold'),bd=6,bg="silver",activebackground="red",command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export Data',width=25,font=('arial',20,'bold'),bd=6,bg="silver",activebackground="red",command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('arial',20,'bold'),bd=6,bg="silver",activebackground="red",command=exitstudent)
exitbtn.pack(side=TOP,expand=True)




ShowDataFrame = Frame(root,bg='darkgrey',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

######Show Data#####
style = ttk.Style()
style.configure('Treeview.Heading',font=('roman',20,'bold'))
style.configure('Treeview',font=('times',15,'bold'),foreground="blue",background="cyan")
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)

'''Creating Slider'''
ss="Welcome to student management system "
SliderLabel = Label(root,relief=GROOVE,borderwidth=5,font=('Arial',20,'bold'),bg='purple')
SliderLabel.place(x=260,y=0)
IntroLabelTick()

'''Time and Clock'''
clock = Label(root,relief=RIDGE,borderwidth=4,font=('times',14,'bold'),bg='cyan')
clock.place(x=0,y=0)
tick()

'''Database connectivity button'''
connectbutton = Button(root,text="Connect to Database",width=24,font=('Roman',16,'bold'),bg="yellow",fg="green",relief=RIDGE,activebackground="red",activeforeground="white",command=Connectdb)
connectbutton.place(x=930,y=0)



root.mainloop()