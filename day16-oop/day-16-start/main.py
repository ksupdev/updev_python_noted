# # import another_module
# # print(another_module.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# # timmy.color('red', 'green')
# timmy.color("coral")
# timmy.forward(100)

# # print(timmy) # => <turtle.Turtle object at 0x0000024AC5E1B0D0>

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"


print(table)

# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide",1295, 1158259, 600.5])
# x.add_row(["Brisbane",5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])

# print(x)