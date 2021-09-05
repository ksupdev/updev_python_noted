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
column = 0
row = 0

horizonal = int(position[0])
vertical = int(position[1])
print(f"{column} | {row}")
map[vertical-1][horizonal-1] = "x"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
```

## Project: Rock Paper Scissors

```python

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

actions = [rock,paper,scissors] #[0,1,2]
your_action = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n ")
your_action_int = int(your_action)

# 0 : Rock
# 1 : Paper
# 2 : Scissors

com_action_random = random.randint(0,2)
com_action_string = actions[com_action_random]
you_action_string = actions[your_action_int]

print(you_action_string)
print(f"Computer chose: {com_action_random}")
print(com_action_string)

if your_action_int == 0 and com_action_random == 2:
  print(" You win")
elif your_action_int == 0 and com_action_random == 0:
  print(" Again")
elif your_action_int == 0 and com_action_random == 1:
  print(" You lose")
elif your_action_int == 1 and com_action_random == 0:
  print(" You win")
elif your_action_int == 1 and com_action_random == 1:
  print(" Again")
elif your_action_int == 1 and com_action_random == 2:
  print(" You lose")
elif your_action_int == 2 and com_action_random == 1:
  print(" You win")
elif your_action_int == 2 and com_action_random == 2:
  print(" Again")
elif your_action_int == 2 and com_action_random == 0:
  print(" You lose")

```
