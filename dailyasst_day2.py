#RECTANGLE_AREA
a=int(input("assign rectangle length: "))
b=int(input("assign rectangle bredth: "))
area=a*b
print(f"The area is {area}")



#PASSWORD_LOGIN
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



#PRIME-OR-NOT
import math

def search_prime(n):

    if(n==2):

        return True

    if(n%2==0):

        return False

    i=3

    while(i<=math.sqrt(n)):

        if(n%i==0):

            return False

        i+=2

    return True

def main():

    n=int(input("Enter a number: "))

    val=search_prime(n)

    print(val)



main()


#NET SALARY_ALLOWANCE
def Tax(a,b,c):
    b*=12
    c*=12

    if a<=500000:
        d=10
        print(f"the tax needed to pay is {d}%")
        tax=(d/100)*a
        tax+=b
        tax+=c
        a-=tax
        print(f"the inhand salary per annum is : {a}")
        print("the inhand salary per month is :",end=" ")
        return a/12
    else:
        d=20
        print(f"the tax needed to pay is {d}%")
        tax=(d/100)*a
        tax+=b
        tax+=c
        a-=tax
        print(f"the inhand salary per annum is : {a}")
        print("the inhand salary per month is : ",end=" ")
        return a/12



Gross=int(input("Enter the Gross salary : "))
Allovances=int(input("Enter the allovances in salary : "))
personal_fund=int(input("Enter the personal fund : "))
print(Tax(Gross,personal_fund,Allovances))


# def main():
#     salary=int(input("Enter your salary: "))
#     if(salary>=500000):
#         tax=0.2*salary
#         salary=salary-tax
#     elif(salary<500000):
#         tax=0.1*salary
#         salary=salary-tax
#     print("Salary after tax deduction: ",salary)
# main()




#CALCULATE_ATTENDENCE
def main():
    number_of_classes=int(input("Enter the number of classes: "))
    classes_attended=int(input("Enter the number of classes attended: "))
    attendance=(classes_attended/number_of_classes)*100
    if(attendance>=75):
        print(f"your attendence is {attendance}")
        print("You are allowed to sit in the exam")
    else:
        print(f"your attendence is {attendance}")
        print("You are not allowed to sit in the exam")

main()