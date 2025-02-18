import pandas as pd


df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(df.head())

# print(df)
# print(df.columns)

squirrel_color_count = df['Primary Fur Color'].value_counts()
squirrel_color_count.to_csv('my_squirrel_count.csv')
