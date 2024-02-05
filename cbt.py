# assignment
# online cbt center 
# questions and answer
# how many students do u want to register
# names of the students, matric number and subjects
# let students take their test. ask number of questions given and answers
# the questions and answers should be in a tuple 
# list of students name and score
# call the students to take their test and store their score
# print the student with the maximum mark, the score and and an award of schoolarship

print("""
Good morning Principal
Welcome to the Online CBT Test
""")
x=1
number_of_students= int(input("How many students are taking the test:"))
number_of_questions= int(input("How many questions do you want the students to answer:"))
user= input("""
1. Enter list of students
2. Exit

Choose option:""")
names_of_students= []
if user=="1":
    while True:
        lists_options= input("""
        1. Create The lists of student's names
        2. View the names of Students
        3. Edit the name of Students
        4. Remove a name(s) of students
        5. Delete the list of stundet's names
        6. Exit.
        7. Proceed 
        Pick an option: """)
        if lists_options=="1":
            while True:
                add_names= input(f"""
                 
                Enter number {x} name: """)
                names_of_students.append(add_names)
                # if x>=number_of_students:
                #     print("ok")
                x+=1
                if x==number_of_students+1:
                    break
            
        elif lists_options=="2":
            print(names_of_students)
        elif lists_options=="3":
            edit_name= input("""
            Name that you want to edit
            
            answer: """)
            if edit_name in names_of_students:
                editted_name=input("Enter the correct name: ")
                print("Name Editted")
                names_of_students.remove(edit_name)
                names_of_students.append(editted_name)
        elif lists_options=="4":
            name_remove=input("What name do you want to remove: ")
            if name_remove in names_of_students:
                print("done")
            else:
                print("Name to be romeved not found in the database")
            names_of_students.remove(name_remove)
            if names_of_students== number_of_students:
                print("Incoplete number of students")
        elif lists_options=="5":
            names_of_students= []
        elif lists_options=="6":
            exit()
       
        elif lists_options=="7":
            ques=[]
            ans=[]
            x=1
            while True:
                question=input(f"""
            Enter question {x} : """)
                ques.append(question)
                answer=input(f"Enter answer for question {x} : " )
                ans.append(answer)
                x+=1
                if x==number_of_students*number_of_questions + 1:
                    break
            for items in names_of_students:
                ready= input(f"""{items}, are you ready for your test?
            
            if ready, type yes: """)
                y=0
                if ready=="yes":  
                    x=1 
                    for quest in ques:
                        print(f"{x}. {quest}")
                        x+=1
                        student_answer= input("Answer: ")
                        for answ in ans:
                            if student_answer==answ:
                                y+=2
                    else:
                        y+=0
                    print(f"{items}, your total score is {y}")
        if lists_options=="7":
            break  
         
                
                
else:
    exit()