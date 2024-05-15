from tkinter import *

class TextColor:
  RESET = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  WHITE = '\033[97m'

def viewing(customerorders): #views orders
    viewed = input("what is the number of the order you want to view? ('return' to return to selector)")
    if viewed.isdigit() == True:
        if int(viewed) <= len(customerorders):
            print(customerorders[int(viewed)])
            if str(input("would you like to view another")) == "yes":
                viewing(customerorders)
            else:    
                print("Returing to selector")
        else:
            print("Out of range...")
            viewing(customerorders)
    elif viewed == "return":
        import main as m
        m.windowing()
    else:
        print("Invalid")
        print("Please enter a", TextColor.BOLD + "number" + TextColor.RESET)
        viewing(customerorders)

def sales(basket,customerorders): #asks their intented action
    import main as m
    a = False
    while a == False:
        choice = str(input("Would you like to view an existing order or edit the menu? ('return' to return to selector)"))
        if choice == "view":
            viewing(customerorders)
        elif choice == "edit":
            pizzaing(basket)
        elif choice == "return":
            import main as m
            m.windowing()
        else: 
            print("invalid input")
            sales(basket, customerorders)

def pizzaing(basket): #editing menu
    done = False
    print(basket)
    action = str(input("do you want to edit, remove, or add a new one? (end to end) "))  
    if action == "edit":
        print(basket)
        action = str(input("which pizza would you like to edit"))
        if action in basket:
            basket.pop(action)
            updates = input("update the title")
            updatesnum = int(input("update the price"))
            basket.update({updates: updatesnum})
            print("the menu is now", basket)
            pizzaing(basket)
        else:
            print("Pizza not found")
            pizzaing(basket)
    elif action == "add":
        change = input("Type the name of the pizza you want to add")
        value = int(input("Enter the value: "))
        basket.update({change: value})
        print("the menu is now",basket)
        pizzaing(basket)
    elif action == "end":
        done = True
    elif action == "remove":
        change = str(input("Which do you want to remove"))
        if change in basket:
            basket.pop(change)
            pizzaing(basket) #removes a pizza from the menu entirely
        else:
            print("invalid input")
            pizzaing(basket)
    else:
        print("invalid action")
        pizzaing(basket)