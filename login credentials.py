attempts=3
while attempts>0:
    a=input("enter the user ID: ")
    b=input("enter the password : ")
    if a=='testuser' and b=='Password@123':
         print(f"{a} successfully logedin")
         break
    elif  attempts>1:
         print("invalid userid or password")
         attempts=attempts-1
    else:
         print("try after some time you have reached max attempts")
