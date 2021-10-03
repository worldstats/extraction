import numpy as np
import pandas as pd
import json
from utils.execute_current import execute_current
import xlrd

raw_file = "./raw/capacity1-2021-08.xls"
chart_file = "./charts/summary.json"


def toChart():

    workbook = xlrd.open_workbook_xls(raw_file)

    sheet = workbook.sheet_by_index(0)
    smallhydro = sheet.cell_value(colx=1, rowx=39)
    windpower = sheet.cell_value(colx=2, rowx=39)
    solarpower = sheet.cell_value(colx=10, rowx=39)

    print(a1)

    return {
        "type": "bar",
        "series": [{
            "color": "pink",
            "type": "bar",
            "opacity": 0.5,
            "name": "Fossil Fuels",
            "data": []
        }]
    }


execute_current()
