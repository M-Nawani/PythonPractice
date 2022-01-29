# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DeepPink")
# timmy.forward(100)
#
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)
table.align["Pokemon Name"] = "l"
print(table)

