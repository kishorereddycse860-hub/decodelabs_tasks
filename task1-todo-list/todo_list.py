my_tasks=[]
while True:
    
    print("====TO-DO-LIST====")
    print("1.Add a task:")
    print("2.View all tasks:")
    print("3.Exit")
    choice=input("choose an option(1/2/3):")
    
    if choice =="1":
        task = input("Enter the task you want to add:")
        my_tasks.append(task)
        print(f"'{task}' has been added.")
    elif choice =="2":
        if not my_tasks:
            print("your TO-DO LIST is empty.")
        else:
            for index,task in enumerate(my_tasks):
                print(f"{index + 1}.{task}")
    elif choice =="3":
        print("goodbye!")
        break
    else:
        print("Invalid Choice")
