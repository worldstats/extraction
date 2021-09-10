from processing.utils.NpEncoder import NpEncoder
import numpy as np
import pandas as pd
import json
from ...utils.NpEncoder import NpEncoder

s = pd.read_csv('./data/utlity_companies.csv')


filtered = s
capacity = []
generation = []
renewable_generation = []


for index in filtered.index:
  capacity.append({"x": filtered["Company"][index], "y": filtered["Capacity"][index] })
  generation.append({"x": filtered["Company"][index], "y": filtered["Generation"][index] })
  renewable_generation.append({"x": filtered["Company"][index], "y": filtered["Generation"][index] })

def comparator(point):
  return point["y"]


#sort
capacity.sort(key=lambda point : point["y"],reverse=True)


with open('../charts/electricity/produced-by-companies-in-india.json', 'w') as outfile:

  json.dump({
    "type":"HorizontalCategorical",
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
  },outfile,cls=NpEncoder);
