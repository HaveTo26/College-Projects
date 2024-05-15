from tkinter import *
import billing as b
import pizza1 as p

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

def addingtobasket(menu,basket,basketprice): #user ordering   
    print(TextColor.GREEN, TextColor.BOLD,"welcome to the pizza shop")
    print("=============================================================================================", TextColor.RESET)
    print(TextColor.CYAN,"Menu:")
    print(menu,TextColor.RESET)
    pick = str(input("What pizza would you like (X to continue to checkout)"))
    if pick in menu: # adds their desired item
        basket.append(pick)
        price = menu[pick]
        b.bill.append(pick)
        b.costs.append(price)
        p.neworder.append(pick)
        basketprice = basketprice + price
        print(basketprice, basket)
        addingtobasket(menu,basket,basketprice)
    elif pick.lower() == "x": # goes onto paying
        if len(basket) < 1:
            print(TextColor.RED, "Your basket is empty", TextColor.RESET)
            addingtobasket(menu, basket, basketprice)
        print("your current order is:",basket)
        while len(basket) > 5:
            if str(input("Are you sure you want to order that many pizzas?")).lower() == "yes":
                break
            else:
                print(TextColor.RED + "Clearing your basket...")
                basket.clear()
                b.bill.clear()
                b.costs.clear()
                p.neworder.clear()
                basketprice = 0
                print(TextColor.BLUE + "Returning to ordering..." + TextColor.RESET)
                addingtobasket(menu, basket,basketprice)
        if str(input("Are you finished?")).lower() == "yes":
            print(TextColor.BLUE + "Your total is £",basketprice, TextColor.RESET)
            while basketprice > 40:
                print(TextColor.PURPLE + "You are valid for a 10% discount!" + TextColor.RESET)
                b.old = basketprice # assigns the previous total to a new variable
                basketprice = basketprice * 0.9 # new final price
                print(TextColor.BLUE,"Your total is now £", basketprice, TextColor.RESET)
                break
            print(TextColor.GREEN + "Your order is", basket, TextColor.RESET)
            paymentinfo = input(TextColor.BOLD + "Enter your card number" + TextColor.RESET)
            if paymentinfo.isalpha() == True:
                print("Invalid input")
                print(TextColor.UNDERLINE,"Ending for security purposes...", TextColor.RESET)
                basket.clear()
                b.bill.clear()
                b.costs.clear()
                p.neworder.clear()
            else:
                print("Thank you for ordering!")
                print(b.bill)
                print(b.costs, "total: £", b.old, "Final Total: £", basketprice)
                p.customerorders.append(p.neworder)
                p.currentorder.append(p.neworder) # send the order to the kitchen to be made
                p.neworder.clear()
                basket.clear()
                b.bill.clear()
                b.costs.clear()
        else: # goes back to adding items
            addingtobasket(menu,basket,basketprice)
    else: # goes back to adding items
        print(TextColor.RED + "That is not in the menu")
        print("please try again" + TextColor.RESET)
        addingtobasket(menu,basket,basketprice)

# doesnt go back to selector because a customer shouldnt be able to edit the menu etc