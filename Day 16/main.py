# import turtle
# from turtle import Turtle,Screen
# timy = Turtle()
# timy.shape("turtle")
# timy.color("DarkSeaGreen")
# my_screen = Screen()
# timy.forward(-75)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name",['chespin', 'Quilladin', 'chesnaught','Fennekin'])
table.add_column('Type',['Grass','Grass','Grass', 'Fire'])

table.align = 'l'
print(table)

table2 = PrettyTable()
table2.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table2.add_rows(
[
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
table.border = False
table2.border = False
table2.header = False
table2.padding_width = 5
print(table2)