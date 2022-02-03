
import guizero 
from guizero import App, Window, PushButton, Text, Box, TextBox, ButtonGroup, Combo, ListBox, info
#
import sqlite3  # Database
from sqlite3 import Error #
#
#
import os
import os.path
#
#

import datetime
from datetime import date

#
database_file = 'K1J.db' #name of database
UserID_logged = 1 # global varibel user id logged to show whos logged on 
Userstaff = 0    # This store whether the logiin user is staff or not 


####
#### Delete Database
####
def delete_database(database_file):
    if os.path.exists(database_file):
        os.remove(database_file)


delete_database(database_file)

####
#### Create Database
####

def execute_sql(database, sql_statement):  # This function executes the sql to return last row
    conn = sqlite3.connect(database)
    #conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()
    cur.execute(sql_statement)
    conn.commit()
    return 

sql = """
	CREATE TABLE "Customer" (
	"CustID"	INTEGER NOT NULL,
	"Firstname"	TEXT,
	"Surname"	TEXT,
	"Password"	TEXT,
	PRIMARY KEY("CustID" AUTOINCREMENT)
);
"""

sql2 = """
	CREATE TABLE "Staff" (
	"StaffID"	INTEGER NOT NULL,
	"StaffPassword"	TEXT,
	"StaffName"	TEXT,
	"StaffNumber"	INTEGER,
	PRIMARY KEY("StaffID" AUTOINCREMENT)
);
"""

sql3 = """
	CREATE TABLE "Message" (
	"MessageID"	INTEGER NOT NULL,
	"StaffID"	INTEGER,
	"CustID"	INTEGER,
	"MessageContent"	TEXT,
	"DateTime"	TEXT,
	PRIMARY KEY("MessageID" AUTOINCREMENT),
	FOREIGN KEY("CustID") REFERENCES Customer("CustID"),
	FOREIGN KEY("StaffID") REFERENCES Staff("StaffID")
);
"""

execute_sql(database_file, sql)
execute_sql(database_file, sql2)
execute_sql(database_file, sql3)

insertCust1 = "INSERT INTO Customer(Firstname, Surname, Password) VALUES( 'Marlon', 'Williams', 'pass')"
insertCust2 = "INSERT INTO Customer(Firstname, Surname, Password) VALUES( 'Andrew', 'Smith', 'pass')"
insertCust1 = "INSERT INTO Customer(Firstname, Surname, Password) VALUES( 'Joe', 'Williams', 'pass')"

insert1 = "INSERT INTO Staff(StaffPassword, StaffName, StaffNumber) VALUES('pass', 'Will', '01')"
insert2 = "INSERT INTO Staff(StaffPassword, StaffName, StaffNumber) VALUES('pass', 'Marlon', '02')"
insert3 = "INSERT INTO Staff(StaffPassword, StaffName, StaffNumber) VALUES('pass', 'Jack', '03')"
insert4 = "INSERT INTO Staff(StaffPassword, StaffName, StaffNumber) VALUES('pass', 'Tom', '04')"
insert5 = "INSERT INTO Staff(StaffPassword, StaffName, StaffNumber) VALUES('pass', 'Chloe', '05')"




insertMes1 = "INSERT INTO Message(StaffID, CustID, MessageContent, DateTime) VALUES(1, 1, 'Hello Content of message here', '21/01/2022')"
insertMes2 = "INSERT INTO Message(StaffID, CustID, MessageContent, DateTime) VALUES(1, 1, 'What are you interested in?', '22/01/2022')"



execute_sql(database_file, insertCust1)
execute_sql(database_file, insertCust2)
#
execute_sql(database_file, insert1)
execute_sql(database_file, insert2)
execute_sql(database_file, insert3)
execute_sql(database_file, insert4)
execute_sql(database_file, insert5)
#
execute_sql(database_file, insertMes1)
execute_sql(database_file, insertMes2)



###
###
###

def send_message():
	MessagesW.info(Text,"Sending your messages")
	if choice.value ==  "Marlon":
		S_ID = 1
	elif choice.value ==  "Andrew":
		S_ID = 2
	elif choice.value ==  "Joe":
		S_ID = 3
	today = date.today()
	print("Today's date:", today)
	query = ("INSERT INTO Message(StaffID, CustID, MessageContent, DateTime) VALUES(1, " + str(S_ID) + ", 'Next message', " + str(today) + ")")
	print(query)
	sql_Insert(database_file, query)










def Logindone_Check_Customer():
	print("Login check ")




####
#### Create window
####


app = App(title = "Login or sign up window")
app.set_full_screen()



StaffLogin = Window(app,title = "Please Login")
StaffLogin.hide()
StaffLogin.set_full_screen()

CustomerLogin = Window(app,title = "Please Login")
CustomerLogin.hide()
CustomerLogin.set_full_screen()



MessagesW = Window(app,title = "This is the start of your conversation")
MessagesW.hide()
MessagesW.set_full_screen()





####
#### Messages 
####

text = Text(MessagesW, text="See your messages below")
textspace = Text(MessagesW, text="            ")
StaffGetM= PushButton(MessagesW, text="Get my messages", command = Get_Messages, width=20, height = 2  )
textspace = Text(MessagesW, text="            ")
textspace = Text(MessagesW, text="            ")
textspace = Text(MessagesW, text="            ")
textspace = Text(MessagesW, text="            ")
list = ListBox(MessagesW, height = 500, width = 500)
textspace = Text(MessagesW, text="            ")
textwho = Text(MessagesW, text="Who are you sending a message to?            ")
choice = ButtonGroup(MessagesW, options=["Marlon", "Andrew", "Joe"], selected="Marlon")
textspace = Text(MessagesW, text="Please enter your message below:")
textMessagebox = TextBox(MessagesW, width = 70)
textMessagebox.text_size = 10

Send_Button = PushButton(MessagesW, text= "SEND!",  width=20, height = 2, command = send_message  )







app.display()
