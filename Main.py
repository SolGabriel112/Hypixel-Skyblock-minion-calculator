from minioncalc_GUI import minoncalc_GUI
from Calculations import Calc
import requests
import json
Main_Data = "test"
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
    app.update_results(total_profit,diamond_profit)
#runs the gui file
if __name__ == "__main__":
    app = minoncalc_GUI(callback=info)
    app.mainloop()
