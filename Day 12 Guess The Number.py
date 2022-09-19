import random
import Day_12_art as day
#print(day.logo)

number = random.randint(1,100)
print(number) 
print("This is Guessing Number Game, Welcome!")
print("I'm thinking of a number between 1 and 100.")
level = input("Select level do you want play 'easy' or 'hard'?\n")
life = 0
if level == 'hard':
  life += 5 
elif level == 'easy':
  life += 10 
else:
  print("your type wrong, bye! ")
print(f"You have {life} attempt to guess! ")
guess = 0
play_game = True

while play_game:
  guess = int(input("Guess The Number!\n"))
  if guess == number:
    print(f"Thats right the number is {number}, Congratulation")
    play_game = False
  elif life == 1:
    print("You can't attempt any more")
    print("you lose")
    play_game = False
  elif guess > number:
    print("Its to high") 
    life -= 1
    print(f"You have {life} attempt to guess!")
  elif guess < number:
    print("Its to low")
    life -= 1
    print(f"You have {life} attempt to guess!")
    

  
