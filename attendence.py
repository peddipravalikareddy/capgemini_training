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