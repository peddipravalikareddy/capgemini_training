def main():
    salary=int(input("Enter your salary: "))
    if(salary>=500000):
        tax=0.2*salary
        salary=salary-tax
    elif(salary<500000):
        tax=0.1*salary
        salary=salary-tax
    print("Salary after tax deduction: ",salary)
main()