import pandas as pd
from utils.execute_current import execute_current

raw_file = "./raw/utlity_companies.csv"
chart_file = "./charts/electric_utlity_companies.json"


def toChart():
    s = pd.read_csv(raw_file)
    filtered = s
    capacity = []
    generation = []
    renewable_generation = []

    for index in filtered.index:
        capacity.append({
            "x": filtered["Company"][index],
            "y": filtered["Capacity"][index]
        })

        generation.append({
            "x": filtered["Company"][index],
            "y": filtered["Generation"][index]
        })

        renewable_generation.append({
            "x": filtered["Company"][index],
            "y": filtered["Generation"][index]
        })

    # sort
    capacity.sort(key=lambda point: point["y"], reverse=True)

    return {
        "type": "HorizontalCategorical",
        "options": {
            "units": "MW",
            "yType": "category"
        },
        "series": [{
            "color": "navy",
            "type": "bar",
            "opacity": 1,
            "name": "Total Capacity",
            "data": capacity
        }]
    }


execute_current()
