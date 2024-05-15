from tkinter import *
import pizza1 as s

def fulfilling(currentorder): #kitchen staff 
    complete = False
    while complete == False: #loops
        print (currentorder)
        inp = str(input("Which items are yet to be cooked? ('done' if none remain)"))
        if inp.lower() == "done":
            complete = True
            currentorder.clear()
            print("good")
            print("Send to delivery")
            import main as m
            m.windowing()
        elif inp in currentorder:
            currentorder.remove(inp)
        elif currentorder == []:
            print("Order seems to be completed")
            complete = True #ends when the list is empty
            m.windowing()
        else:
            print("invalid: input not found")
