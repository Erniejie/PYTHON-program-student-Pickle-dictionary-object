#Python program student Pickle dictionary object

import pickle

def set_data():
    rollno= int(input("Enter Enrollment Number:"))
    name = input("Enter Name: ")
    exam = int(input("Enter Examination Score:"))
    print ()
    student = {}

    student["rollno"] = rollno
    student["name"] = name
    student["exam_mark"] = exam
    return student

def display_data(student):
    print("Roll Number:",student["rollno"])
    print("Name:",student["name"])
    print("Examination Score:",student["exam_mark"])
    print()

def newcreat():
    outfile = open("student1.dat","ab")
    pickle.dump(set_data(),outfile)
    outfile.close()

def dataentry():
    recfile = open("student1.dat","rb")
    while True:
        try:
            student = pickle.load(recfile)
            display_data(student)
        except EOFError:
            break
    recfile.close()

def recordsearch():
    recfile = open("student1.dat","rb")
    rollno=int(input("Enter rollno to Search:"))
    flag = False
    while True:
        try:
            student = pickle.load(recfile)
            if student["rollno"]== rollno:
                display_data(student)
                flag = True
                break
        except EOFError:
            break
    if flag == False:
        print("Record Not Found")
        print()
    recfile.close()
def main_menu():
    print("Main Menu")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Search a Record")
    print("4. Exit")

def main():
    while(True):
        main_menu()
        option = input("Enter Option(1-4):")
        print()

        if option == "1":
            newcreat()
        elif option == "2":
            dataentry()
        elif option == "3":
            recordsearch()
        elif option == "4":
            break
        else:
            print("Invalid Input")

main()
        

    


    
