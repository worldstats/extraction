from .NpEncoder import NpEncoder
import json

def writeToJSONChartFile(data,chart_file):
  with open(chart_file, 'w') as outfile:
    json.dump(data,outfile,cls=NpEncoder)
