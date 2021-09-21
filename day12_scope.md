# Scope & Number Guessing Game

**keyconcept** : scope ใน python จะมีความต่างจากภาษาอื่นๆ จาก code

```python
################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```

สิ่งที่เราคิดกันทั่วๆไป ผลลัพท์ที่ได้มันน่าาจะแสดง 2 ทั้งคู่ แต่เหมือนในส่วนของ python จะมีการ scope การทำงานภายใน *function หรือก็คือจะไม่สามารถ assign value ไปที่ตัวแปลที่อยู่นอก function ได้* 

```powershell
enemies inside function : 2
enemies Outside function : 1

```

และถ้าเราพยายามจะแก้ไข หรือก็คือการอัพเดต value โดยการ ref ไปที่ global variable เช่น ``enemies += 2`` program ก็เจอ error ทันที

```powershell
UnboundLocalError: local variable 'enemies' referenced before assignment
```

จากเงื่อนไขต่างๆ เราอาจจะสามารถมองว่า ``enemies`` นั้นเป็น Constants ซึ่งตามโดยปกติ เราจะใช้เป็นตัวใหญ่ทั้งหมดแทน ``ENEMIES`` 

## the Number Guessing Game
### updev version
```python
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level_of_game = input("Choose a difficulty. Type 'easy' or 'hard':")

count_guess = 0

if level_of_game == "easy":
  count_guess = 10
else:
  count_guess = 5

print(f"You have {count_guess} attempts remaining to guess the number.")
import random
temp_input = 0
you_win = False


def guess(count_guess, number_guessing):
  while count_guess != 0:
    guess_number = int(input("Make a guess:"))
    if guess_number > number_guessing:
      print("To high.")
    elif guess_number < number_guessing:
      print("To low.")
    else:
      return True
    count_guess -= 1
    print("Guess again.")
    print(f"You have {count_guess} attemots remaining to quess the number.")
  return False

number_guessing = random.randint(1, 100)
if guess(count_guess,number_guessing):
  print(f"You win {number_guessing}")
else:
  print(f"You lose ,{number_guessing}")

```

## UDEMY version

```python
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Fucntion to check user's guess against acutal anwser
def check_answer(guess, anwser,turns):
  """Checks answer against guess. Returns thenumber of turns remaining."""
  if guess > anwser:
    print("Too high.")
    return turns - 1
  elif guess < anwser:
    print("Too low. ")
    return turns - 1
  else:
    print(f"You got it! The anwser was {anwser}")

#Male function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard' :")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS



def game():
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()

  guess = 0

  #Repeat the guessing functionlity if they get it wrong.
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    #Let the user guess a number
    guess = int(input("Make a guess:"))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return

  #Track the number of turns and reduce by 1 if they get it wrong.

game()

```

