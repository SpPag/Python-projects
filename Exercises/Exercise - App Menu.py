while True:
    options = "1. Option A\n2. Option B\n3. Exit\n"
    print(options)
    answer = input("please type the number that corresponds to your choice: ")
    while answer != "1" and answer != "2" and answer != "3":
        answer = input("please type the number that corresponds to your choice: ")
    if answer == "1":
        print("\nOption A\n")
    elif answer == "2":
        print("\nOption B\n")
    else:
        break
print("\nThank you for using our app, we hope to see you again.")
