import numpy as np
import pandas as pd
import json
from utils.execute_current import execute_current

raw_file = "./raw/utlity_companies.csv"
chart_file = "./charts/electric_renewable-electricity-consumption.json"


def toChart():
    s = pd.read_csv(raw_file)
    filtered = s
    capacity = []
    generation = []
    renewable_generation = []
    commited_capacity = []

    filtered = filtered.sort_values(by='CleanGeneration',ignore_index=True,ascending=False)
    print(filtered)



    for index in filtered.index:
        capacity.append({"x": filtered["Company"][index], "y": filtered["Capacity"][index]})
        generation.append({"x": filtered["Company"][index], "y": filtered["Generation"][index]})
        renewable_generation.append({"x": filtered["Company"][index], "y": filtered["CleanGeneration"][index]})
        commited_capacity.append({"x": filtered["Company"][index], "y": filtered["commited_capacity"][index]})

    return {
        "type": "HorizontalCategorical",
        "options": {
            "units": "MW",
            "yType": "category",
            "scales": {
                "y": {
                    "stacked": True
                },
                "x": {
                    "stacked": True
                }
            }
        },
        "series": [{
            "color": "green",
            "type": "bar",
            "opacity": 1,
            "name": "Renewable Capacity",
            "data": renewable_generation
        },
            {
                "color": "lightgreen",
                "type": "bar",
                "opacity": 1,
                "name": "Renewable Commited Capacity",
                "data": commited_capacity
            }]
    }


execute_current()
