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

