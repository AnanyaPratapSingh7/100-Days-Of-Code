# with open("weather_data.csv") as file:
#     data = file.readlines()

# print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []

#     for row in data:
#         if row[1]=='temp':
#             continue
#         temperatures.append(int(row[1]))

#     print(temperatures)

import pandas as pd # type: ignore

data = pd.read_csv("weather_data.csv")

# temperatures = data["temp"].to_list()

# avg_temp = sum(temperatures)/len(temperatures)

# print(round(avg_temp, 2))

# avg_temp = data.temp.mean()

# print(avg_temp)

# max_value = data.temp.max()

# print(max_value)

# Get data in row

# print(data[data.day == "Thursday"])



#Challenge : Pull out the row of data when temperature was maximum

# max_temp = data.temp.max()
# row_with_max = data[data.temp == max_temp]

# print(row_with_max)

#Get Monday's temperature in Farenheit

monday = data[data.day == "Monday"]
temp_on_mon = monday.temp
temp_on_monday = temp_on_mon.to_list()
temp_on_monday = (9/5)*temp_on_monday[0] + 32

print(temp_on_monday)