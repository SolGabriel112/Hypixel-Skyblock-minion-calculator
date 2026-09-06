from minioncalc_GUI import minoncalc_GUI
from Calculations import Calc
import requests
import json
import os
Main_Data = "test"
#saves the results so you can look at the diffrent results and compare more easily
def save_results(new_data):
    #will save what minion and how much it made to a json file
    #so everything can be much more easily compeared afterwards incase you do alot at one time
    if os.path.exists("results.json"):
        with open("results.json", "r") as file:
            try:
                save_data = json.load(file)
            except json.JSONDecodeError:
                save_data = []
    else:
        save_data = []
    if not isinstance(save_data, list):
        save_data = [save_data]

    save_data.append(new_data)

    with open("results.json", "w") as file:
        json.dump(save_data, file, indent=4)


#takes the infomation and sends it to calculate
def info(data):
    calculate(data)
#starts the calculations.py file 
def calculate(data):
    print("Minion data")
    data = Calc(data)
    results = data.calculate()
    print(results)
    total_profit = results.get("total_profit",0)
    diamond_profit = results.get("diamondspreading", 0)
    minion_used = results.get("minion","")

    app.update_results(total_profit,diamond_profit)
    for_save = [minion_used,total_profit]
    save_results(for_save)

#runs the gui file
if __name__ == "__main__":
    app = minoncalc_GUI(callback=info)
    app.mainloop()
