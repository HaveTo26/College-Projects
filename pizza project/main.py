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

import pizza1 as a
import user as u
import kitchen as k
import sales as s

def windowing(): # starting menu 
    window = Tk()
    window.title("User Selector")
    window.geometry("300x300")

    label = Label(window, text="Are you:", font=("Comic Sans MS",20))
    label.pack()

    customer_button = Button(window, text= "Customer", command=lambda: u.addingtobasket(a.basket, a.menu, a.basketprice), height=3, width=100)
    customer_button.pack()

    sales_button = Button(window, text="Sales/Marketing", command=lambda: s.sales(a.basket, a.customerorders), height=3, width=100)
    sales_button.pack()

    kitchen_button = Button(window, text="Kitchen", command=lambda: k.fulfilling(a.currentorder), height=3,width=100)
    kitchen_button.pack()

    quit_button = Button(window, text="Exit", command=window.destroy, height=5, width=100)
    quit_button.pack()

    window.mainloop()

windowing()