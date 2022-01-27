import numpy as np
import pandas as pd
import os
import json
from utils.execute_current import execute_current
import utils.time_series as ts

raw_file = "./raw/electricity-generation.csv"
raw_file2 = "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Number%20of%20people%20with%20and%20without%20electricity%20access%20(OWID%20based%20on%20WB%2C%202019)/Number%20of%20people%20with%20and%20without%20electricity%20access%20(OWID%20based%20on%20WB%2C%202019).csv"
chart_file = "./charts/" + os.path.basename(__file__).replace('.py', '.json')

def toChart():
    cres = pd.read_csv(raw_file2)

    cres_india = cres[cres["Entity"] == "India"]
    cres_india = cres_india.rename(columns={"Year": "time"})

    return ts.create_time_series_chart(cres_india, {
        "type": "TimeSeries",
        "options": {
            "stackBy": 'y'
        },
        "series": [
            {
               "data": 'Number of people with access to electricity',
               "name": "Number of people with access to electricity",
               "type": "area", "color": "orange"
             },
            {
              "data": 'Number of people without access to electricity',
              "name": "Number of people without access to electricity",
              "type": "area",
              "color": "grey"
            },
        ]
    }
   )

execute_current()
