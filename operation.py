import sqlite3
class Phonebook:
    def __init__(self):
        self.name = ''
        self.number = ''
        self.location = ''
        
    def giveContactDetails(self):
        self.name = input("Name: ")
        self.number = int(input("Number: "))
        self.location = input("Location: ")
        return self.name, self.number, self.location
        
    def displayContacts(self):
        print("Name: ",self.name)
        print("Number: ",self.number)
        print("Location: ",self.location)
        print("\n")
        
    def deleteContact(self,name):
        self.name = input("Enter: ")
        return name
    
    def editContact(self, old_name):
        con = sqlite3.connect('phonebook.db')
        cur = con.cursor()
        cur.execute("SELECT NAME, NUMBER, LOCATION FROM PHONEBOOK WHERE NAME=?", (old_name,))
        result = cur.fetchone()
        if result:
            print("Contact found. Please provide the updated details:")
            new_name = input("New Name: ")
            new_number = int(input("New Number: "))
            new_location = input("New Location: ")
            cur.execute("UPDATE PHONEBOOK SET NAME=?, NUMBER=?, LOCATION=? WHERE NAME=?", (new_name, new_number, new_location, old_name))
            con.commit()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
    
contactList = []
choice = 'y'

while(choice.lower()=='y'):
    print("Press 1.Add Contacts 2.DisplayContacts 3.Delete 4.Edit")
    responce = int(input("Press your choice: "))
    print("\n")
    
    if (responce == 1):
        contact = Phonebook() 
        (name, number, location)=contact.giveContactDetails()
        with sqlite3.connect("phonebook.db") as con:
            cur = con.cursor()
            cur.execute("""
                        INSERT INTO PHONEBOOK(NAME, NUMBER, LOCATION)
                        VALUES(?,?,?)
                        """,(name, number, location))
            con.commit()
            msg = "Connected Successfully"
    elif(responce == 2):
        con = sqlite3.connect('phonebook.db')
        cur = con.cursor()
        cur.execute("SELECT NAME, NUMBER, LOCATION FROM PHONEBOOK")
        result = cur.fetchall()
        for i in range(len(result)):
            print(result[i][0],"  ",result[i][1],"  ",result[i][2])
            #print("\n")
        
        #print(result, sep = '\n')
    
    elif(responce == 3):
        contact = Phonebook()
        (name)= contact.deleteContact(name)
        con = sqlite3.connect('phonebook.db')
        cur = con.cursor()
        cur.execute("DELETE FROM PHONEBOOK WHERE NAME=?",(name,))
        con.commit()
        
        
    elif responce == 4:
        contact = Phonebook()
        (name, number, location) = contact.giveContactDetails()
        contact.editContact(name)  
              
    else:
        print("Please check your responce")
        
    choice = input("Press Y to Continue: ")
else:
    print("Thank You")
