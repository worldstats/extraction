import pandas as pd
from utils.execute_current import execute_current

raw_file = "./raw/EQUITY_L.csv"
chart_file = "./charts/equity_companies.json"

def toChart():
    s = pd.read_csv(raw_file)
  
    return {
      "type":"Table",
        "options": {
        "units": "MW",
        "yType": "category"
      },
      "series": [{
      "color": "navy",
      "type": "bar",
      "opacity": 1,
      "name": "Name",
      "data": []
    }]
  }

execute_current()
