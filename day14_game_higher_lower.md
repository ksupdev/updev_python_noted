# Day 14 : Beginner - Higher Lower Game Project 

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

from art import logo
from art import vs


def random_questions():
  from game_data import data
  questions = []
  # Set Quesion for compare
  # Validate duplicate Question
  
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


def game():

  compare_list = []
  score = 0
  is_game_over = False
  
  print(logo)
  # Loop play game until game is Over
  while not is_game_over:
    print(f"You're right! Current score: {score}.")

    questions = random_questions()

    print_question(questions)


    
    # Remove first question when Answer
    
    # print(compare_list)
    is_game_over = True



game()

# Load Question

# Check Question

```
