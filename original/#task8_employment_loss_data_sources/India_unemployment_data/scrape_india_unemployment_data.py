import glob
import os
import functools

import pandas as pd


sheets = [
    "monthly unemployment",
    "daily averaged unemployment",
    "weekly unemployment"
]

def format_country_data(excel_writer):
    # data downloaded and extracted from https://unemploymentinindia.cmie.com/kommon/bin/sr.php?kall=wtabnav&tab=4020

    # list of (pattern, name) tuples
    rates = [("_M_", "monthly"),
             ("_D_", "daily averaged"),
             ("_W_", "weekly")]

    # list of (suffix, name) tuples
    locations = [("Total", "total"),
                 ("Urban", "urban"),
                 ("Rural", "rural")]

    parsed_dfs = []
    for rate_pattern, rate_name in rates:
        location_dfs = []
        for location_suffix, location_name in locations:
            file_pattern = os.path.join("unemploymentrateinindia", "*" + rate_pattern + location_suffix + "*")
            matches = glob.glob(file_pattern)
            assert len(matches) == 1, f"something went wrong with {file_pattern}"
            raw_df = pd.read_csv(matches[0], skiprows=1)
            raw_df.columns = raw_df.columns.str.strip()
            raw_df.columns = [c + ": " + location_name if c_ind > 2 else c for c_ind, c in enumerate(raw_df.columns)]
            raw_df["Date"] = pd.to_datetime(raw_df["Date"], dayfirst=True)
            location_dfs.append(raw_df)
        merged_df = functools.reduce(lambda x, y: pd.merge(x, y,
                                                           on=["Region", "Date", "Frequency"],
                                                           how="outer"),
                                     location_dfs)
        merged_df = merged_df.set_index("Region").sort_values(["Region", "Date"])
        merged_df.to_excel(excel_writer,
                           sheet_name=f"{rate_name} unemployment")
        merged_df.loc[merged_df.index != "India", "Gov level"] = "State"
        merged_df.loc[merged_df.index == "India", "Gov level"] = "Country"
        parsed_dfs.append(merged_df)

    return parsed_dfs


if __name__ == '__main__':
    with pd.ExcelWriter("india_unemployment.xlsx",
                        engine='xlsxwriter',
                        datetime_format='mm-dd-yyyy',
                        date_format='mm-dd-yyyy') as writer:
        format_country_data(writer)

    # example usage
    pd.read_excel("india_unemployment.xlsx",
                  sheet_name="monthly unemployment")