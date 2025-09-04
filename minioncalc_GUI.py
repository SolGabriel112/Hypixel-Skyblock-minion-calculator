import customtkinter as ctk
import requests
import json

minions = ["select minion","Cobblestone","Diamond","Melon","Potato","Pumpkin"]
fuels = ["select fuel","Enchated lavabucket","Catalysts","Chesse","Hamster wheel"]
teirs = ["select teir","1","2","3","4","5","6","7","8","9","10","11","12"]
upgrades = ["select upgrade","Super_compactor","Diamond spreading","Flycatcher"]

app = ctk.CTk()
dropdown_minion = ctk.CTkOptionMenu(app, values=minions)
dropdown_teir = ctk.CTkOptionMenu(app, values=teirs)
dropdown_fuel = ctk.CTkOptionMenu(app, values=fuels)
dropdown_upgrade1 = ctk.CTkOptionMenu(app, values=upgrades)
dropdown_upgrade2 = ctk.CTkOptionMenu(app, values=upgrades)

dropdown_minion.place(x=0,y=0)
dropdown_fuel.place(x=150,y=0)
dropdown_teir.place(x=300,y=0)
dropdown_upgrade1.place(x=450,y=0)
dropdown_upgrade2.place(x=600,y=0)

output_label = ctk.CTkLabel(app, text="")
output_label.place(x=450,y=100)

button = ctk.CTkButton(app, text="calculate")
button.place(x=450,y=150)

minion = ""
fuel = ""

app.geometry("900x700")


def calculate():
    result = 20+40*30
    output_label.configure(text=result)

    print("calculations made")

def minion_select(choice):
    print("minion selected:",choice)
    minion = choice

def fuel_select(choice):
    print("fuel selected:",choice)
    fuel = choice

def tier_sellect(choice):
    print("teir selected:",choice)
    teir = choice

def upgrade_select1(choice):
    print("upgrade1 selected:",choice)
    upgrade1 = choice

def upgrade_select2(choice):
    print("upgrade2 selected:",choice)
    upgrade2 = choice
            
dropdown_minion.configure(command=minion_select)
dropdown_teir.configure(command=tier_sellect)
dropdown_fuel.configure(command=fuel_select)
dropdown_upgrade1.configure(command=upgrade_select1)
dropdown_upgrade2.configure(command=upgrade_select2)
button.configure(command=calculate)

app.mainloop()
