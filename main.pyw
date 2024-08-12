### MAKE A GAME DOC FOR IMPLEMENTATION ###

### OTHER FILES IMPORTS FOR FUNCTIONS ###


import tkinter as tk
from tkinter import *
import math
from math import *
import time 
from time import *


#Using Threading for incrementing
#Maybe multiprocessing would be more useful to switch to as the game expands (?) not 100% sure
import threading 

root = tk.Tk()
root.geometry("1080x720")
root.title("My Game :>")
root.config(bg="#000000")
root.resizable(1,1)

### FRAMES ###
infoframe = Frame(root, bg="#000000", width=1080, height=125)
infoframe.pack(fill=BOTH, expand=True)
infoframe.grid_propagate(0)
moneyFrame = Frame(root, bg="#000000", width=1080, height=(720-125))
moneyFrame.pack(fill=BOTH, expand=True)
moneyFrame.grid_propagate(0)
moneyFrame.tkraise()

upgFrame  = Frame(root, bg="#032234", width=1080, height=(720-125))
upgFrame.pack(fill = BOTH, expand = True)
upgFrame.grid_propagate(0)




###FRAME TRANSITIONS###

font_type = 'Comic Sans MS'
font_size = 13

money = 20.0

### GAME CODE ###
# VARIABLES #
buy_1_amnt = 0.0
buy_1_cost = 10.0 + (buy_1_amnt ** 1.1)
increment_amount = 0
currency_label = tk.Label(infoframe, text=("${:.7}".format(money)), font=(font_type, font_size), fg="#3f2", bg="#000", width=20, height=6)


### FUNCTIONS ###
def poor(button):
    button.configure(text="Too Poor!")
    sleep(0.1)

### Buyable function, make into a class probably ###
def buy_1():
    global money
    global buy_1_amnt
    global buy_1_cost
    global increment_amount
    if money >= buy_1_cost:
        money -= buy_1_cost
        buy_1_amnt += 1
        buy_1_cost = 10.0 + ((sqrt(3) * buy_1_amnt) ** 1.3)
        increment_amount = (buy_1_amnt * 0.1)
        buyable_1.configure(text="Cost: ${:.7}".format(buy_1_cost))
    else:
        ###FIGURE OUT HOW TO MAKE A WAY TO ALERT USER THEY ARE BROKE###
        buyable_1.configure(text="Cost: ${:.7}".format(buy_1_cost))

def increment_stuff():
    global money #defined on Line 33
    while True:
        money += increment_amount
        sleep(0.033) ##30 updates/second, might set to 60, or 100 idk
        currency_label.configure(text="${:.7}".format(money))
        currency_label.grid(row=0, column=0, padx=10, pady=10)

#CREATE BUYABLES#

buyable_1 = tk.Button(moneyFrame, text= "Cost: ${:.7}".format(buy_1_cost), font=(font_type, font_size - 2), fg="#3f2", bg="#000", height=3, command = buy_1) 
buyable_1.grid(row=0, column=0, padx=100, pady=75)

threading.Thread(target=increment_stuff, daemon=True).start()





root.mainloop()
