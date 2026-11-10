import json
from classes import Cab

def load_cabs():
    try:
        with open("cabs.json", "r") as file:
            data = json.load(file)

        cabs=[]
        for cab in data:
            new_cab = Cab(
                cab["driver"],
                cab["seats"],
                cab["destination"],
                cab["time_slot"]
            )
            cabs.append(new_cab)
        return cabs

    except:
        print("Could not load cabs.")
        return []