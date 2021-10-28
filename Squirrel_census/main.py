import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_list = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

squirrel_file = pandas.DataFrame(squirrel_list)

squirrel_file.to_csv("new_data.csv")
