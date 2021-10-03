import numpy as np
import pandas as pd
import json
from utils.execute_current import execute_current

raw_file = "./raw/electricity-generation.csv"
raw_file2 = "./raw/energy-consumption-by-source-and-region.csv"
chart_file = "./charts/electric_india-electricity-consumption-over-time.json"


def toChart():
    totals = pd.read_csv(raw_file)
    cres = pd.read_csv(raw_file2)
    fossil_fuels = []
    green_energy = []

    cres_india = cres[cres["Entity"] == "India"]

    for index in cres_india.index:
        fossil_fuels.append({
            "x": cres_india["Year"][index],
            "y": int(cres_india["Coal Consumption - EJ"][index])
                 + int(cres_india["Oil Consumption - EJ"][index])
                 + int(cres_india["Gas Consumption - EJ"][index])
                 + int(cres_india["Nuclear Consumption - EJ"][index])
        })

    for index in cres[cres["Entity"] == "India"].index:
        green_energy.append({
            "x": cres_india["Year"][index],
            "y": int(cres_india["Hydro Consumption - EJ"][index])
                 + int(cres_india["Wind Consumption - EJ"][index])
                 + int(cres_india["Geo Biomass Other - EJ"][index])
                 + int(cres_india["Biofuels (TWh)"][index])
                 + int(cres_india["Solar Consumption - EJ"][index])
        })

    return {
        "type": "TimeSeries",
        "series": [{
            "color": "brown",
            "type": "bar",
            "opacity": 0.5,
            "name": "Fossil Fuels",
            "data": fossil_fuels
        },
            {
                "color": "green",
                "type": "bar",
                "opacity": 1,
                "name": "Renewable Energy",
                "data": green_energy
            }
        ]
    }


execute_current()
