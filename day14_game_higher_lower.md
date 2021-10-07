# Day 14 : Beginner - Higher Lower Game Project 

##UPDEV version
```python
# List message string
# Print Game logo

# You're right! Current score: 1.
# Sorry, that's worng. Final score: 1.

# Compare A : name,description, country
# Print VS Logo

# Compare B : name,description, country
#Who has more followers? Type 'A' or 'B':


import random
from replit import clear

from art import logo
from art import vs


def random_questions(param_questions):
  from game_data import data
  # Set Quesion for compare
  # Validate duplicate Question
  questions = param_questions
  while len(questions) < 2:
    ques = random.choice(data)
    if ques not in questions:
      questions.append(ques)

  return questions

# random_question()

def print_question(questions):
  is_fist_question = True
  for ques in questions:
    if is_fist_question:
      print(f"Compare A : {ques['name']} , {ques['description']}, {ques['country']}")   
      print(vs)
      is_fist_question = False
    else:
      print(f"Compare B : {ques['name']} , {ques['description']}, {ques['country']}")

# def check_answer():



def game():
  score = 0
  is_game_over = False
  
  
  # Loop play game until game is Over
  questions = []
  while not is_game_over:
    print(logo)
    print(f"You're right! Current score: {score}.")

    questions = random_questions(questions)

    print_question(questions)

    
    if len(questions) != 2:
      print(f"Program has some error.")
      is_game_over = True
      break

    score_of_ques_A = questions[0]["follower_count"]
    score_of_ques_B = questions[1]["follower_count"]

    print(f"{score_of_ques_A}")
    print(f"{score_of_ques_B}")

    correct_anw = ""
    if score_of_ques_A >= score_of_ques_B:
      correct_anw = "A"
    else:
      correct_anw = "B"

    answer = str(input("Who has more followers? Type 'A' or 'B':"))
    if answer.upper() == correct_anw:
      del questions[0]
      score += 1
    else:
      is_game_over = True
    clear()
    
  print(logo)
  print(f"Sorry, that's worng. Final score: {score}.")
  
game()

```

## UDAYME

```
from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()


# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
```
