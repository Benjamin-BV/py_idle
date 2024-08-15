### MAKE A GAME DOC FOR IMPLEMENTATION ###

### OTHER FILES IMPORTS FOR FUNCTIONS ###

import sys
import tkinter as tk
from tkinter import *
import math
from math import *
import time 
from time import *

### Seperating classes ###

from subdir.classes import *



#Using Threading for incrementing


#Maybe multiprocessing would be more useful to switch to as the game expands (?) not 100% sure
import threading 





### FONT SETS ###
font_type = 'Comic Sans MS' ##Funny font lul##
font_size = 13

root = tk.Tk()
root.geometry("1080x720")
root.title("My Game  :>")
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

winframe = Frame(root, bg = "#948372", width = 1080, height = 720)
winframe.pack(fill=BOTH, expand = True)
winframe.grid_propagate(0)
youwin = Label(winframe, text="You WIN! You have reached infinite(Py_INF) money in the game, now we can all go and move on with our day, nothing else to see here...", fg="#fa0", width = 40, height = 18)

### FRAME TRANSITIONS ###



### GAME CODE BEGINS ###

###ADD SOME SORT OF STORY WITH POPUP FRAMES###



# VARIABLES #
money = 15.0
buy_1_amnt = 0.0
buy_1_cost = 10.0 
increment_amount = 0
currency_label = tk.Label(infoframe, text=("${:.7}".format(money)), font=(font_type, font_size), fg="#3f2", bg="#000", width=20, height=6)


### FUNCTIONS ###

### As name sates ###
def poor(button):
    button.configure(text="Too Poor!")
    sleep(0.1)

### Buyable function, make into a class eventually for better structure ###
def buy_1():
    global money
    global buy_1_amnt
    global buy_1_cost
    global increment_amount
    if money >= buy_1_cost:
        money -= buy_1_cost
        buy_1_amnt += 1
        buy_1_cost += ((sqrt(3) * buy_1_amnt) ** 1.3) ##Will be subject to change depending on balancing, maybe upgrades to change the base cost/improve it##
        increment_amount += 0.1
        buyable_1.configure(text="Cost: ${:.7}".format(buy_1_cost))
    else:
        ### FIGURE OUT HOW TO MAKE A WAY TO ALERT USER THEY ARE BROKE *Current function doesn't work, assume because of the sleep function ###
        buyable_1.configure(text="Cost: ${:.7}".format(buy_1_cost))

### Increments money at a constant rate based on total value of all buyables, will probably be jank with upgraders added in but whatever ###
def increment_stuff():
    global money 
    while True:
        if(money == inf):
            winframe.tkraise()
        money += increment_amount
        sleep(0.033) ##30 updates/second, might set to 60, or 100 idk
        currency_label.configure(text="${:.7}".format(money))
        currency_label.grid(row=0, column=0, padx=10, pady=10)

# CREATE BUYABLES #

buyable_1 = tk.Button(moneyFrame, text= "Cost: ${:.7}".format(buy_1_cost), font=(font_type, font_size - 2), fg="#3f2", bg="#000", height=3, command = buy_1) 
buyable_1.grid(row=0, column=0, padx=100, pady=75)



# CREATE UPGRADES #



### MONEY INCREMENT ###
threading.Thread(target=increment_stuff, daemon=True).start()



### CREATE LOCAL SAVEDATA ###



# So it is not static, and has runtime #
root.mainloop()
