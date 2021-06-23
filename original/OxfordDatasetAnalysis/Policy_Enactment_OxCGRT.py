#OMDENA CHALLENGE COVID-19
#File created on 18/4/20 by Arthur Wandzel

#Directions:
#Select country name of interest and input it into variable below then run cmd: "python Policy_Enactment_OxCGRT.py"
#Add OxCGRT in same directory as python script.
#You may need to download the python modules pandas, matplotlib, numpy, seaborn.
COUNTRY_NAME = "United States"

# [('Aruba', 'ABW'), ('Afghanistan', 'AFG'), ('Angola', 'AGO'), ('Albania', 'ALB'), ('Andorra', 'AND')]
# [('United Arab Emirates', 'ARE'), ('Argentina', 'ARG'), ('Australia', 'AUS'), ('Austria', 'AUT'), ('Azerbaijan', 'AZE')]
# [('Burundi', 'BDI'), ('Belgium', 'BEL'), ('Burkina Faso', 'BFA'), ('Bangladesh', 'BGD'), ('Bulgaria', 'BGR')]
# [('Bahrain', 'BHR'), ('Bosnia and Herzegovina', 'BIH'), ('Belize', 'BLZ'), ('Bermuda', 'BMU'), ('Bolivia', 'BOL')]
# [('Brazil', 'BRA'), ('Barbados', 'BRB'), ('Brunei', 'BRN'), ('Botswana', 'BWA'), ('Canada', 'CAN')]
# [('Switzerland', 'CHE'), ('Chile', 'CHL'), ('China', 'CHN'), ('Cameroon', 'CMR'), ('Democratic Republic of Congo', 'COD')]
# [('Colombia', 'COL'), ('Cape Verde', 'CPV'), ('Costa Rica', 'CRI'), ('Cuba', 'CUB'), ('Cyprus', 'CYP')]
# [('Czech Republic', 'CZE'), ('Germany', 'DEU'), ('Djibouti', 'DJI'), ('Denmark', 'DNK'), ('Dominican Republic', 'DOM')]
# [('Algeria', 'DZA'), ('Ecuador', 'ECU'), ('Egypt', 'EGY'), ('Spain', 'ESP'), ('Estonia', 'EST')]
# [('Finland', 'FIN'), ('France', 'FRA'), ('Gabon', 'GAB'), ('United Kingdom', 'GBR'), ('Ghana', 'GHA')]
# [('Gambia', 'GMB'), ('Greece', 'GRC'), ('Greenland', 'GRL'), ('Guatemala', 'GTM'), ('Guam', 'GUM')]
# [('Guyana', 'GUY'), ('Hong Kong', 'HKG'), ('Honduras', 'HND'), ('Croatia', 'HRV'), ('Hungary', 'HUN')]
# [('Indonesia', 'IDN'), ('India', 'IND'), ('Ireland', 'IRL'), ('Iran', 'IRN'), ('Iraq', 'IRQ')]
# [('Iceland', 'ISL'), ('Israel', 'ISR'), ('Italy', 'ITA'), ('Jamaica', 'JAM'), ('Jordan', 'JOR')]
# [('Japan', 'JPN'), ('Kazakhstan', 'KAZ'), ('Kenya', 'KEN'), ('Kyrgyz Republic', 'KGZ'), ('South Korea', 'KOR')]
# [('Kuwait', 'KWT'), ('Laos', 'LAO'), ('Lebanon', 'LBN'), ('Libya', 'LBY'), ('Sri Lanka', 'LKA')]
# [('Lesotho', 'LSO'), ('Luxembourg', 'LUX'), ('Macao', 'MAC'), ('Morocco', 'MAR'), ('Moldova', 'MDA')]
# [('Madagascar', 'MDG'), ('Mexico', 'MEX'), ('Mali', 'MLI'), ('Myanmar', 'MMR'), ('Mongolia', 'MNG')]
# [('Mozambique', 'MOZ'), ('Mauritania', 'MRT'), ('Mauritius', 'MUS'), ('Malawi', 'MWI'), ('Malaysia', 'MYS')]
# [('Namibia', 'NAM'), ('Niger', 'NER'), ('Nigeria', 'NGA'), ('Nicaragua', 'NIC'), ('Netherlands', 'NLD')]
# [('Norway', 'NOR'), ('New Zealand', 'NZL'), ('Oman', 'OMN'), ('Pakistan', 'PAK'), ('Panama', 'PAN')]
# [('Peru', 'PER'), ('Philippines', 'PHL'), ('Papua New Guinea', 'PNG'), ('Poland', 'POL'), ('Puerto Rico', 'PRI')]
# [('Portugal', 'PRT'), ('Paraguay', 'PRY'), ('Palestine', 'PSE'), ('Qatar', 'QAT'), ('Romania', 'ROU')]
# [('Russia', 'RUS'), ('Rwanda', 'RWA'), ('Saudi Arabia', 'SAU'), ('Sudan', 'SDN'), ('Singapore', 'SGP')]
# [('Sierra Leone', 'SLE'), ('El Salvador', 'SLV'), ('San Marino', 'SMR'), ('Serbia', 'SRB'), ('South Sudan', 'SSD')]
# [('Slovak Republic', 'SVK'), ('Slovenia', 'SVN'), ('Sweden', 'SWE'), ('Eswatini', 'SWZ'), ('Seychelles', 'SYC')]
# [('Syria', 'SYR'), ('Chad', 'TCD'), ('Thailand', 'THA'), ('Trinidad and Tobago', 'TTO'), ('Tunisia', 'TUN')]
# [('Turkey', 'TUR'), ('Tanzania', 'TZA'), ('Uganda', 'UGA'), ('Ukraine', 'UKR'), ('Uruguay', 'URY')]
# [('United States', 'USA'), ('Uzbekistan', 'UZB'), ('Venezuela', 'VEN'), ('Vietnam', 'VNM'), ('South Africa', 'ZAF')]
# [('Zambia', 'ZMB'), ('Zimbabwe', 'ZWE'), ('Taiwan', 'TWN'), ('Kosovo', 'RKS')]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import axes
import seaborn as sb

def set_labels_invisiable(ax):
    every_nth = 7
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)

if __name__ == '__main__':
    FORWARD_SHIFT_IN_TIMELINE = 0
    df = pd.read_csv("OxCGRT_18_04_20.csv")  # df = dataframe
    #print descriptive labels
    print("Columns:\n", df.columns)
    print("Number of represented Countries:\n", len(df.CountryCode.unique()))
    #print("Index:\n", df.index)
    #print("Country Codes:\n", df.CountryCode.unique())

    #test 2: cumulative cases with policy annotations
    data = list(zip(df.CountryName.unique(), df.CountryCode.unique()))
    [print(data[x:x + 5]) for x in range(0, len(data), 5)]
    series_indexes = df.index[df['CountryName'] == COUNTRY_NAME].tolist()
    confirmed_cases = df.iloc[series_indexes]['ConfirmedCases']
    date = df.iloc[series_indexes]['Date'].astype(str).str[4:6] + "/" + df.iloc[series_indexes]['Date'].astype(str).str[6:68]
    # print(confirmed_cases.to_string())
    # print(date.to_string())

    confirmed_cases = confirmed_cases.tolist()
    transform_daily_cases = []
    date = date.tolist()

    #clean data
    clean_value = 0
    clean_index = 0
    print("Before clean \n", confirmed_cases)
    for i in range(1, len(confirmed_cases)):
        if not np.isnan(confirmed_cases[i]):
            clean_value = confirmed_cases[i]
            clean_index = i
        else:
            confirmed_cases[i] = clean_value + (clean_value - confirmed_cases[clean_index-1])

    #transform confirmed cases to daily increase
    print("Before transform \n", confirmed_cases)
    transform_daily_cases.append(confirmed_cases[0])
    for i in range(1, len(confirmed_cases)):
        transform_daily_cases.append(confirmed_cases[i] - confirmed_cases[i-1])
    print("After \n", transform_daily_cases)

    #detect change in policies
    markers = {}
    index = [3, 6, 9, 12, 15, 18, 21]
    columns = df.columns.tolist()
    for i in range(1, len(series_indexes)):
        for j in index:
            policy_value = df.at[series_indexes[i], columns[j]]
            if columns[j] not in markers and policy_value > 0:
                markers[columns[j]] = i

    #make markers
    marker_on = []
    marker_labels = []
    for k,v in markers.items():
        marker_on.append(v)
        marker_labels.append("" + k)

    print(marker_on)
    fig, _ = plt.subplots()
    ax = sb.lineplot(date[FORWARD_SHIFT_IN_TIMELINE:],
                     transform_daily_cases[FORWARD_SHIFT_IN_TIMELINE:], marker="*", ms=10, markevery=marker_on)
    set_labels_invisiable(ax)

    for i in range(len(marker_labels)):
        ax.text(date[marker_on[i]], transform_daily_cases[marker_on[i]], marker_labels[i], fontsize=10, rotation=85)
    #ax.text(date[1], confirmed_cases[1], "hey", rotation=45)
    #axes.Axes.text(date[1], confirmed_cases[1], "hey", )

    ax.set_ylabel("Daily Confirmed Cases")
    ax.set_xlabel("Date")
    plt.title("Policy Enactment of " + COUNTRY_NAME)
    fig.autofmt_xdate()
    plt.show()
