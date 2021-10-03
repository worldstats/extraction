import numpy as np
import pandas as pd
import json
from utils.execute_current import execute_current

raw_file = "./raw/electricity-generation.csv"
chart_file = "./charts/electric_india-electricity-consumption-over-time.json"

def toChart():

    s = pd.read_csv(raw_file)
    filtered = s[s["Entity"] == "India"]
    points = []
    for index in filtered.index:
        points.append({
            "x": filtered["Year"][index],
            "y": int(filtered["Electricity Generation (TWh)"][index])
        })

    return {
        "type": "TimeSeries",
        "series": [{
            "color": "pink",
            "type": "bar",
            "opacity": 0.5,
            "name": "Fossil Fuels",
            "data": points
        }]
    }

execute_current()
