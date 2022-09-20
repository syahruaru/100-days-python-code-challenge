import random
import art
from game_data import data

score = 0
comparison = True
keys = ['name', 'follower_count', 'description','country']

option_1 = data[random.randint(0,49)]
option_2 = data[random.randint(0,49)]
info_1 = []
info_2 = []
for key in keys:
  info_1.append(option_1.get(key))
  info_2.append(option_2.get(key))

while comparison == True: 
  info_1 = info_2
  option_2 = data[random.randint(0,49)]
  info_2 = []
  for key in keys:
    info_2.append(option_2.get(key))
  info_1.append(info_2)

  print(f"Compare Follower of 'A' {info_1[0]} a {info_1[2]} from {info_1[3]} and\n'B' {info_2[0]} a {info_2[2]} from {info_2[3]}")
  answer = input("Which one has more follower 'A' or 'B'?").upper()

  if answer == 'A' or answer == 'B':
    if answer == 'A':
      if info_1[1] > info_2[1]:
        score += 1
        print(f"You Right,Your Score Now is {score}")
      elif info_1[1] < info_2[1]:
        comparison = False
        print("You Wrong, The answer is B ")
        print(f"Your final score is {score}")
    elif answer == 'B':
      if info_2[1] > info_1[1]:
        score += 1
        print(f"You Right,Your Score Now is {score}")
      elif info_2[1] < info_1[1]:
        comparison = False
        print("You Wrong, The answer is A")
        print(f"Your final score is {score}")    
  else :
    comparison = False
    print("Your Typo, bye!")