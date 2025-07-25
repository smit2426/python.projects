students =[]

print("\nWilcome to the Student Data Organizer!")

while True:
    print("Select an Option:")
    print("1. Add student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delet Student")
    print("5. Display subjects Offered")
    print("6. Exit")

    choice = input("Enter Your choice: ")

    if choice == "1":
        stdId = input("Student ID: ")
        stdName = input("Name: ")
        stdAge = input("age: ")
        stdgrade = input("Grade: ")
        stdDateofBirth = input("Date of Birth (YYYY-MM-DD): ")

        Newstudent = {
            "id": stdId,
            "name": stdName,
            "age": stdAge,
            "grade": stdgrade,
            "Date of Birth": stdDateofBirth
            }
        students.append(Newstudent)
        print("new Student Added Success")

    elif choice == "2":
        if not students:
            print("no Student Data Found...")
        else:
            print("--------Students List--------")
            for stu in students:
                print(f"id: {stu['id']},Name: {stu['name']},Age: {stu['age']},Grade: {stu['grade']},DateofBirth: {stu['Date of Birth']}")
            print()

    elif choice == "3":
        uId = input("Eneter Update id: ")
        found = False
        for std in students:
            if std["id"] == uId:
                uName = input("Enter name: ")
                uAge = input("enter Age: ")
                ugrade = input("enter grade: ")
                udateofbirth = input("Enter brith date: ")
                if(uName != ""):
                    std["name"] = uName
                if(uAge != ""):
                    std["age"] = uAge
                if(ugrade != ""):
                    std["grade"] = ugrade
                if(udateofbirth!= ""):
                    std["Date of Birth"] = udateofbirth
                print("student is update Success")
                found = True
                break
            if not found:
                print("No student found....")

    elif choice == "4":
       did = input("enter delete Success")
       found = False
       for std in students:
           students.remove(std)
           print("Student is Delete Success")
           found = True
           break

       if not found:
        print("No Stundet Found...")

    elif choice == "5":
        print("Display subjects Offered")

    elif choice == "6":
        print("Exit Progaram")
        break
        
      
   
        
