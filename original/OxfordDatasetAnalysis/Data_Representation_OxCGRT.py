#OMDENA CHALLENGE COVID-19
#File created on 18/4/20 by Arthur Wandzel

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import axes
import seaborn as sb

if __name__ == '__main__':
    df = pd.read_csv("OxCGRT_18_04_20.csv")  # df = dataframe
    #print descriptive labels
    print("Columns:\n", df.columns)
    print("Index:\n", df.index)
    print("Country Names:\n", df.CountryName.unique())
    print("Number of represented Countries:\n", len(df.CountryCode.unique()))

    #test 1: plot data representativeness
    country_index = df.CountryName.unique()

    #iterate over country indexes : count NaNs
    nan_count_array = np.zeros(len(country_index))
    total_count_array = np.zeros(len(country_index))
    representation_index = np.zeros(len(country_index))
    for i, ccode in enumerate(country_index):
        series_indexes = df.index[df['CountryName'] == ccode].tolist()
        nan_count_array[i] = df.iloc[series_indexes].isna().sum().sum()
        total_count_array[i] = len(series_indexes) * len(df.columns)
        representation_index[i] = (total_count_array[i] - nan_count_array[i]) / total_count_array[i]
        #print(ccode, " : ", df.iloc[series_indexes].isna().sum().sum())

    #pandas dataframe: {column=country_code, row=NaN_count
    df_temp = pd.DataFrame({"cc" : country_index,
                           "nan" : nan_count_array,
                           "total" : total_count_array,
                           "rep_idx" : representation_index})
    df_temp = df_temp.sort_values(by="rep_idx", ascending=False)
    print("Best", df_temp.head(10))
    print("Worse", df_temp.tail(10))

    x = df_temp["rep_idx"]
    ax = sb.distplot(x, bins=len(x), kde=True)
    ax.set_ylabel("Number of Countries")
    ax.set_xlabel("Percent of Complete Data Entrees")
    plt.title("Representation in OxCGRT")
    #ax.set_xticks(np.arange(len(x)))
    #ax.set_xticklabels(labels, rotation=45, rotation_mode="anchor", ha="right")
    plt.show()