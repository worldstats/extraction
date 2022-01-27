import numpy as np


def create_time_series_chart(dataFrame,chartConfig):
    return {
        **chartConfig,
        "series": list(map(lambda x: map_series_config_to_data(dataFrame, x),chartConfig["series"]))
    }

def map_series_config_to_data(dataFrame, config):
    series = chart_timeSeries_from_data_frame(dataFrame, config["data"])
    return {**config, "data": series }


def diff_two(x):
    diff = (x.iloc[-1] - x.iloc[0])

    return np.fix(diff)


def chart_timeSeries_from_data_frame(dataFrame, seriesName,transformSeries=lambda x: x):
    series = transformSeries(dataFrame[seriesName])

    return dataFrame[seriesName].index \
        .map(lambda x: ({
        "x": dataFrame["time"][x],
        "y": series[x]})) \
        .values


def rolling_diff(series):
    return series.rolling(window=2) \
        .apply(diff_two) \
        .fillna(0)
