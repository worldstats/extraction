import numpy as np
import pandas as pd
import os
import json
from utils.execute_current import execute_current
import utils.time_series as ts

raw_file2 = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
chart_file = "./charts/" + os.path.basename(__file__).replace('.py', '.json')


def toChart():
    cres = pd.read_csv(raw_file2)

    cres_india = cres[cres["country"] == "India"]
    cres_india = cres_india.rename(columns={"year": "time"})

    cres_india = cres_india[cres["fossil_electricity"].isnull() ^ 1].fillna(0)
    
    return ts.create_time_series_chart(cres_india, {
        "type": "TimeSeries",
        "options": {
            "stackBy": 'y'
        },
        "series": [
            {"data": 'renewables_electricity', "name": "From renewable sources", "type": "bar", "color": "lightgreen"},
            {"data": 'fossil_electricity', "name": "From fossil fuel sources", "type": "bar","color": "grey"},
        ]
     }
    )

execute_current()
