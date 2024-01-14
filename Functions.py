'''
This File Contains ALL THE FUNCTIONS REQUIRED FOR STUDENT MANAGEMENT TO BE SAVED AS A BINARY FILE
'''
from pickle import load,dump
import tabulate
def add():
    try:
        a=int(input("Enter Admission Number: "))
        p=open("Student_DB.txt","rb")
        try:
            L=[]
            c=open("restore.txt",'rb')
            try:
                while True:
                    tmp=load(c)
                    L.append(tmp)
            except:
                try:
                    temp=0
                    while True:
                        q=load(p)
                        for i in L:
                            if q[1]==a or i[1]==a:
                                print("\t\t--------THIS ADMISSION NUMBER ALREADY EXISTS--------")
                                print("\t\t\t-------------TRY AGAIN LATER------------")
                                temp=1
                                break
                except:
                    p.close()
                    if temp==0:
                        print("\t\t\t----------ADDING RECORDS----------")
                        p=open("Student_DB.txt",'ab')
                        b=input("Enter Student Name: ")
                        c=input("Enter Student's Class: ")
                        d=input("Enter Student's Section: ")
                        dump([b,a,c,d],p)
                        print("\t\t\t---------RECORD HAS BEEN SAVED---------")
                        p.close()
        except FileNotFoundError:
            try:
                temp=0
                while True:
                    q=load(p)
                    if q[1]==a:
                        print("\t\t--------THIS ADMISSION NUMBER ALREADY EXISTS--------")
                        print("\t\t\t-------------TRY AGAIN LATER------------")
                        temp=1
                        break
            except:
                p.close()
                if temp==0:
                    print("\t\t\t----------ADDING RECORDS----------")
                    p=open("Student_DB.txt",'ab')
                    b=input("Enter Student Name: ")
                    c=input("Enter Student's Class: ")
                    d=input("Enter Student's Section: ")
                    dump([b,a,c,d],p)
                    print("\t\t\t---------RECORD HAS BEEN SAVED---------")
                    p.close()

    except FileNotFoundError:
        print("\t\t--------ADDING RECORDS--------")
        p=open("Student_DB.txt",'ab')
        b=input("Enter Student Name: ")
        c=input("Enter Student's Class: ")
        d=input("Enter Student's Section: ")
        dump([b,a,c,d],p)
        print("\t\t\t---------RECORD HAS BEEN SAVED---------")
        p.close()
def search():
    try:
        f=open("Student_DB.txt",'rb')
        try:
            print("PRESS 1 to search using Admission Number")
            print("PRESS 2 to search using Name")
            i=int(input("Enter Choice: "))
            temp=0
            if i in range(1,3):
                if i==1:
                    a=int(input("Enter Admission Number: "))
                if i==2:
                    b=input("Enter Student Name: ")
                L=[]
                while True:
                    if i==1:
                        q=load(f)
                        if q[1]==a:
                            print("\n\t\t\t-------------RECORD FOUND------------\n")
                            L.append([q[0],q[1],q[2],q[3]])
                            temp=1
                    elif i==2:
                        q=load(f)
                        if q[0].upper()==b.upper():
                            print("\n\t\t------------RECORD FOUND------------\n")
                            L.append([q[0],q[1],q[2],q[3]])
                            temp=1
            else:
                print("--------ENTER A VALID INPUT--------")
        except:
            import tabulate
            D=["Name","Admission Number","Class","Section"]
            if temp==0:
                print("\t\t--------NO RECORD FOUND-------")
            else:
                print(tabulate.tabulate(L,headers=D,tablefmt='grid'))
    except FileNotFoundError:
        print("\t\t--------------NO SUCH FILE EXISTS---------------")
def delete():
    try:
        f=open("Student_DB.txt",'rb')
        g=open("temp.txt",'ab')
        c=open("restore.txt",'ab')
        print("PRESS 1 to delete using Admission Number:")
        print("PRESS 2 to delete using Student's name: ")
        x=int(input("Enter Choice: "))
        if x in range(1,3):
            try:
                if x==1:
                    m=int(input("Enter Admission Number: "))
                    import tabulate
                    temp=0
                    while True:
                        t=load(f)
                        if t[1]==m:
                            temp=1
                            dump(t,c)
                            print("\t\t-----------RECORD FOUND----------")
                            print(tabulate.tabulate([t],headers=['Name','Admission Number','Class','Section'],tablefmt='grid'))
                            print("\n\t\t\t--------RECORD DELETED--------")
                        else:
                            dump(t,g)
                    
                if x==2:
                    n=input("Enter Student's Name:  ")
                    import tabulate
                    temp=0
                    while True:
                        t=load(f)
                        if t[0].upper()==n.upper():
                            temp=1
                            dump(t,c)
                            print("\t\t-----------RECORD FOUND----------")
                            print(tabulate.tabulate([t],headers=['Name','Admission Number','Class','Section'],tablefmt='grid'))
                            print("\n\t\t\t--------RECORD DELETED--------")
                        else:
                            dump(t,g)
                else:
                    print("\t\t--------INVALID INPUT--------")
            except:
                if temp==0:
                    print("\t\t----------NO SUCH RECORD FOUND----------")
                f.close()
                g.close()
                c.close()
                import os
                os.remove("Student_DB.txt")
                os.rename("temp.txt","Student_DB.txt")
    except FileNotFoundError:
        print("\t\t---------------NO SUCH FILE EXISTS---------------")
def restore():
    try:
        f=open("restore.txt",'rb')
        g=open("Student_DB.txt",'ab')
        h=open("xyz.txt",'ab')
        print("PRESS 1 to restore using Admission Number:")
        print("PRESS 2 to restore using Student's name:")
        x=int(input("Enter Choice: "))
        if x in range(1,3):
            try:
                import tabulate
                temp=0
                if x==1:
                    e=int(input("Enter Admission Number: "))
                    while True:
                        y=load(f)
                        if y[1]==e:
                            temp=1
                            print(tabulate.tabulate([y],headers=['Name','Admission Number','Class','Section'],tablefmt='grid'))
                            res=input("Press y to Restore this record: ")
                            if res in 'yY':
                                dump(y,g)
                                print("\t\t\t---------THIS RECORD HAS BEEN RESTORED SUCCESSFULLY--------")
                            else:
                                dump(y,h)
                                print("\t\t-------THIS RECORD HAS NOT BEEN ADDED TO FILE------")
                        if y[1]!=e:
                            dump(y,h)
                if x==2:
                    s=input("Enter Name of Student: ")
                    while True:
                        y=load(f)
                        if y[0].upper()==s.upper():
                            temp=1
                            print(tabulate.tabulate([y],headers=['Name','Admission Number','Class','Section'],tablefmt='grid'))
                            res=input("Press y to Restore this record: ")
                            if res in 'yY':
                                dump(y,g)
                                print("\t\t\t---------THIS RECORD HAS BEEN RESTORED SUCCESSFULLY--------")
                            else:
                                dump(y,h)
                                print("\t\t-------THIS RECORD HAS NOT BEEN ADDED TO FILE------")
                        else:
                            dump(y,h)
            except:
                if temp==0:
                    print("\t\t---------NO SUCH RECORD DELETED---------")
                f.close()
                g.close()
                h.close()
                import os
                os.remove("restore.txt")
                os.rename("xyz.txt","restore.txt")
        else:
            print("\t\t------------ENTER A VALID INPUT-----------")
    except FileNotFoundError:
        print("\t\t------------------NO SUCH FILE EXISTS---------------")
def view_all():
    import tabulate
    try:
        f=open("Student_DB.txt",'rb')
        try:
            L=[]
            while True:
                y=load(f)
                L.append(y)
        except:
            print("\n\nDATA IN FILE IS AS FOLLOWS:\n\n")
            if len(L)!=0:
                print(tabulate.tabulate(L,headers=['Name','Admission number','Class','Section'],tablefmt='grid'))
            else:
                print("\t\t\t-----------NO RECORD FOUND----------")
    except FileNotFoundError:
        print("\t\t------------------NO SUCH FILE EXISTS---------------")
def update():
    try:
        f=open("Student_DB.txt",'rb')
        h=open('temporary.txt','ab')
        try:
            print("PRESS 1 to search record using Admission Number:")
            print("PRESS 2 to search record using Student's name:")
            x=int(input("Enter Choice: "))
            if x in range(1,3):
                if x==1:
                    admno=int(input("Enter Admission Number: "))
                    while True:
                        y=load(f)
                        if y[1]==admno:
                            print("Enter What do you want to Update:")
                            print("(1)Name\n(2)Admission Number\n(3)Class\n(4)Section")
                            z=int(input("Enter choice: "))
                            if z in range(1,5):
                                if z==1:
                                    Name=input("Enter Updated name: ")
                                    y[0]=Name
                                    dump(y,h)
                                if z==2:
                                    Admno=int(input("Enter New Admission Number: "))
                                    y[1]=Admno
                                    dump(y,h)
                                if z==3:
                                    Class=input("Enter New Class: ")
                                    y[2]=Class
                                    dump(y,h)
                                if z==4:
                                    Section=input("Enter New Section: ")
                                    y[3]=Section
                                    dump(y,h)
                            else:
                                print("\t\t\t----------ENTER A VALID INPUT---------")
                        else:
                            dump(y,h)
                if x==2:
                    name=input("Enter name: ")
                    while True:
                        y=load(f)
                        if y[0].upper()==name.upper():
                            print("Enter What do you want to Update:")
                            print("1)Name\n2)Admission Number\n3)Class\n4)Section")
                            z=int(input("Enter choice: "))
                            if z in range(1,5):
                                if z==1:
                                    Name=input("Enter Updated name: ")
                                    y[0]=Name
                                    dump(y,h)
                                if z==2:
                                    Admno=int(input("Enter New Admission Number: "))
                                    y[1]=Admno
                                    dump(y,h)
                                if z==3:
                                    Class=input("Enter New Class: ")
                                    y[2]=Class
                                    dump(y,h)
                                if z==4:
                                    Section=input("Enter New Section: ")
                                    y[3]=Section
                                    dump(y,h)
                            else:
                                print("\t\t\t----------ENTER A VALID INPUT---------")
                        else:
                            dump(y,h)
            else:
                print("\t\t\t----------ENTER A VALID INPUT---------")
        except:
            f.close()
            h.close()
            import os
            os.remove("Student_DB.txt")
            os.rename("temporary.txt","Student_DB.txt")
            print("\t\t\t------------DATA HAS BEEN UPDATED SUCCESSFULLY-------------")
    except FileNotFoundError:
        print("\t\t------------------NO SUCH FILE EXISTS---------------")                     
def export_to_csv():
    import csv
    import os
    loc=os.getcwd()
    try:
        f=open("Student_DB.txt",'rb')
        m=input("Enter File name: ")
        s=m+'.csv'
        try:
            f1=open(s,'r')
            print("\t\tTHIS FILE ALREADY EXISTS")
        except:
            f1=open(s,'a',newline='')
            try:
                L=[]
                data=csv.writer(f1)
                while True:
                    x=load(f)
                    L.append(x)
            except:
                data.writerows(L)
                print("\t\t-----CSV FILE WITH NAME",s,"HAS BEEN SUCCESSFULLY CREATED------")
                print("\t\tLocation=",loc)
                f.close()
                f1.close()
    except FileNotFoundError:
        print("\t\t-----------NO SUCH FILE EXISTS---------------")
