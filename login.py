username = input("Enter your username: ") 
password = input("Enter your Password: ")
if (username == "admin"):
    print("login success")

elif (password == "admin" or "Admin@123"):
    print("logged in  success")
else:
    print("please enter valid credentials")
    

