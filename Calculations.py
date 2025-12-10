import requests
import json

class Calc:
    def __init__(self, data):
        self.data = data

    def meth_chossen_upgrade1(self):
        data = self.data
        #checks what went into upgrade slot 1
        match data["upgrade1"]:
            case "Super_Compactor":
                print("Supercompector")
                return "Super_Compactor"
            case "Diamond_Spreading":
                print("Diamond_spreading")
                return "Diamond_Spreading"
            case "Flycatcher":
                print("Flycatcher")
                return("Flycatcher")

    def meth_chossen_upgrade2(self):
        data = self.data
        #checks what went into upgrade slot 2
        match data["upgrade2"]:
            case "Super_Compactor":
                print("Supercompector")
                return "Super_Compactor"
            case "Diamond_Spreading":
                print("Diamond_spreading")
                return "Diamond_Spreading"
            case "Flycatcher":
                print("Flycatcher")
                return("Flycatcher")

    def meth_chossen_teir(self):
        data = self.data
        #checks which teir of the minion was selected
        match data["teir"]:
            case "1":
                print("1")
                return "1"

            case "2":
                print("2")
                return "2"

            case "3":
                print("3")
                return "3"

            case "4":
                print("4")
                return "4"

            case "5":
                print("5")
                return "5"

            case "6":
                print("6")
                return "6"

            case "7":
                print("7")
                return "7"

            case "8":
                print("8")
                return "8"

            case "9":
                print("9")
                return "9"

            case "10":
                print("10")
                return "10"

            case "11":
                print("11")
                return "11"

            case "12":
                print("12")
                return "12"

    def meth_chossen_fuel(self):
        data = self.data
        #checks which fuel it is that has been selected
        match data["fuel"]:
            case "Enchated lavabucket":
                print("Enchated lavabucket")
                return "Enchated lavabucket"
            case "Catalysts":
                print("Catalysts")
                return "Catalysts"
            case "Tasty Cheese":
                print("Tasty Cheese")
                return "Tasty Cheese"
            case "Hamster wheel":
                print("hamster wheel")
                return "Hamster wheel"
        
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
        data = self.data
        day = 86400
        week = 7
        month = 4
        url = "https://api.hypixel.net/v2/skyblock/bazaar"
        response = requests.get(url)
        api_data = response.json()

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
        print(chossen_minion)
        print(chossen_teir)
        print(chossen_fuel)
        print(chossen_upgrade1)
        print(chossen_upgrade2)
        
        minion = self.data["minion"]# Example: "Pumpkin"
        tier = self.data["teir"]# Example: "5"
        

        base_speed = self.minion_data["minions"][minion]["tiers"][tier]
        speed_multiplier = self.fuel_data[chossen_fuel].get("Fuel_Speed",1)
        item_boost = self.fuel_data[chossen_fuel].get("Item_boost",1)
        base_output = self.minion_data["minions"][minion]["output"]
        upgrade_speed1 = self.upgrade1_data["upgrades"][chossen_upgrade1]["speed_multiplier"]
        upgrade_speed2 = self.upgrade2_data["upgrades"][chossen_upgrade2]["speed_multiplier"]
        item = self.minion_data["minions"][minion]["item"]

        print("Chosen minion:", minion)
        print("Chosen tier:", tier)
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
        print("sellprice:",sellPrice)
        daily_profit = daily_output*sellPrice
        print("daily profit:",daily_profit)
