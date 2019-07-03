#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import codecs
import glob


# In[69]:


df_list = []
for file in glob.glob("data/*"):
    with codecs.open(file, "r", 
                         "Shift-JIS", "ignore") as f:
        df = pd.read_csv(
                f, delimiter=",", skiprows=5, index_col=0, 
                usecols=[0,1,2,3,6,9,12,15,19,23,27,29,35,41])
    df_new = df.reset_index()
    df_new = df_new.rename(columns={"Unnamed: 1": "month",
                                "Unnamed: 2": "day",
                                "Unnamed: 3": "avg_temp",
                                "Unnamed: 6": "max_temp",
                                "Unnamed: 9": "min_temp",
                                "Unnamed: 12": "avg_wind",
                                "Unnamed: 15": "precip",
                                "Unnamed: 19": "day_light",
                                "Unnamed: 23": "snowfall",
                                "Unnamed: 27": "max_wind",
                                "Unnamed: 29": "wind_direc",
                                "Unnamed: 35": "weather",
                                "Unnamed: 41": "avg_cloud",
                                "index": "year",})
    df_list.append(df_new)

df_all = pd.concat(df_list).sort_values(['year', 'month', 'day']).reset_index(drop=True)
# df_all.info()
# df_all[df_all.wind_direc == '']
df_all.loc[df_all['wind_direc'] == '北', 'wind_direc'] = 'N'
df_all.loc[df_all['wind_direc'] == '北)', 'wind_direc'] = 'N'
df_all.loc[df_all['wind_direc'] == '北]', 'wind_direc'] = 'N'
df_all.loc[df_all['wind_direc'] == '南', 'wind_direc'] = 'S'
df_all.loc[df_all['wind_direc'] == '南)', 'wind_direc'] = 'S'
df_all.loc[df_all['wind_direc'] == '南]', 'wind_direc'] = 'S'
df_all.loc[df_all['wind_direc'] == '東', 'wind_direc'] = 'E'
df_all.loc[df_all['wind_direc'] == '西', 'wind_direc'] = 'W'
df_all.loc[df_all['wind_direc'] == '北東', 'wind_direc'] = 'NE'
df_all.loc[df_all['wind_direc'] == '北東)', 'wind_direc'] = 'NE'
df_all.loc[df_all['wind_direc'] == '北北東', 'wind_direc'] = 'NNE'
df_all.loc[df_all['wind_direc'] == '北北東)', 'wind_direc'] = 'NNE'
df_all.loc[df_all['wind_direc'] == '東北東', 'wind_direc'] = 'ENE'
df_all.loc[df_all['wind_direc'] == '北西', 'wind_direc'] = 'NW'
df_all.loc[df_all['wind_direc'] == '北西)', 'wind_direc'] = 'NW'
df_all.loc[df_all['wind_direc'] == '北北西', 'wind_direc'] = 'NNW'
df_all.loc[df_all['wind_direc'] == '北北西)', 'wind_direc'] = 'NNW'
df_all.loc[df_all['wind_direc'] == '西北西', 'wind_direc'] = 'WNW'
df_all.loc[df_all['wind_direc'] == '南東', 'wind_direc'] = 'SE'
df_all.loc[df_all['wind_direc'] == '南東)', 'wind_direc'] = 'SE'
df_all.loc[df_all['wind_direc'] == '南南東', 'wind_direc'] = 'SSE'
df_all.loc[df_all['wind_direc'] == '南南東)', 'wind_direc'] = 'SSE'
df_all.loc[df_all['wind_direc'] == '南南東]', 'wind_direc'] = 'SSE'
df_all.loc[df_all['wind_direc'] == '東南東', 'wind_direc'] = 'ESE'
df_all.loc[df_all['wind_direc'] == '南西', 'wind_direc'] = 'SW'
df_all.loc[df_all['wind_direc'] == '南西)', 'wind_direc'] = 'SW'
df_all.loc[df_all['wind_direc'] == '南南西', 'wind_direc'] = 'SSW'
df_all.loc[df_all['wind_direc'] == '南南西)', 'wind_direc'] = 'SSW'
df_all.loc[df_all['wind_direc'] == '南南西]', 'wind_direc'] = 'SSW'
df_all.loc[df_all['wind_direc'] == '西南西', 'wind_direc'] = 'WSW'
df_all.wind_direc.unique()

# df_all[df_all.wind_direc == i]

for col in df_all.columns.values:
    df_isna = df_all[df_all[col].isna()]
    if len(df_isna) != 0:
        print(col)
        print('欠損データ: {}件'.format(len(df_isna)))
        display(df_isna)


# df_all.to_csv("weather_tokyo_1987-2018.csv", index=False)

