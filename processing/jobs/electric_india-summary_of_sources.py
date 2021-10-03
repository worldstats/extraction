import numpy as np
import pandas as pd
import json
from utils.execute_current import execute_current
import xlrd

raw_file = "./raw/capacity1-2021-08.xls"
chart_file = "./charts/electric_india-summary-capacity-sources.json"


def toChart():
    workbook = xlrd.open_workbook_xls(raw_file)

    sheet = workbook.sheet_by_index(0)

    smallhydro = sheet.cell_value(colx=1, rowx=39)
    wind = sheet.cell_value(colx=2, rowx=39)
    solar = sheet.cell_value(colx=10, rowx=39)

    series = []

    for row in [["Small Hydro", smallhydro], ["Wind", wind], ["Solar", solar]]:
        series.append({
            "color": "green",
            "type": "bar",
            "opacity": 1,
            "name": row[0],
            "data": row[1]
        })

    return {
        "type": "NumberStats",
        "options": {
            "units": "MW",
            "yType": "category"
        },
        "series": series
    }


execute_current()
