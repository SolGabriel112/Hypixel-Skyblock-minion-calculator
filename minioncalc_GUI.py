import customtkinter as ctk
import requests
import json
class minoncalc_GUI(ctk.CTk):

    def __init__(self,callback=None):
        super().__init__()
        #varibles to hold the option you choose
        self.minion = ""
        self.fuel = ""
        self.teir = ""
        self.upgrade1 = ""
        self.upgrade2 = ""
        self.choice = ""

        self.app = ctk.CTk()

        self.callback = callback #so we can callback into main
        
        self.send_button = ctk.CTkButton(self, text="Send Info", command=self.send_info)
        self.send_button.place(x=20, y=120)
        # arays of options 
        self.minions = ["select minion","Snow","Diamond","Melon","Potato","Pumpkin"]
        self.fuels = ["select fuel","Enchated lavabucket","Catalysts","Tasty Cheese","Hamster wheel"]
        self.teirs = ["select teir","1","2","3","4","5","6","7","8","9","10","11","12"]
        self.upgrades = ["select upgrade","Super_Compactor","Diamond_Spreading","Flycatcher"]
        
        self.app.geometry("1080x720")
        #the dropdownmenues
        self.dropdown_minion = ctk.CTkOptionMenu(self, values=self.minions)
        self.dropdown_teir = ctk.CTkOptionMenu(self, values=self.teirs)
        self.dropdown_fuel = ctk.CTkOptionMenu(self, values=self.fuels)
        self.dropdown_upgrade1 = ctk.CTkOptionMenu(self, values=self.upgrades)
        self.dropdown_upgrade2 = ctk.CTkOptionMenu(self, values=self.upgrades)
        #menu placements
        self.dropdown_minion.place(x=0,y=0)
        self.dropdown_fuel.place(x=150,y=0)
        self.dropdown_teir.place(x=300,y=0)
        self.dropdown_upgrade1.place(x=450,y=0)
        self.dropdown_upgrade2.place(x=600,y=0)
        #taking the manu into their coresponding functions
        self.dropdown_minion.configure(command=self.minion_select)
        self.dropdown_teir.configure(command=self.tier_sellect)
        self.dropdown_fuel.configure(command=self.fuel_select)
        self.dropdown_upgrade1.configure(command=self.upgrade_select1)
        self.dropdown_upgrade2.configure(command=self.upgrade_select2)
    #sends back the data to main
    def send_info(self):
        if self.callback:
            data = {
                "minion": self.minion,
                "teir": self.teir,
                "fuel": self.fuel,
                "upgrade1": self.upgrade1,
                "upgrade2": self.upgrade2,
            }
            self.callback(data)
    #puts the selected choice into its coresponding self.
    def minion_select(self,choice):
        print("minion selected:",choice)
        self.minion = choice
    
    def fuel_select(self,choice):
        print("fuel selected:",choice)
        self.fuel = choice

    def tier_sellect(self,choice):
        print("teir selected:",choice)
        self.teir = choice

    def upgrade_select1(self,choice):
        print("upgrade1 selected:",choice)
        self.upgrade1 = choice

    def upgrade_select2(self,choice):
        print("upgrade2 selected:",choice)
        self.upgrade2 = choice
