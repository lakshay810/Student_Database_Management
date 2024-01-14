# Student Management system

# Note that to Run this file, you must download the Functions.py file in your device
from Functions import *
while True:
    print("Press 1 to add data")
    print("Press 2 to Search data")
    print("Press 3 to Delete Student data")
    print("Press 4 to Restore student details")
    print("Press 5 to View all Student's data")
    print("Press 6 to update data")
    print("Press 7 to export to a CSV file")
    print("Press 8 TO EXIT")
    x=int(input("Enter CHOICE: "))
    if x==1:
        add()
    elif x==2:
        search()
    elif x==3:
        delete()
    elif x==4:
        restore()
    elif x==5:
        view_all()
    elif x==6:
        update()
    elif x==7:
        export_to_csv()
    elif x==8:
        break
    else:
        print("--------------------INVALID INPUT--------------------------")
