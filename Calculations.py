import requests
import json

class Calc:
    def __init__(self, data):
        self.data = data

    def meth_chossen_upgrade(self):
        print("later")

    def meth_chossen_upgrade2(self):
        print("later")

    def meth_chossen_teir(self):
        data = self.data
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
        match data["fuel"]:
            case "Enchated lavabucket":
                print("Enchated lavabucket")
                return "Enchated lavabucket"
            case "Catalysts":
                print("Catalysts")
                return "Catalysts"
            case "Chesse":
                print("Cheese")
                return "Cheese"
            case "Hamster wheel":
                print("hamster wheel")
                return "haster wheel"
        
    def meth_chossen_minion(self):
        data = self.data
        match data["minion"]:
            case "Melon":
                return "Melon"
            case "Cobblestone":
                print("cobble")
                return "Cobblestone"
            case "Diamond":
                print("diamond")
                return "Diamond"
            case "Potato":
                print("potato")
                return "Potato"
            case "Pumpkin":
                print("pumpkin")
                return "Pumpkin"
    
    def calculate(self):
        data = self.data
        chossen_minion = self.meth_chossen_minion()
        print(chossen_minion)
        chossen_fuel = self.meth_chossen_fuel()
        print(chossen_fuel)
