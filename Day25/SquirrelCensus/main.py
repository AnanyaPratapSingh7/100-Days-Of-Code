import pandas as pd

data = pd.read_csv("SquirrelCensus/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

new_data = {
    "Fur Color" : ["Grey", "Cinnamon", "Black"],
    "Count" : [gray, cinnamon, black],
}

new_data_frame = pd.DataFrame(new_data)
new_data_frame.to_csv("./analysed_data.csv")