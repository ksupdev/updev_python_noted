## Who wil pay the bill?

```python
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
randome_who_pay = random.randint(0,len(names)-1)
print(f"{names[randome_who_pay]} is going to buy the meal today!")
```

## Day 4.3 Treasure Map Exercise

```python
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# [column][row]
column = 0
row = 0

column = int(position[0])
row = int(position[1])
print(f"{column} | {row}")
map[row-1][column-1] = "x"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
```
