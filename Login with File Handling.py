def register():
    username = input("Please input the first 2 letters of your first name and your birth year ")
    password = input("Please input your desired password ")
    file = open("Login.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if login():
        print("You are now logged in...")
    else:
        print("You aren't logged in!")
    
def login():
    username = input("Please enter your username")
    password = input("Please enter your password")  
    for line in open("Login.txt","r").readlines(): 
        login_info = line.split() 
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            return True
            plagarism()
    print("Incorrect credentials.")
    return False
def  choose():
    choice=int(input("""Press 1 for register:
    Press 2 for login"""))
    if choice ==1:
        return register()
    elif choice ==2:
        return login()
    else:
        return"type error"
    
choose()
