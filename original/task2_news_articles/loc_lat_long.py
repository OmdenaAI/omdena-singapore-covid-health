data = pd.read_csv("english_1K_sequence_label.csv")
df = pd.DataFrame(index=range(0,1020))
df['lat'] = data.ActionGeo_Lat.values
df['long'] = data.ActionGeo_Long.values
records = df.to_records(index=False)
df['loc'] = ""
result = list(records)
print(df)


for index in df.iterrows():
    results = Geocoder.reverse_geocode(df['lat'][index[0]], df['long'][index[0]])
    df.iloc[index[0], df.columns.get_loc('loc')] = results.city