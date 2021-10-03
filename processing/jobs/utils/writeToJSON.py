from .NpEncoder import NpEncoder
import json

def writeToJSONChartFile(data,chart_file):
  with open(chart_file, 'w') as outfile:
    print('writing to file',chart_file)
    json.dump(data,outfile,cls=NpEncoder)
