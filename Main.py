from minioncalc_GUI import minoncalc_GUI
import requests
import json

def info(data):
    print("Received data:", data)

if __name__ == "__main__":
    app = minoncalc_GUI(callback=info)
    app.mainloop()

print(app.fuel)
print(app.minion)