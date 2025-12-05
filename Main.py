from minioncalc_GUI import minoncalc_GUI
from Calculations import Calc
import requests
import json
Main_Data = "test"
#takes the infomation and sends it to calculate
def info(data):
    global Main_Data
    Main_Data = data
    calculate(data=Main_Data)
#starts the calculations.py file 
def calculate(data):
    print("Minion data")
    data = Calc(data)
    data.calculate()
#runs the gui file
if __name__ == "__main__":
    app = minoncalc_GUI(callback=info)
    app.mainloop()
