
user_name= 'hanie'
user_password= '1234'
lock_user = []
for i in range(3):
    username=input("username= ")
    password=input("password= ") 
    if username == user_name and password == user_password:
        print ("welcom!")
        break
    elif user_name != username and user_password != password:
        if i < 2:
            print("your username and password is incorrect! please try again!")
        else:
            lock_user.append(username)
            print("your account is locked!")
            






