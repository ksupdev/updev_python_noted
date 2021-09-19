# The Blackjack Capstone

## Updev version
```python
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

def is_Blackjack(card_on_hand):
  if len(card_on_hand) == 2 and 11 in card_on_hand and 10 in card_on_hand:
    return True
  return False

def sum_score(card_on_hand):
  all_score = 0
  for val in card_on_hand:
    all_score += val
  
  if all_score > 21 and 11 in card_on_hand:
    all_score -= 10
  return all_score

def is_Over21(card_on_hand):
  all_score = sum_score(card_on_hand)
  if all_score > 21:
    return True
  else:
    return False

import random

def random_cards(cards):
  return random.choice(cards)

def check_base_rule(cards):
  if is_Blackjack(user_card):
    print("BlackJack !")
    return "win"
  else:
    if is_Over21(user_card):
      return "lose"
    else:
      print(f" Your current {user_card} score {sum_score(user_card)}")
      return "continue"

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
computer_card = []

# Gen first card
user_card.append(random_cards(cards))
# print(f"user_card {user_card}")
computer_card.append(random_cards(cards))
# print(f"computer_card {computer_card}")

# Gen second card
user_card.append(random_cards(cards))
print(f"user_card {user_card}")
computer_card.append(random_cards(cards))
print(f"computer_card {computer_card[0]}")

# Check is BlackJack

get_more_card = "y"
re_cal = True
end_game = False

while re_cal:
  result_cond = check_base_rule(user_card)

  if result_cond == "win":
    print("User is Win")
    re_cal = False
    end_game = True
  elif result_cond == "lose":
    print(f"User is Lose with {sum_score(user_card)}")
    re_cal = False
    end_game = True
  else:
    get_more_card = str(input("Do you want to get another card? , please fill y:"))
    if get_more_card == "y":
      user_card.append(random_cards(cards))
      # print(f"user_card {user_card} with {sum_score(user_card)}")
    else:
      re_cal = False

if end_game == False:
  user_score = sum_score(user_card)
  com_final_score = 0
  while end_game == False:
    com_result_cond = check_base_rule(computer_card)
    if com_result_cond == "win":
      print("Computer is Win")
      end_game = True
    elif com_result_cond == "lose":
      print(f"Computer is Lose with {sum_score(computer_card)}")
      end_game = True
    else:
      if sum_score(computer_card) <= 17:
        computer_card.append(random_cards(cards))
        com_final_score = sum_score(computer_card)
        print(f"computer_card {com_final_score}")
      else:
        end_game = True
        com_final_score = sum_score(computer_card)
        print(f"computer_card {com_final_score}")

  if com_final_score > user_score:
    print("Computer is Win")
  elif com_final_score < user_score:
    print("User is Win")
  else:
    print("Draw")
```

## Udemy version

```python

```
