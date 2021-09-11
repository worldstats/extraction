import inspect
from .writeToJSON import writeToJSONChartFile

def execute_current():
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    if mod.__name__ == "__main__":
      json = mod.toChart()
      writeToJSONChartFile(json,mod.chart_file)
