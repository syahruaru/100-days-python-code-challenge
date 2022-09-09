import random
from replit import clear
from art import logo

def deal_card():
  '''Return a random card '''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
#print(deal_card())

def calculate_score(cards):
  
  
  if sum(cards) == 21 and len(cards)== 2 :
    return 0
 
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score,computer_score):
  
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  
  
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  
  print(logo)

  
  user_cards = []
  computer_cards = []
  blackjack = 'y'
  is_game_over = False

  for i in range (2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
# print(f"user cards = {user_cards}")
# print(f"computer cards = {computer_cards[0]}")
  
  while blackjack == 'y':
  #while not is_game_over:
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      blackjack = 'n'
      #is_game_over = True
    else:
      
      draw = input("you wanna draw another card?\n'y' or 'n'")
      if draw == 'y':
        user_cards.append(deal_card())
      else:
        blackjack = 'n'
        #is_game_over = True
        
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

    
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play blackjack?\ntype 'y' for yes or type 'n' for no.\n").lower() == 'y':
  
  clear()
  play_game()

