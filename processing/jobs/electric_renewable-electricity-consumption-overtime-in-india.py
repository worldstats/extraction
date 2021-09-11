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
  
  for index in filtered.index:
    capacity.append({"x": filtered["Company"][index], "y": filtered["Capacity"][index] })
    generation.append({"x": filtered["Company"][index], "y": filtered["Generation"][index] })
    renewable_generation.append({"x": filtered["Company"][index], "y": filtered["CleanGeneration"][index] })

  #sort
  renewable_generation.sort(key=lambda point : point["y"],reverse=True)

  return {
      "type":"HorizontalCategorical",
        "options": {
        "units": "MW",
        "yType": "category"
        },
      "series": [{
        "color": "green",
        "type": "bar",
        "opacity": 1,
        "name": "Renewable Capacity",
        "data": renewable_generation
      }]
    }

execute_current()
