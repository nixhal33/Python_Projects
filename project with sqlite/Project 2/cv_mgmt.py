# simply importing sqlite3
import sqlite3

# now i am gonna create the table using sqlite as i am also gonna use sqlite
#
conn=sqlite3.connect('cv_mgmt.db')
curser=conn.cursor()

curser.execute('''
        CREATE TABLE IF NOT EXISTS cv (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                marital_status TEXT NOT NULL,
                studies TEXT NOT NULL
                )
''')

def list_cv():
     curser.execute("SELECT * FROM cv")
     cv=curser.fetchall()
     if not cv:
         print("No CV detected!!")
     else:
         for row in cv:
             print(row)

def add_new_cv(name,phone,email,address,marital_status,studies):
     curser.execute("INSERT INTO cv (name,phone,email,address,marital_status,studies) VALUES (?,?,?,?,?,?)",(name,phone,email,address,marital_status,studies))
     conn.commit()
     print(" \n New CV added successfully!! \n")

def update_cv(new_name,new_phone,new_email,new_address,new_marital_status,new_studies,cv_id):
     curser.execute("UPDATE cv SET name=?,phone=?,email=?,address=?,marital_status=?,studies=? WHERE id=?",(new_name,new_phone,new_email,new_address,new_marital_status,new_studies,cv_id))
     conn.commit()
     print("\n CV updated successfully!! \n")

def delete_cv(cv_id):
     curser.execute("DELETE FROM cv WHERE id=?",(cv_id,))
     conn.commit()
     print("\n CV deleted successfully!! \n")



def main():
        while True:
                print(" \n This is Your CV MANAGEMENT SYSTEM using the SQLITE3 DATABASE \n")
                print("\n  Enter Your Choice !! \n")
                print("\n")
                print("1. List the CV ")
                print("2. Add new CV ")
                print("3. Update  CV")
                print("4. Delete CV ")
                print("5. Exit this App")
                print('\n')
                
                choice=input("Enter your choice:")
                
                # using the if else statement to check the choice of the user
                if choice=='1':
                        list_cv()

                elif choice=='2':
                        name=input("Enter the name of the person : ")
                        phone=input("Enter the phone number of the person : ")
                        email=input("Enter the email of the person : ")
                        address=input("Enter the address of the person : ")
                        marital_status=input("Enter the marital status of the person : ")
                        studies=input("Enter the studies of the person : ")
                        add_new_cv(name,phone,email,address,marital_status,studies)
                
                elif choice=='3':
                        cv_id=input("Enter the ID of the person you want to update : ")
                        name=input("Enter the new name of the person : ")
                        phone=input("Enter the new phone number of the person : ")
                        email=input("Enter the new email of the person : ")
                        address=input("Enter the new address of the person : ")
                        marital_status=input("Enter the new marital status of the person : ")
                        studies=input("Enter the new studies of the person : ")
                        update_cv(name,phone,email,address,marital_status,studies,cv_id)  
                        
                elif choice=='4':
                        cv_id=input("Enter the ID of the person you want to delete : ")
                        delete_cv(cv_id)

                elif choice=='5':
                        break

                else:
                        print("Invalid choice entered!!!")
        # closing the connection after the while loop ends
        conn.close()

if __name__=='__main__':
    main()      
