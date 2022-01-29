import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"].value_counts()
print(fur_color)

data_frame = pandas.DataFrame(fur_color)
print(data_frame)

# average = data["temp"].mean()


# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)
