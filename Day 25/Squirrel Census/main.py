import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_dict = data.to_dict()
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Red"])

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Red"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, red_squirrels_count]
}

new_data = pandas.DataFrame(squirrel_dict)
new_data.to_csv("squirrel_count.csv")