import pickle
def menu_1():
    print('**********************************')
    print('*** AUTOMOBILE SERVICE STATION ***')
    print('***                            ***')
    print('***          MAIN MENU         ***')
    print('**********************************\n')
    print('1. Customer info')
    print('2. Fuel')
    print('3. Repair')
    print('4. Cleaning')
    print('5. Maintenance')
    print()
    print('9. Exit\n')
def db_creation():
    f1=open('fuel.dat','wb')
    fuel_d=[]
    pickle.dump(fuel_d,f1)
    f1.close()
    f2=open('repair.dat','wb')
    repair_d=[]
    pickle.dump(repair_d,f2)
    f2.close()
    f3=open('cleaning.dat','wb')
    cleaning_d=[]
    pickle.dump(cleaning_d,f3)
    f3.close()
    f4=open('maintenance.dat','wb')
    maintenance_d=[]
    pickle.dump(maintenance_d,f4)
    f4.close()
    f5=open('customer.dat','wb')
    customer_d=[]
    pickle.dump(customer_d,f5)
    f5.close()
    print('Database File Creation Successful')
def db_load():
    f1=open('fuel.dat','rb')
    f2=open('repair.dat','rb')
    f3=open('cleaning.dat','rb')
    f4=open('maintenance.dat','rb')
    f5=open('customer.dat','rb')
    customer_d=pickle.load(f5)
    fuel_d=pickle.load(f1)
    repair_d=pickle.load(f2)
    cleaning_d=pickle.load(f3)
    maintenance_d=pickle.load(f4)
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    print('Database Successfully Loaded')
    return customer_d, fuel_d, repair_d, cleaning_d, maintenance_d
def customer_menu():
    print("==========================")
    print('Customer Details Menu')
    print()
    print('1. Display all custumers')
    print('2. Add new custumer')
    print('3. Delete a customer')
    print('4. Search for a customer')
    print('5. Update Customer Info')
    print()
    print('9. Back to main menu')
    print()
def saving(customer_d, fuel_d, repair_d, cleaning_d, maintenance_d):
    f1=open('fuel.dat','wb')
    f2=open('repair.dat','wb')
    f3=open('cleaning.dat','wb')
    f4=open('maintenance.dat','wb')
    f5=open('customer.dat','wb')
    pickle.dump(customer_d,f5)
    pickle.dump(fuel_d,f1)
    pickle.dump(repair_d,f2)
    pickle.dump(cleaning_d,f3)
    pickle.dump(maintenance_d,f4)
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    print('DATABASE SAVED')
def new_customer(customer_d):
    while True:
        c_id=(input("Enter the Customer Id: :"))
        l=[]
        flag_1=0
        flag_2=0
        for i in customer_d:
            l.append(i[0])
        if c_id.isdigit():
            flag_2=1
        else:
            print('Please Enter the Customer ID properly using only digits.')
        if int(c_id) in l:
            print('This Customer ID exists.')
        else:
            flag_1=1
        
        if flag_1==1 and flag_2==1:
            c_id=int(c_id)
            break
    c_name=input("Enter the customer name : ")
    while True:
        c_no=input("Enter the customer phone no: ")
        if c_no.isdigit():
            break
        else:
            print('Please Enter the phone number properly using only digits.')
    c_address=input("Enter the customer address: ")
    while True:
        c_pincode=input("Enter the pincode: ")
        if c_pincode.isdigit():
            break
        else:
            print('Please Enter the pin code properly using only digits.')
    list1=[c_id,c_name,c_no,c_address,c_pincode]  
    customer_d.append(list1)
    return customer_d
def remove_customer(customer_d):
    flag=0
    while True:
        d=(input("Enter the the customer ID for deletion:- "))
        if d.isdigit():
            d=int(d)
            break
        else:
            print('Please Enter the Customer ID properly using only digits.')
    for i in customer_d:
        if i[0]==d:
            e=customer_d.index(i)
            f=customer_d.pop(e)
            print('Deletion of ',f,' Successful')
            flag=1
    if flag==0:
        print('ID Number Not Found')
    return customer_d
def remove_mainenance_record(maintenance_d):
    flag=0
    d=(input("Enter the the serial number for deletion:- "))
    for i in maintenance_d:
        if i[0]==d:
            e=maintenance_d.index(i)
            f=maintenance_d.pop(e)
            print('Deletion of',f,' Successful')
            flag=1
    if flag==0:
        print('Serial Number Not Found')
    return maintenance_d
def display_all(list_d):
    for i in list_d:
        print(i)
def add_maintenance_record(maintenance_d,customer_d):
    s_no=(input("Enter the serial Number: "))
    while True:
        c_id=(input("Enter the Customer Id: :"))
        if c_id.isdigit():
            c_id=int(c_id)
            break
        else:
            print('Please Enter the Customer ID properly using only digits.')
    flag=0
    for i in customer_d:
        if i[0]==c_id:
            while True:
                try:
                    c_ttlamt=float(input("Enter the total amount: "))
                    c_discount=float(input("Enter the discount(%): "))
                    break
                except:
                    print('Enter Numerical Values')
            c_des=input('Enter the description of maintenance: ')
            c_grandttl=c_ttlamt*(1-c_discount/100)
            l=(s_no,c_id,c_ttlamt,c_discount,c_grandttl,c_des)
            maintenance_d.append(l)
            flag=1
    if flag==0:
        print('Please Register the customer first!')
    return maintenance_d
def search_maintenance_record(maintenance_d):
    s_no=(input("Enter the serial Number to be searched: "))
    while True:
        try:
            c_id=int(input("Enter the Customer Id to be searched: :"))
            break
        except:
            print('Please Enter the Customer ID properly using only digits.')
    flag=0
    for i in maintenance_d:
        if i[0]==s_no and i[1]==c_id:
            print('[Serial Number, Customer ID, Total Amount, Discount(%), Grand Total, Description]')
            print(i)
            flag=1
    if flag==0:
        print('No record found on the given Serial Number and Customer ID')
def maintenance_menu():
    print('===============================\nMaintenance Menu\n')
    print('1. Display Maintenance record')
    print('2. Add Maintenance record')
    print('3. Delete a Maintenance record')
    print('4. Search for a maintenance record')
    print('9. Back to main menu\n')
def search_customer(customer_d):
    flag=0
    while True:
        d=(input("Enter the the customer ID for Search:- "))
        if d.isdigit():
            d=int(d)
            break
        else:
            print('Please Enter the Customer ID properly using only digits.')
    for i in customer_d:
        if i[0]==d:
            print('[Customer ID, Customer Name, Customer Phone No., Customer Address, Customer Pincode]')
            print(i)
            flag=1
    if flag==0:
        print('ID Number Not Found')
def fuel_menu():
    print('=======================\nFuel Menu')
    print('')
    print('1. Refill Gasoline')
    print('2. Refill Diesel')
    print('3. Display Records')
    print('4. Delete Record')
    print('9. Back to main menu')
    print()
def remove_fuel_record(fuel_d):
    flag=0
    d=(input("Enter the the serial number for deletion:- "))
    for i in fuel_d:
        if i[0]==d:
            e=fuel_d.index(i)
            f=fuel_d.pop(e)
            print('Deletion of',f,' Successful')
            flag=1
    if flag==0:
        print('Serial Number Not Found')
    return fuel_d
def add_fuel_record(fuel_d,fuel):
    s_no=input('Enter Serial Number:- ')
    while True:
        try:
            amt=input('Enter Amount(Rs):- ')
            break
        except:
            print('Please enter the amount properly in digits')
    tup=(s_no, fuel, amt)
    fuel_d.append(tup)
    return fuel_d
def repair_menu():
    print('=========================\nRepair Menu')
    print()
    print('1. Display All Records')
    print('2. Search For A Record')
    print('3. Add Record')
    print('4. Delete Record')
    print('9. Back To Main Menu')
    print()
def search_repair_record(repair_d):
    s_no=input('Enter Serial Number:- ')
    c_id=input('Enter Customer ID:- ')
    flag=0
    for i in repair_d:
        if i[0]==s_no and i[1]==int(c_id):
            print('[Serial No., Customer ID, Amount, Discount(%), Grand Total, Description]')
            print(i)
            flag==1
            break
    if flag==0:
        print('No Data Found')
def by():
    data_1=[80,114,111,103,114,97,109,32,66,121,32,65,97,100,
            105,116,104,121,97,110,32,82,97,106,117,32,79,102,
            32,67,108,97,115,115,32,49,50,32,65,116,32,83,70,
            83,32,80,117,98,108,105,99,32,83,99,104,111,111,
            108,32,38,32,74,117,110,105,111,114,32,67,111,108,
            108,101,103,101]
    for i in data_1:
        print(chr(i),end='')
    print()
def add_repair_record(repair_d,customer_d):
    s_no=input('Enter Serial Number:- ')
    while True:
        c_id=input('Enter Customer ID:- ')
        if c_id.isdigit():
            c_id=int(c_id)
            break
        else:
            print('Enter the Customer ID in digits')
    flag=0
    for i in customer_d:
        if i[0]==c_id:
            while True:
                try:
                    c_ttlamt=float(input("Enter the total amount: "))
                    c_discount=float(input("Enter the discount(%): "))
                except:
                    print('Enter Numerical Values')
            c_des=input('Enter the description of repair: ')
            c_grandttl=c_ttlamt*(1-c_discount/100)
            l=(s_no,c_id,c_ttlamt,c_discount,c_grandttl,c_des)
            repair_d.append(l)
            flag=1
            break
    if flag==0:
        print('Register the Customer First')
    return repair_d
def del_repair_record(repair_d):
    flag=0
    d=(input("Enter the the serial number for deletion:- "))
    for i in repair_d:
        if i[0]==d:
            e=repair_d.index(i)
            f=repair_d.pop(e)
            print('Deletion of',f,' Successful')
            flag=1
    if flag==0:
        print('Serial Number Not Found')
    return repair_d
def cleaning_menu():
    print('=========================\nCleaning Menu')
    print()
    print('1. Display All Records')
    print('2. Search For A Record')
    print('3. Add Record')
    print('4. Delete Record')
    print('9. Back To Main Menu')
    print()
def search_cleaning_record(cleaning_d):
    s_no=input('Enter Serial Number:- ')
    c_id=input('Enter Customer ID:- ')
    flag=0
    for i in cleaning_d:
        if i[0]==s_no and i[1]==int(c_id):
            print(i)
            flag==1
            break
    if flag==0:
        print('No Data Found')
def add_cleaning_record(cleaning_d,customer_d):
    s_no=input('Enter Serial Number:- ')
    while True:
        c_id=input('Enter Customer ID:- ')
        if c_id.isdigit():
            c_id=int(c_id)
            break
        else:
            print('Enter the Customer ID in digits')
    flag=0
    for i in customer_d:
        if i[0]==c_id:
            while True:
                try:
                    c_ttlamt=float(input("Enter the total amount: "))
                    c_discount=float(input("Enter the discount(%): "))
                    break
                except:
                    print('Enter Numerical Values')
            c_des=input('Enter the description of cleaning: ')
            c_grandttl=c_ttlamt*(1-c_discount/100)
            l=(s_no,c_id,c_ttlamt,c_discount,c_grandttl,c_des)
            cleaning_d.append(l)
            flag=1
            break
    if flag==0:
        print('Register the Customer First')
    return cleaning_d
def del_cleaning_record(cleaning_d):
    flag=0
    d=(input("Enter the the serial number for deletion:- "))
    for i in cleaning_d:
        if i[0]==d:
            e=cleaning_d.index(i)
            f=cleaning_d.pop(e)
            print('Deletion of',f,' Successful')
            flag=1
            break
    if flag==0:
        print('Serial Number Not Found')
    return cleaning_d
def edit_customer(customer_d):
    try:
        temp=0
        c_id=(input("Enter the Customer Id: :"))
        l=[]
        flag_1=0
        flag_2=0
        index_1=0
        for i in customer_d:
            l.append(i[0])
        if c_id.isdigit():
            flag_2=1
        else:
            print('Please Enter the Customer ID properly using only digits.')
        if int(c_id) in l:
            flag_1=1
            index_1=l.index(int(c_id))
            temp=1
        else:
            print('This Customer ID does not exist.')
        
        if flag_1==1 and flag_2==1:
            c_id=int(c_id)
        if temp==1:    
            for i in customer_d:
                if customer_d.index(i)==index_1:
                    c_name=i[1]
                    while True:
                        c_no=input("Enter the customer phone no: ")
                        if c_no.isdigit():
                            break
                        else:
                            print('Please Enter the phone number properly using only digits.')
                    c_address=input("Enter the customer address: ")
                    while True:
                        c_pincode=input("Enter the pincode: ")
                        if c_pincode.isdigit():
                            break
                        else:
                            print('Please Enter the pin code properly using only digits.')
        list1=[c_id,c_name,c_no,c_address,c_pincode]
        customer_d[index_1]=list1

    except:
        pass
    return customer_d
customer_d, fuel_d, repair_d, cleaning_d, maintenance_d = [], [], [], [], []
while True:
    by()
    print('\n\nStartup\n')
    b=input("Is this the first time running this program?(Y/N): ")
    if b=='y'or b=='Y':
        db_creation()
        break
    elif b=='n'or b=='N':
        customer_d, fuel_d, repair_d, cleaning_d, maintenance_d = db_load()
        break
    else:
        print('Enter a valid input')
    print('\n\n\n')
while True:
    menu_1()
    a=(input('Enter Choice (As Number):- '))
    if a=='1':
        while True:
            customer_menu()
            g=input('Enter the choice:- ')
            if g=='1':
                if len(customer_d)>0:
                    print('[Customer ID, Customer Name, Customer Details, Customer Address, Customer Pincode]')
                    display_all(customer_d)
                else:
                    print('No Customers Found')
            elif g=='2':
                customer_d=new_customer(customer_d)
            elif g=='3':
                customer_d=remove_customer(customer_d)
            elif g=='4':
                search_customer(customer_d)
            elif g=='5':
                customer_d=edit_customer(customer_d)
            elif g=='9':
                break
            else:
                print('Enter a valid choice')
    elif a=='2':
        while True:
                fuel=''
                fuel_menu()
                g=input("Enter your choice: ")
                if g=='1':
                    fuel='Gasoline'
                elif g=='2':
                    fuel='Diesel'
                elif g=='3':
                    if len(fuel_d)>0:
                        print('[Serial NO.,Fuel Refilled, Amount(Rs)]')
                        display_all(fuel_d)
                    else:
                        print('No Records found')
                elif g=='4':
                    fuel_d=remove_fuel_record(fuel_d)
                elif g=='9':
                    break
                else:
                    print('Invalid Choice')
                if fuel!='':
                    fuel_d=add_fuel_record(fuel_d,fuel)
    elif a=='3':
        while True:
            repair_menu()
            h=input('Enter Choice:- ')
            if h=='1':
                if len(repair_d)>0:
                    display_all(repair_d)
                else:
                    print('No Record Found')
            elif h=='2':
                search_repair_record(repair_d)
            elif h=='3':
                repair_d=add_repair_record(repair_d,customer_d)
            elif h=='4':
                repair_d=del_repair_record(repair_d)
            elif h=='9':
                break
            else:
                print('Invalid Choice!') 
    elif a=='4':
        while True:
            cleaning_menu()
            h=input('Enter Choice:- ')
            if h=='1':
                if len(cleaning_d)>0:
                    display_all(cleaning_d)
                else:
                    print('No Record Found')
            elif h=='2':
                search_cleaning_record(cleaning_d)
            elif h=='3':
                cleaning_d=add_cleaning_record(cleaning_d,customer_d)
            elif h=='4':
                cleaning_d=del_cleaning_record(cleaning_d)
            elif h=='9':
                break
            else:
                print('Invalid Choice!')    
    elif a=='5':
        while True:
            maintenance_menu()
            c=input('Enter the choice:- ')
            if c=='1':
                if len(maintenance_d)>0:
                    print('[Serial Number, Customer ID, Total Amount, Discount(%), Grand Total, Description]')
                    display_all(maintenance_d)
                else:
                    print('No maintenance records found')
            elif c=='2':
                maintenance_d=add_maintenance_record(maintenance_d,customer_d)
            elif c=='3':
                maintenance_d=remove_mainenance_record(maintenance_d)
            elif c=='4':
                search_maintenance_record(maintenance_d)
            elif c=='9':
                break
            else:
                print('Invalid Option')
    elif a=='9':
        saving(customer_d, fuel_d, repair_d, cleaning_d, maintenance_d)
        break
    else:
        print('Invalid Choice! Please Enter a Valid Choice!')

