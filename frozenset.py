def display_menu():
    print("\n spend an option:\n")
    print("1.view frozenset")
    print("2.add element")
    print("3.remove element")
    print("4.save frozenset to file")
    print("5.load frozenset from file")
    print("6.exit")
    

def save_to_file(fs,file_name="frozenset_data.txt"):
    with open(file_name,"w") as file:
        for item in fs:
            file.write(str(item)+"\n")
        print ("saved a file")
        
        
def load_from_file():
    try:
        with open("frozen_data.txt","r") as file:
            items = [line.strip()for line in file]
            return frozenset[items]
    except FileNotFoundError:
        print("file not found.")
        
        return frozenset()
    
def menu_app():
    fs = frozenset(["kiwi","dragon","cherry"])
    while True:
        display_menu
        choice = int(input("ENTER YOUR CHOICE (1-6): ")) 
        if choice ==1:
            print("current frozenset",fs)
            
        elif choice == 2:
            temp_list = list(fs) 
            new_item = input("enter item to add: ")
            temp_list.append(new_item)
            fs = frozenset(temp_list)
            print(f"'{new_item}' added")     
            
        elif choice == 3:
            temp_list = list(fs)
            remove_item = input("enter an item to remove: ") 
            if remove_item in temp_list:
                temp_list.remove(remove_item)
                fs = frozenset(fs)
                print(f"'{remove_item}' is removed")
            else:
                print(f"{remove_item} not found in frozenset")
                
        elif choice == 4:
            save_to_file(fs)
            
        elif choice == 5:
            fs = load_from_file(fs)
            print("frozenset loaded",fs)
            
        elif choice == 6:
            print("Existing The Frozenset Application. Bye, Take Care!")
            break
        else:
            print("Invalid Choice. Try Again")
            
            
menu_app()
            
