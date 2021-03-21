# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()
print(data_dict)

data_json = data.to_json()
print(data_json)

data_list = data["temp"].to_list()
print(data_list)
avg_temp = sum(data_list)/len(data_list)
print(avg_temp)
print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(int(monday.temp)*9/5+32)

# Create a dataframe from scratch
data_dict2 = {
    "students": ["Jake", "Amy", "Rosa"],
    "scores": [58, 99, 75]
}
new_data = pandas.DataFrame(data_dict2)
print(new_data)
new_data.to_csv("new_data.csv")