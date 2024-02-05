print("My To-Do list Application".center(100))
user =input("""
    1. Create a To-Do list
    2. Exit

    Choose option:""")
todo_list=[]
if user=="1":
    
    while True:
        
        todo_option= input("""
        1. Add to list
        2. Edit an item
        3. Remove an item
        4. Delete list
        5. View To-Do list
        6. Exit


        chooes option: """)
        if todo_option=="1":
            add_list= input("""
        
            Add To-Do:""")
            todo_list.append(add_list)
        elif todo_option=="2":
            user= int(input("""
            Item number what are you editing
            
            answer: """))
            if user:
                todo_list[user -1]=input(f"Editing {todo_list[user -1]} ")
                num=1
            for item in todo_list:
                print(f"""
            {num}.{item}
                """)
                num+=1
            else:
                print("invalid option")
        # elif todo_option=="3":
            
        elif todo_option=="5":
            num=1
            for item in todo_list:
                print(f"""
            {num}.{item}
                """)
                num+=1
        elif todo_option=="6":
            exit()
        
elif user=="2":
    exit()
else:
    print("Invalid")