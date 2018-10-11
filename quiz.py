def show_menu():
    print("Quiz Game")
    print("----------")
    print("1. Run Quiz")
    print("2. Enter a Question")
    print("3. Exit")
    print()
    
    option = int(input("Enter Option: "))
    return option


while True:    
    option = show_menu()
    if option == 3:
        print("Game ended")
        break
    
    
    
    
    
    



