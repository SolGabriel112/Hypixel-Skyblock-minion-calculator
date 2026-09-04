import requests
import json

class Calc:
    def __init__(self, data):
        self.data = data
    
    def meth_chossen_amount(self):
        data = self.data
        #sends out how many minions
        #potential other way to do this
        chossen_varible = data["amount"]
        if chossen_varible == "select amount" or chossen_varible == "_":
            chossen_varible = "1"
            return chossen_varible
        else:
            return chossen_varible

    def meth_chossen_upgrade1(self):
        data = self.data
        #checks what went into upgrade slot 1
        chossen_varible = data["upgrade1"]
        if chossen_varible == "select upgrade" or chossen_varible == "_":
            chossen_varible = "Super_Compactor"
            return chossen_varible
        else:
            return chossen_varible


    def meth_chossen_upgrade2(self):
        data = self.data
        #checks what went into upgrade slot 2
        chossen_varible = data["upgrade2"]
        if chossen_varible == "select upgrade" or chossen_varible == "_":
            chossen_varible = "Super_Compactor"
            return chossen_varible
        else:
            return chossen_varible


    def meth_chossen_teir(self):
        data = self.data
        #checks which teir of the minion was selected
        chossen_varible = data["teir"]
        if chossen_varible == "select teir" or chossen_varible == "_":
            chossen_varible = "11"
            return chossen_varible
        else:
            return chossen_varible

    def meth_chossen_fuel(self):
        data = self.data
        #checks which fuel it is that has been selected
        chossen_varible = data["fuel"]
        if chossen_varible == "select fuel" or chossen_varible == "_":
            chossen_varible = "NO_FUEL"
            return chossen_varible
        else:
            return chossen_varible
        
    def meth_chossen_minion(self):
        data = self.data
        #checks which minion it is that has been selected
        match data["minion"]:
            case "Melon":
                return "Melon"
            case "Snow":
                print("snow")
                return "Snow"
            case "Diamond":
                print("Diamond")
                return "Diamond"
            case "Potato":
                print("potato")
                return "Potato"
            case "Pumpkin":
                print("pumpkin")
                return "Pumpkin"
    
    def calculate(self):
        data = self.data
        day = 86400
        amount_dia = 0
        profit_diamond = 0
        #chossen_varibles used for the api 
        url = "https://api.hypixel.net/v2/skyblock/bazaar"
        response = requests.get(url)
        api_data = response.json()
        #opens up the different Json files with the data
        with open("minions.json") as f:
            self.minion_data = json.load(f)
        with open("fuels.json") as fuel:
            self.fuel_data = json.load(fuel)
        with open("upgrades.json") as upgrade1:
            self.upgrade1_data = json.load(upgrade1)
        with open("upgrades.json") as upgrade2:
            self.upgrade2_data = json.load(upgrade2)
        
        #grabs the infomation sent over so it can later be used
        chossen_minion = self.meth_chossen_minion()
        chossen_fuel = self.meth_chossen_fuel()
        chossen_teir = self.meth_chossen_teir()
        chossen_upgrade1 = self.meth_chossen_upgrade1()
        chossen_upgrade2 = self.meth_chossen_upgrade2()
        chossen_amount = self.meth_chossen_amount()
        print(chossen_minion)
        print(chossen_teir)
        print(chossen_fuel)
        print(chossen_upgrade1)
        print(chossen_upgrade2)
        
        minion = self.data["minion"]# Example: "Pumpkin"
        tier = self.data["teir"]# Example: "5"
        #matches the different chossen_varibles with the the data from the json files
        base_speed = self.minion_data["minions"][chossen_minion]["tiers"][chossen_teir]
        speed_multiplier = self.fuel_data[chossen_fuel].get("Fuel_Speed",1)
        item_boost = self.fuel_data[chossen_fuel].get("Item_boost",1)
        base_output = self.minion_data["minions"][minion]["output"]
        upgrade_speed1 = self.upgrade1_data["upgrades"][chossen_upgrade1]["speed_multiplier"]
        upgrade_speed2 = self.upgrade2_data["upgrades"][chossen_upgrade2]["speed_multiplier"]
        item = self.minion_data["minions"][minion]["item"]

        #just alot of debug print satements that will be removed later on
        #and some important math that will be kept
        print("Chosen minion:", chossen_minion)
        print("Chosen tier:", chossen_teir)
        print("Base speed:", base_speed)
        print("Speed Multiplier:",speed_multiplier)
        print("Item_boost:",item_boost)
        print("item output:",base_output*item_boost)
        final_output = base_output*item_boost
        print("final output",final_output)
        print("uprage1:",upgrade_speed1)
        print("uprage2:",upgrade_speed2)
        speed_with_fuel = base_speed * speed_multiplier*upgrade_speed1*upgrade_speed2
        print("final speed:",speed_with_fuel)
        affective_actions = day/speed_with_fuel
        print(affective_actions)
        daily_output = affective_actions*final_output
        print("daily output:",daily_output)
        print("item:",item)
        product = api_data["products"][item]
        sellPrice = product["quick_status"]["sellPrice"]
        print("sell price:",sellPrice)

        print(int(chossen_amount))
        #if they have diamond spreading
        if chossen_upgrade1 == "Diamond_Spreading" or chossen_upgrade2 == "Diamond_Spreading":
            amount_dia = daily_output/10
            product = api_data["products"]["DIAMOND"]
            sellPrice_diamond = product["quick_status"]["sellPrice"]
            profit_diamond = amount_dia*sellPrice_diamond*int(chossen_amount)

        daily_profit = ((daily_output*sellPrice)*int(chossen_amount))+profit_diamond

        return{
            "total_profit":daily_profit,
            "diamondspreading":profit_diamond
        }
