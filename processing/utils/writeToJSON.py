from NpEncoder import NpEncoder
import json

def writeToJSONFile(data):
  with open('../charts/electricity/produced-by-companies-in-india.json', 'w') as outfile:
    json.dump(data,outfile,cls=NpEncoder)
