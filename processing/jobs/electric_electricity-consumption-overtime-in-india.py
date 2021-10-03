import numpy as np
import pandas as pd
import json
from utils.execute_current import execute_current

raw_file = "./raw/electricity-generation.csv"
raw_file2 = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
chart_file = "./charts/electric_india-electricity-consumption-over-time.json"


def toChart():
    totals = pd.read_csv(raw_file)
    cres = pd.read_csv(raw_file2)
    fossil_fuels = []
    green_energy = []
    coal_energy = []
    oil_electricity = []

    cres_india = cres[cres["country"] == "India"]
    cres_india = cres_india[cres["fossil_electricity"].isnull() ^ 1]

    for index in cres_india.index:
        green_energy.append({
            "x": int(cres_india["year"][index]),
            "y": float(cres_india["renewables_electricity"][index])
        })

        fossil_fuels.append({
            "x": int(cres_india["year"][index]),
            "y": float(cres_india["fossil_electricity"][index])
        })

    return {
        "type": "TimeSeries",
        "options": {
          "stackBy": "y"
        },
        "series": [
            {
                "color": "green",
                "type": "bar",
                "opacity": 1,
                "name": "Renewable Energy",
                "data": green_energy,
                "stack": False

            },
            {
                "color": "brown",
                "type": "bar",
                "opacity": 0.5,
                "name": "Fossil Fuels",
                "data": fossil_fuels,
                "stack": False
            },
        ]
    }


execute_current()
