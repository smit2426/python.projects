students = []

while True:
    print("\nWelcome to the Student Data Organizer!")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")
        student = {}
        student['id'] = int(input("Student ID: "))
        student['name'] = input("Name: ")
        student['age'] = int(input("Age: "))
        student['grade'] = input("Grade: ")
        student['Date of Birth'] = input("Date of Birth (YYYY-MM-DD): ")
        
        subjects_input = input("Subjects (comma-separated): ")
        student['subjects'] = [s.strip() for s in subjects_input.split(',')]
        
        students.append(student)
        print("\n Student added successfully!")

    elif choice == "2":
        print("\n--- Display All Students ---")
        if students:
            for stu in students:
                print(f"Student ID: {stu['id']} | Name: {stu['name']} | Age: {stu['age']} | Grade: {stu['grade']} | Date of Birth: {stu['Date of Birth']} | Subjects: {', '.join(stu['subjects'])}")
        else:
            print("No students to display.")

    elif choice == "3":
        update_id = int(input("Enter the Student ID to update: "))
        found = False

        for stu in students:
            if stu['id'] == update_id:
                print(f"Current Data for ID {update_id}:")
                print(f"Name: {stu['name']}, Age: {stu['age']}, Grade: {stu['grade']}, DOB: {stu['Date of Birth']}, Subjects: {', '.join(stu['subjects'])}")

                print("\nEnter new details :")

                new_name = input("New Name: ")
                new_age = input("New Age: ")
                new_grade = input("New Grade: ")
                new_dob = input("New Date of Birth (YYYY-MM-DD): ")
                new_subjects = input("New Subjects (comma-separated): ")

                if new_name:
                    stu['name'] = new_name
                if new_age:
                    stu['age'] = int(new_age)
                if new_grade:
                    stu['grade'] = new_grade
                if new_dob:
                    stu['Date of Birth'] = new_dob
                if new_subjects:
                    stu['subjects'] = [s.strip() for s in new_subjects.split(',')]

                print("Student information updated successfully!")
                found = True
                break
        
        if not found:
            print(" Student ID not found.")
    elif choice == "4":
       did = input("enter delete Success:")
       found = False
       for std in students:
           students.remove(std)
           print("Student is Delete Success")
           found = True
           break

       if not found:
        print("No Stundet Found...")


    elif choice == "5":
        print("\n--- Subjects Offered ---")
        all_subjects = set()
        for stu in students:
            all_subjects.update(stu.get('subjects', []))
        
        if all_subjects:
            print("Subjects offered across all students:")
            for subject in sorted(all_subjects):
                print(f"- {subject}")
        else:
            print("No subjects found.")

    elif choice == "6":
        print("Exiting the program")
        break

'''
Welcome to the Student Data Organizer!
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1

Enter student details:
Student ID: 100
Name: smit
Age: 18
Grade: a+
Date of Birth (YYYY-MM-DD): 2008-02-08
Subjects (comma-separated): sci,guj,eng

 Student added successfully!

Welcome to the Student Data Organizer!
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1

Enter student details:
Student ID: 101
Name: akshat
Age: 19
Grade: b+
Date of Birth (YYYY-MM-DD): 2007-06-01
Subjects (comma-separated): sci,eng,a\c,eco

 Student added successfully!

Welcome to the Student Data Organizer!
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 2

--- Display All Students ---
Student ID: 100 | Name: smit | Age: 18 | Grade: a+ | Date of Birth: 2008-02-08 | Subjects: sci, guj, eng
Student ID: 101 | Name: akshat | Age: 19 | Grade: b+ | Date of Birth: 2007-06-01 | Subjects: sci, eng, a\c, eco

Enter your choice: 3
Enter the Student ID to update: 100
Current Data for ID 100:
Name: smit, Age: 18, Grade: a+, DOB: 2008-02-08, Subjects: sci, guj, eng

Enter new details :
New Name: s
New Age: 19
New Grade: S+
New Date of Birth (YYYY-MM-DD): 2008-02-08
New Subjects (comma-separated): sci,eco,eng,guj
Student information updated successfully!

Enter your choice: 2

--- Display All Students ---
Student ID: 100 | Name: s | Age: 19 | Grade: S+ | Date of Birth: 2008-02-08 | Subjects: sci, eco, eng, guj
Student ID: 101 | Name: akshat | Age: 19 | Grade: b+ | Date of Birth: 2007-06-01 | Subjects: sci, eng, a\c, eco

Enter your choice: 4
enter delete Success:101
Student is Delete Success

Enter your choice: 5

--- Subjects Offered ---
Subjects offered across all students:
- a\c
- eco
- eng
- sci

Enter your choice: 6
Exiting the program


'''
