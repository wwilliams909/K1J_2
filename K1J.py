
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


def query_database(database, query):  # This function querys the database
    conn = sqlite3.connect(database) # connecting to the database which is a file containg the databse
    cur = conn.cursor()
    cur.execute(query)  # query is astring you want to run on the database
    rows = cur.fetchall()
    cur.close()
    return rows



def sql_Insert(database_file, query):
    conn = sqlite3.connect(database_file) # connecting to the database which is a file containg the databse
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()



def Logindone_Check_Staff():
	print("Login check ")
	query = ("SELECT * from Staff WHERE StaffNumber = '"+ str(StaffUN.value) + "' AND StaffPassword = '" + str(StaffPW.value) + "'")
	print(query)
	row = query_database(database_file, query)
	if len(row)== 0:
		info("Error!", "Your details are not in our database! Try again.")

	else:
		UserID_logged = row[0] [0]
		StaffLogin.hide()
		MessagesW.show()



def Get_Messages():
	MessagesW.info(Text, "Getting your messages")
	query = ("SELECT * from Message WHERE StaffID = '"+ str(UserID_logged) + "'")
	print(query)
	row = query_database(database_file, query)
	if len(row)== 0:
		info("You have no new messages!")

	else:
		# clearlist box
		list.clear()
		# add messages to the list box
		for x in range (0,len(row)):
			list.append(row[x])
		StaffLogin.hide()
		MessagesW.show()




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
#### Open & Close Windows
####



def open_CustomerLogin():
    CustomerLogin.show()
    app.hide()

def open_StaffLogin():
    StaffLogin.show()
    app.hide()

####
#### Back buttons
####


def Go_home():
	StaffLogin.hide()
	CustomerLogin.hide()
	app.show()


####
#### Greetings page
####
textspace = Text(app, text="            ")
textspace = Text(app, text="            ")
textspace = Text(app, text="            ")
textspace = Text(app, text="            ")
textspace = Text(app, text="            ")
Newbox = Box(app, layout="grid")
StaffLoginbutton = PushButton(Newbox,text = "Staff Login", width = 10, command = open_StaffLogin, grid=[0,0])
CustomerLoginbutton = PushButton(Newbox,text = "Customer Login", width = 10, command = open_CustomerLogin, grid=[1,0])




####
#### Customer Login Window 
####

text = Text(CustomerLogin, text="Enter your details to login!")
textspace = Text(CustomerLogin, text="            ")
textspace = Text(CustomerLogin, text="Please enter your username:")
CustomerUN = TextBox(CustomerLogin, text = "", width=30)
textspace1 = Text(CustomerLogin, text="Please enter your password:")
CustomerPW = TextBox(CustomerLogin, text = "", width=30)
back_button = PushButton(CustomerLogin, text="Home", command = Go_home, width=20, height = 2  )
CustomerLoginCheck = PushButton(CustomerLogin, text="Login", command = Logindone_Check_Customer, width=20, height = 2  )





####
#### Staff Login Window
####

text = Text(StaffLogin, text="Enter your details to login!")
textspace = Text(StaffLogin, text="            ")
textspace = Text(StaffLogin, text="Please enter your userID:")
StaffUN = TextBox(StaffLogin, text = "", width=30)
textspace1 = Text(StaffLogin, text="Please enter your password:")
StaffPW = TextBox(StaffLogin, text = "", width=30)
back_button = PushButton(StaffLogin, text="Home", command = Go_home, width=20, height = 2  )
StaffLoginCheck= PushButton(StaffLogin, text="Login", command = Logindone_Check_Staff, width=20, height = 2  )










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






####
#### Sales Screen
####

#text = Text(Sales, text = "Sales screeen")

app.display()