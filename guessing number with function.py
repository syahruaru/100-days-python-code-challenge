import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def level ():
  level = input("Select level do you want play 'easy' or 'hard'?\n")
  if level == 'hard':
    return HARD_LEVEL_TURNS 
  elif level == 'easy':
    return EASY_LEVEL_TURNS 


def comp(guess,number,life):
  if guess > number:
    print("Too High")
    return life - 1
  elif guess < number:
    print("Too Low")
    return life - 1
 
  
  

play_game = True

def The_game ():

  number = random.randint(1,100)
  print(number) # for investigating
  print("This is Guessing Number Game, Welcome!")
  
  life = level()
  guess = 0
  
  while guess != number:
    
    print(f"You have {life} attempt to guess! ")
    guess = int(input("Guess The Number!\n"))
    life = comp(guess,number,life)
    if guess == number:
      print(f"Thats right the number is {number}, Congratulation")
      return
    elif life == 0:
      print("You can't attempt any more")
      print("you lose")
      return

    
The_game()
  
