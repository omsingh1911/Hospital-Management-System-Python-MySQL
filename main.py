import mysql.connector

mydb=mysql.connector.connect(user='root',host='localhost',passwd='')

mycursor=mydb.cursor()

try:
    mycursor.execute("create database hospital")
    mycursor.execute("use hospital")
except:
    mycursor.execute("use hospital")

print("----------------------------------------")
print("| |----------------------------------| |")
print("| |                                  | |")
print("| |    Hospital Management System    | |")
print("| |                                  | |")
print("| |----------------------------------| |")
print("----------------------------------------")


def Menu():   
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Patient details.")
    print("2. Doctor details.")
    print("3. Worker details.")
    print("4. Exit.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def MenuPatient():
    print("..............................")
    print("1. Insert record.")
    print("2. Show all records.")
    print("3. Search by serial number.")
    print("4. Create a bill.")
    print("5. View bill details.")
    print("6. Modify record.")
    print("7. Delete record.")
    print("8. Back")
    print("..............................")

def MenuDoctor():
    print("..............................")
    print("1. Insert record.")
    print("2. Show all records.")
    print("3. Search by ID.")
    print("4. Modify record.")
    print("5. Delete record.")
    print("6. Back")
    print("..............................")

def MenuWorker():
    print("..............................")
    print("1. Insert record.")
    print("2. Show all records.")
    print("3. Search by ID.")
    print("4. Modify record.")
    print("5. Delete record.")
    print("6. Back")
    print("..............................")

def CreatePatient():
    try:
        mycursor.execute('create table patient(PATIENT_ID varchar(20),NAME varchar(50),AGE varchar(10),SEX varchar(1),ADDRESS varchar(50),PHONE varchar(10),DISEASE varchar(50))')
        InsertPatient()
    except:
        InsertPatient()

def CreatePatientBill():
    try:
        mycursor.execute('create table bill(PATIENT_ID varchar(20),NAME varchar(50),AGE varchar(10),SEX varchar(1),VISITING_FEES varchar(10),MEDICINES varchar(10),ROOM_CAHRGES varchar(10))')
        InsertPatientBillDetails()
    except:
        InsertPatientBillDetails()

def CreateDoctor():
    try:
        mycursor.execute('create table doctor(DOCTOR_ID varchar(20),NAME varchar(50),AGE varchar(10),SEX varchar(1),PHONE varchar(10),ADDRESS varchar(50),DEPARTMENT varchar(20))')
        InsertDoctor()
    except:
        InsertDoctor()

def CreateWorker():
    try:
        mycursor.execute('create table worker(WORKER_ID varchar(20),NAME varchar(50),AGE varchar(10),SEX varchar(1),PHONE varchar(10),ADDRESS varchar(50),WORK varchar(20))')
        InsertWorker()
    except:
        InsertWorker()

def InsertPatient():
    while True:
        print("\nEnter details of new patient.\n")
        sno=int(input("Enter Patient ID :"))
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        sex=input("Enter Sex (M/F):")
        address=input("Enter Address:")
        pno=int(input("Enter Phone number:"))
        dname=input("Enter Disease Name:")
        Rec=[sno,name.upper(),age,sex.upper(),address.upper(),pno,dname.upper()]
        Cmd="insert into patient values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        print("\nRecord Inserted.\n")
        ch=input("Do you want to enter more records (Y/N) : ")
        if ch=='N' or ch=='n':
            break

def InsertPatientBillDetails():
    while True:
        print("\nEnter the bill details.\n")
        p_id=int(input("Enter Patient ID : "))
        p_name=input("Enter Patient name : ")
        p_age=int(input("Enter Age : "))
        p_sex=input("Enter Sex (M/F) : ")
        p_visit=int(input("Enter Doctor Visiting fees : "))
        p_medicine=int(input("Enter the cost of medicines : "))
        p_room=int(input("Enter room charges : "))
        p_total=p_visit+p_medicine+p_room
        print("Total charge : ",p_total)
        Rec=[p_id,p_name.upper(),p_age,p_sex.upper(),p_visit,p_medicine,p_room]
        Cmd="insert into bill values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        print("\nRecord Inserted.\n")
        ch=input("Do you want to enter more records (Y/N) : ")
        if ch=='N' or ch=='n':
            break

def InsertDoctor():
    while True:
        print("\nEnter details of new doctor.\n")
        did=int(input("Enter ID : "))
        dname=input("Enter Name :  ")
        dage=int(input("Enter Age : "))
        dsex=input("Enter Sex (M/F) : ")
        dphone=int(input("Enter Phone number : "))
        daddress=input("Enter Address : ")
        ddepartment=input("Enter Department : ")
        Rec=[did,dname.upper(),dage,dsex.upper(),dphone,daddress.upper(),ddepartment.upper()]
        Cmd="insert into doctor values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        print("\nRecord Inserted.\n")
        ch=input("Do you want to enter more records (Y/N) : ")
        if ch=='N' or ch=='n':
            break

def InsertWorker():
    while True:
        print("\nEnter details of new worker.\n")
        wid=int(input("Enter ID : "))
        wname=input("Enter Name :  ")
        wage=int(input("Enter Age : "))
        wsex=input("Enter Sex (M/F) : ")
        wphone=int(input("Enter Phone number : "))
        waddress=input("Enter Address : ")
        wdepartment=input("Enter type of work : ")
        Rec=[wid,wname.upper(),wage,wsex.upper(),wphone,waddress.upper(),wdepartment.upper()]
        Cmd="insert into worker values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        print("\nRecord Inserted.\n")
        ch=input("Do you want to enter more records (Y/N) : ")
        if ch=='N' or ch=='n':
            break

def OutputPatient():
    try:
       mycursor.execute("select * from patient")
       S=mycursor.fetchall()
       print("%15s %15s %15s %15s %15s %15s %15s" % ("PATIENT_ID","PATIENT_NAME","AGE","SEX","ADDRESS","PHONE","DISEASE"))
       print("="*120)
       for i in S:
           for j in i:
               print("%14s" % j, end=' ')
           print()
       print("="*120)
    except:
       print("\nTable doesn't exist.\n")

def OutputPatientBill():
    try:
       mycursor.execute("select * from bill")
       S=mycursor.fetchall()
       print("%15s %15s %15s %15s %15s %15s %15s" % ("PATIENT_ID","PATIENT_NAME","AGE","SEX","VISITING_FEES","MEDICINE_CHARGE","ROOM_CAHRGE"))
       print("="*120)
       for i in S:
           for j in i:
               print("%14s" % j, end=' ')
           print()
       print("="*120)
    except:
       print("\nTable doesn't exist.\n")
    
def OutputDoctor():
    try:
       mycursor.execute("select * from doctor")
       S=mycursor.fetchall()
       print("%15s %15s %15s %15s %15s %15s %15s" % ("DOCTOR_ID","NAME","AGE","SEX","PHONE","ADDRESS","DEPARTMENT"))
       print("="*120)
       for i in S:
           for j in i:
               print("%14s" % j, end=' ')
           print()
       print("="*120)
    except:
       print("\nTable doesn't exist.\n")

def OutputWorker():
    try:
       mycursor.execute("select * from worker")
       S=mycursor.fetchall()
       print("%15s %15s %15s %15s %15s %15s %15s" % ("WORKER_ID","NAME","AGE","SEX","PHONE","ADDRESS","WORK"))
       print("="*120)
       for i in S:
           for j in i:
               print("%14s" % j, end=' ')
           print()
       print("="*120)
    except:
       print("\nTable doesn't exist.\n")       

def DispPatientSearchSno():
    try:
        mycursor.execute("select * from patient")
        S=mycursor.fetchall()
        ch=input("\nEnter the serial number to be searched : ")       
        for i in S:
            if i[0]==ch:
                print("="*120)
                F="%15s %15s %15s %15s %15s %15s %15s"
                print(F % ("PATIENT_ID","PATIENT_NAME","AGE","SEX","ADDRESS","PHONE","DISEASE"))
                print("="*120)
                for j in i:
                    print('%14s' % j,end='')
                print()
                break
        else: 
            print("\nRecord Not found.\n")
    except:
        print("\nTable doesn't exist.\n")

def DispDoctorSearchId():
    try:
        mycursor.execute("select * from doctor")
        S=mycursor.fetchall()
        ch=input("\nEnter the ID to be searched : ")
        for i in S:
            if i[0]==ch:
                print("="*120)
                F="%15s %15s %15s %15s %15s %15s %15s"
                print(F % ("DOCTOR_ID","NAME","AGE","SEX","PHONE","ADDRESS","DEPARTMENT"))
                print("="*120)
                for j in i:
                    print('%14s' % j,end=' ')
                print()
                break
        else:
            print("\nRecord Not found.\n")
    except:
        print("\nTable doesn't exist.\n")
    
def DispWorkerSearchId():
    try:
        mycursor.execute("select * from worker")
        S=mycursor.fetchall()
        ch=input("\nEnter the ID to be searched : ")
        for i in S:
            if i[0]==ch:
                print("="*120)
                F="%15s %15s %15s %15s %15s %15s %15s"
                print(F % ("WORKER_ID","NAME","AGE","SEX","PHONE","ADDRESS","WORK"))
                print("="*120)
                for j in i:
                    print('%14s' % j,end=' ')
                print()
                break
        else:
            print("\nRecord Not found.\n")
    except:
        print("\nTable doesn't exist.\n")

def UpdatePatient(): 
    try:
        mycursor.execute("select * from patient")
        S=mycursor.fetchall()
        A=input("\nEnter the patient ID whose details to be changed : ")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name : ")
                    i[1]=i[1].upper()
                ch=input("Change Age(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[2]=int(input("Enter Age : "))
                ch=input("Change Sex(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter Sex : ")
                    i[3]=i[3].upper()
                ch=input("Change Address(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address : ")
                    i[4]=i[4].upper()     
                ch=input("Change Phone number(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[5]=int(input("Enter Phone number : "))
                ch=input("Change Disease name(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter Disease name : ")
                    i[6]=i[6].upper()
                cmd="UPDATE PATIENT SET NAME=%s,AGE=%s,SEX=%s,ADDRESS=%s,PHONE=%s,DISEASE=%s WHERE PATIENT_ID=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("\nAccount Updated\n.")
                break
        else:
            print("\nRecord not found\n.")
    except:
        print("\nNo such table\n.")

def UpdateDoctor():
    try:
        mycursor.execute("select * from doctor")
        S=mycursor.fetchall()
        A=input("\n\nEnter the ID whose details to be changed : ")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name : ")
                    i[1]=i[1].upper()
                ch=input("Change Age(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[2]=int(input("Enter Age : "))
                ch=input("Change Sex(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter Sex : ")
                    i[3]=i[3].upper()
                ch=input("Change Phone number(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[5]=int(input("Enter Phone number : "))
                ch=input("Change Address(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address : ")
                    i[4]=i[4].upper()     
                ch=input("Change Department(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter Department : ")
                    i[6]=i[6].upper()
                cmd="UPDATE DOCTOR SET NAME=%s,AGE=%s,SEX=%s,PHONE=%s,ADDRESS=%s,DEPARTMENT=%s WHERE DOCTOR_ID=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("\nAccount Updated.\n")
                break
        else:
            print("\nRecord not found.\n")
    except:
        print("\nNo such table.\n")

def UpdateWorker():
    try:
        mycursor.execute("select * from worker")
        S=mycursor.fetchall()
        A=input("\nEnter the ID whose details to be changed : ")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name : ")
                    i[1]=i[1].upper()
                ch=input("Change Age(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[2]=int(input("Enter Age : "))
                ch=input("Change Sex(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter Sex : ")
                    i[3]=i[3].upper()
                ch=input("Change Phone number(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[5]=int(input("Enter Phone number : "))
                ch=input("Change Address(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address : ")
                    i[4]=i[4].upper()     
                ch=input("Change Work(Y/N) : ")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter Work : ")
                    i[6]=i[6].upper()
                cmd="UPDATE WORKER SET NAME=%s,AGE=%s,SEX=%s,PHONE=%s,ADDRESS=%s,WORK=%s WHERE WORKER_ID=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("\nAccount Updated.\n")
                break
        else:
            print("\nRecord not found.\n")
    except:
        print("\nNo such table.\n")

def DeletePatient():
    try:
        mycursor.execute("select * from patient")
        S=mycursor.fetchall()
        A=input("\n\nEnter the serial number whose record is to be deleted : ")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from patient where PATIENT_ID=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("\nRecord Deleted.\n")
                break
        else:
            print("\nRecord not found.\n")
    except:
        print("\nNo such Table.\n")
        
        
def DeleteDoctor():
    try:
        mycursor.execute("select * from doctor")
        S=mycursor.fetchall()
        A=input("\nEnter the ID whose record is to be deleted : ")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from doctor where DOCTOR_ID=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("\nRecord Deleted.\n")
                break
        else:
            print("\nRecord not found.\n")
    except:
        print("\nNo such Table.\n")

def DeleteWorker():
    try:
        mycursor.execute("select * from worker")
        S=mycursor.fetchall()
        A=input("\nEnter the ID whose record is to be deleted : ")
        for i in S:
            i=list(i)
            if i[0]==A:
                cmd="delete from worker where WORKER_ID=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("\nRecord Deleted.\n")
                break
        else:
            print("\nRecord not found.\n") 
    except:
        print("\nNo such Table.\n")

while True:
    Menu()
    ch=input("\nEnter your choice : ")
    if ch=="1":
        while True:
            MenuPatient()
            ch1=input("\nEnter your choice : ")
            if ch1=="1":
                CreatePatient()
            elif ch1=="2":
                OutputPatient()
            elif ch1=="3":
                DispPatientSearchSno()
            elif ch1=="4":
                CreatePatientBill()
            elif ch1=="5":
                OutputPatientBill()
            elif ch1=="6":
                UpdatePatient()
            elif ch1=="7":
                DeletePatient()
            elif ch1=="8":
                print("\nBack to the main menu.\n")
                break
            else:
                print("\nInvalid Choice.\n")
                
    elif ch=="2":
        while True:
            MenuDoctor()
            ch2=input("\nEnter your choice : ")
            if ch2=="1":
                CreateDoctor()
            elif ch2=="2":
                OutputDoctor()
            elif ch2=="3":
                DispDoctorSearchId()
            elif ch2=="4":
                UpdateDoctor()
            elif ch2=="5":
                DeleteDoctor()
            elif ch2=="6":
                print("\nBack to the menu.\n")
                break
            else:
                print("\nInvalid Choice.\n")
                
    elif ch=="3":
        while True:
            MenuWorker()
            ch3=input("\nEnter your choice : ")
            if ch3=="1":
                CreateWorker()
            elif ch3=="2":
                OutputWorker()
            elif ch3=="3":
                DispWorkerSearchId()
            elif ch3=="4":
                UpdateWorker()
            elif ch3=="5":
                DeleteWorker()
            elif ch3=="6":
                print("\nBack to the menu.\n")
                break
            else:
                print("\nInvalid Choice.\n")
                
    elif ch=="4":
        print("\nGood Bye ! Have a nice day . . . \n")
        break
    else:
        print("\nInvalid Choice.\n")
        