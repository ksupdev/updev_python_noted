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
