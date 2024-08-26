### MAKE A GAME DOC FOR IMPLEMENTATION ###

### OTHER FILES IMPORTS FOR FUNCTIONS ###

import sys
import tkinter as tk
from tkinter import *
import math
from math import *
import time 
from time import *

from subdir.classes import * #Importing classes for object creation

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
frameW = 1920
infoH = 250
frameH = 830

infoframe = Frame(root, bg="#000000", width=frameW, height=infoH)
infoframe.pack(fill=BOTH, expand=True)
infoframe.grid_propagate(0)
infoframe.grid(row = 0)
moneyFrame = Frame(root, bg="#051702", width=frameW, height=frameH)
#moneyFrame.pack(fill=BOTH, expand=True)
moneyFrame.grid_propagate(0)
moneyFrame.tkraise()

upgFrame  = Frame(root, bg="#031214", width=frameW, height=frameH)
#upgFrame.pack(fill = BOTH, expand = True)
upgFrame.grid_propagate(0)
testupg = Button(upgFrame, text="HALLO :>", font=(font_type, font_size - 4), bg="#051702", fg="#dab", width = 15, height = 4)#haha, dab
testupg.grid(row=0,column=0, padx=10, pady=15)
winframe = Frame(root, bg = "#948372", width = frameW, height = frameH)
#winframe.pack(fill=BOTH, expand = True)
winframe.grid_propagate(0)
youwin = Label(winframe, text="You WIN! You have reached infinite(Py_INF) money in the game, now we can all go and move on with our day, nothing else to see here...", fg="#fa0", width = 40, height = 18)
combatframe = Frame(root, bg="#230105", width=frameW, height=frameH)


pages = {moneyFrame, upgFrame, winframe, combatframe}
for f in pages:
    f.grid(row=1, column=0, sticky="swe")#Setting the frames to be sticky to the bottom and width of page, top is for infoFrame
### GAME CODE BEGINS ###

###ADD SOME SORT OF STORY WITH POPUP FRAMES###



# VARIABLES #
money = 15.0
buy_1_amnt = 0.0
buy_1_cost = 10.0 
increment_amount = 0
currency_label = Label(infoframe, text=("${:.7}".format(money)), font=(font_type, font_size), fg="#3f2", bg="#000", width = 8, height = 4)
currency_label.grid(row=0,column=0, pady=10, padx=10)

###ADDING TABS AND FRAME CHANGES###
def push(frame): #FIXED: pages were on different columns :/
    frame.tkraise() #Supposed to raise the frame that is set as argument for push func.

buyable_tab = Button(infoframe,text= "Money Generators" , font=(font_type,font_size-4), fg ="#3f2", bg="#000", height = 2, command= lambda: push(moneyFrame))
buyable_tab.grid(row=1,column=0,padx=10, pady=15)

upgrade_tab = Button(infoframe,text = "Upgrades", font=(font_type,font_size-4), fg ="#3f2", bg="#000", height = 2, command = lambda: push(upgFrame))
upgrade_tab.grid(row=1,column=1,padx=10, pady=15)

combat_tab = Button(infoframe,text= "Combat" , font=(font_type,font_size-4), fg ="#822", bg="#000", height = 2, command= lambda: push(combatframe))
combat_tab.grid(row=1, column=2, padx=10, pady=15)
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
        buy_1_cost += ((sqrt(3) * buy_1_amnt) ** 1.25) ##Will be subject to change depending on balancing, maybe upgrades to change the base cost/improve it##
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
        if(money > 1E12): ##Adding scaling reduction if too rich, going to display near the bottom of the page (Basically stealing taxes from synergism, luv u plat <3)
            money += increment_amount **(0.99 ** math.log10(money/5000))
        money += increment_amount
        sleep(0.033) ##30 updates/second, might set to 60, or 100 idk
        currency_label.configure(text="${:.7}".format(money))
        currency_label.grid(row=0, column=0, padx=10, pady=10)

# CREATE BUYABLES #

buyable_1 = tk.Button(moneyFrame, text= "Cost: ${:.7}".format(buy_1_cost), font = (font_type, font_size - 4), fg = "#3f2", bg = "#000", height = 3, command = buy_1) 
buyable_1.grid(row=0, column=0, padx=20, pady=15)
buyable_2 = tk.Button(moneyFrame, text="PlaceHolder", font=(font_type, font_size - 4), fg = "#3f2", bg = "#000", height = 3)
buyable_2.grid(row=1, column=0, padx= 20, pady= 15)
#buyable_2.set(buyable_2, 314, (pi/2 * buy_2_amnt) ** 1.3, money)


# CREATE UPGRADES #
upg1 = upgrade()
upg1.set(upg1, 1000, buyable_1, "mult", pi, "We've Come Half Circle")
upg1.description("Orobous would be saddened by your lack of drive, with only half the effort, he gives half the reward, 3.14x to the first buyable's production.")

### MONEY INCREMENT ###
threading.Thread(target=increment_stuff, daemon=True).start()



### CREATE LOCAL SAVEDATA ###
#only temp right now, will eventually store in game directory#
savedata = open("SnakeSave.txt", "w")
savedata.write("Money = {:.7}\nBuyable_1_amnt = {:0}".format(money, buy_1_amnt))
savedata.close()

# So it is not static, and has runtime #
push(infoframe)
push(moneyFrame)
root.mainloop()
