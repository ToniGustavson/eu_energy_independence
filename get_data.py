import pandas as pd
import os
from PIL import Image

LHV_LNG = 0.006291  # kWh/m3 = MWh/10^3m3


def get_optiRes(pl_reduction, lng_capacity, reduced_demand, soc_slack):
    fileName = f"results_aGasFlowScen{pl_reduction}_{int(lng_capacity*10)}_{reduced_demand}_{soc_slack}.xlsx"
    fileDir = f"Input/Optimization/{fileName}"
    df = pd.read_excel(fileDir, index_col=0)
    df.fillna(0, inplace=True)
    df.time = pd.to_datetime(df.time)
    return df


def get_fzjColor():
    FZJcolor = pd.read_csv("Input/FZJcolor.csv")

    def rgb_to_hex(reg_vals):
        def clamp(x):
            return int(max(0, min(x * 255, 255)))

        return "#{0:02x}{1:02x}{2:02x}".format(
            clamp(reg_vals[0]), clamp(reg_vals[1]), clamp(reg_vals[2])
        )

    col_names = FZJcolor.columns
    hex_vals = [rgb_to_hex(FZJcolor.loc[:, col]) for col in col_names]

    FZJcolor_dict = dict(zip(col_names, hex_vals))
    return FZJcolor_dict


def get_countryColor(country, FZJcolor):
    color_dict = {
        "DE": "blue2",
        "PL": "green",
        "RO": "orange",
        "LT": "yellow",
        "GR": "grey3",
        "EE": "lblue",
        "BG": "pink",
        "SK": "blue",
        "FI": "yellow",
    }
    col_name = color_dict.get(country, "black")
    color_val = FZJcolor.get(col_name)
    return color_val