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

        self.callback = callback #so we can callback into main
        #the button to confrim and start the calulation
        self.send_button = ctk.CTkButton(self, text="Send Info", command=self.send_info)
        self.send_button.place(x=20, y=120)
        
        #labels starting text
        self.total_label = ctk.CTkLabel(self,text="Nothing yet")
        self.diamond_label = ctk.CTkLabel(self,text="Nothing yet")

        #placing out the labels onto the gui
        self.total_label.place(x=170, y=120)
        self.diamond_label.place(x=335, y=120)

        # arays of options 
        self.minions = ["select minion","Snow","Diamond","Melon","Potato","Pumpkin"]
        self.fuels = ["select fuel","Enchated lavabucket","Catalysts","Tasty Cheese","Hamster wheel"]
        self.teirs = ["select teir","1","2","3","4","5","6","7","8","9","10","11","12"]
        self.amount = ["select amount","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25",
        "26","27","28","29","30","31"]
        self.upgrades = ["select upgrade","Super_Compactor","Diamond_Spreading","Flycatcher"]
        
        self.geometry("1080x250")
        #the dropdownmenues
        self.dropdown_minion = ctk.CTkOptionMenu(self, values=self.minions)
        self.dropdown_amount = ctk.CTkOptionMenu(self, values=self.amount)
        self.dropdown_teir = ctk.CTkOptionMenu(self, values=self.teirs)
        self.dropdown_fuel = ctk.CTkOptionMenu(self, values=self.fuels)
        self.dropdown_upgrade1 = ctk.CTkOptionMenu(self, values=self.upgrades)
        self.dropdown_upgrade2 = ctk.CTkOptionMenu(self, values=self.upgrades)
        #menu placements
        self.dropdown_minion.place(x=0,y=0)
        self.dropdown_fuel.place(x=140,y=0)
        self.dropdown_teir.place(x=300,y=0)
        self.dropdown_upgrade1.place(x=440,y=0)
        self.dropdown_upgrade2.place(x=590,y=0)
        self.dropdown_amount.place(x=750,y=0)
        #taking the manu into their coresponding functions
        self.dropdown_minion.configure(command=self.minion_select)
        self.dropdown_teir.configure(command=self.tier_sellect)
        self.dropdown_fuel.configure(command=self.fuel_select)
        self.dropdown_upgrade1.configure(command=self.upgrade_select1)
        self.dropdown_upgrade2.configure(command=self.upgrade_select2)
        self.dropdown_amount.configure(command=self.amount_select)
    
    #used to update the labels that are meant to show the result from the minion output
    def update_results(self,total_profit,diamond_profit):
        print(total_profit,diamond_profit)
        self.total_label.configure(text=f"Total revenue: {total_profit:,.2f}")
        self.diamond_label.configure(text=f"From diamond Spreading: {diamond_profit:,.2f}")

    #sends back the data to main
    def send_info(self):
        if self.callback:
            data = {
                "minion": self.minion,
                "teir": self.teir,
                "fuel": self.fuel,
                "upgrade1": self.upgrade1,
                "upgrade2": self.upgrade2,
                "amount": self.amount
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

    def amount_select(self,choice):
        print("amount selected",choice)
        self.amount = choice
