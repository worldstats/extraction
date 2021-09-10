import numpy as np
import pandas as pd
import json

s = pd.read_csv('./data/utlity_companies.csv')


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


filtered = s
capacity = []
generation = []
renewable_generation = []


for index in filtered.index:
  capacity.append({"x": filtered["Company"][index], "y": filtered["Capacity"][index] })
  generation.append({"x": filtered["Company"][index], "y": filtered["Generation"][index] })
  renewable_generation.append({"x": filtered["Company"][index], "y": filtered["CleanGeneration"][index] })

def comparator(point):
  return point["y"]


#sort
renewable_generation.sort(key=lambda point : point["y"],reverse=True)


with open('../charts/electricity/renewables-produced-by-companies-in-india.json', 'w') as outfile:

  json.dump({
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
  },outfile,cls=NpEncoder);

