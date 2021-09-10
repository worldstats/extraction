import numpy as np
import pandas as pd
import json

s = pd.read_csv('./data/electricity-generation.csv')


print(s[s["Entity"] == "India"])

filtered = s[s["Entity"] == "India"]

points = []

for index in filtered.index:
  print(filtered["Year"][index],filtered["Electricity Generation (TWh)"][index])
  points.append({"x": filtered["Year"][index], "y": int(filtered["Electricity Generation (TWh)"][index])})

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

with open('./electricity-in-india-generation.json', 'w') as outfile:
  json.dump({
   "color": "pink",
   "type": "area",
   "opacity": 0.5,
   "name": "Fossil Fuels",
   "data": points
  },outfile,cls=NpEncoder)
