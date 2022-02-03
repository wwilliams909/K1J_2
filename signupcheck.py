####
#### Sign up check
####

def signup_check():
    Firstname = Fn.value
    Surname = SN.value
    UserName = UserN.value
    UserPassWord = UserPW.value
    #Premium.value = "yes"
    if PremO.value == "yes":
        Prem = 1
    else:
        Prem = 0
    sql_query = f"Insert into userTable (UserFN, UserSN , UserName, UserPW , PremOption) values ('{Firstname}' , '{Surname}' ,'{UserName}' , '{UserPassWord}', '{Prem}');"
    execute_sql(database_file, sql_query)
    info("Account Created","You have successfully created an account!")
    
    
    
    def sql_Insert(con,entities):
    cursorObj= con.cursor()
    cursorObj.execute("INSERT INTO USERTABLE ( UserID , userName , userPW  , userFN , userSN , PremOption) VALUES (?,?,?,?,?,?)",entities)
    con.commit()
