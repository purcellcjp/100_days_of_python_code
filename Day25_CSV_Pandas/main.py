import csv
import pandas as pd

csvpath = 'weather_data.csv'

# with open(csvpath) as file:
#     data = file.readlines()
# print(data)

# with open(csvpath) as data_file:
#     data = csv.reader(data_file)
#     temps=[]
#     for row in data:
#         if row[1] != 'temp':
#             temp=int(row[1])
#             temps.append(temp)
# print(temps)

#Pandas
df = pd.read_csv(csvpath)
# print(df.head())
# print(df['temp'])

# convert to dictionary
# data_dict = df.to_dict()
# print(data_dict)

# convert datafram column to list
# temp_list = df['temp'].to_list()
# print(temp_list)

# print('-'*20)
# average = df.temp.mean()
# print('Average Temp: ', average)
# print(sum(temp_list)/ len(temp_list))
# print('Max Temp', df.temp.max())

# filtering
# print(df[df.day == 'Monday'])

# print(df[df.temp == df.temp.max()])

# convert temps to farhenheit
# df['f_temp'] = (df.temp * 9/5) + 32
# # print(df.f)
# print(df)

data_dict = {
    'students':['amy','jj','bob'],
    'scores':[90,56,65]
}
data_df = pd.DataFrame(data_dict)
print(data_df)
data_df.to_csv('new_data.csv', index=False)