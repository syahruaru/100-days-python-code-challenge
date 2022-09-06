# day 1 band name generator

print("this is band name generator program")
city_name = input("what the name of the city when you grow up?\n")
pet_name = input("waht is your pets name?\n")
print(city_name +" "+ pet_name)


# day 2 bill Calculator

print("Welcome to the tip calculator!")
total_bill = input('What was the total bill? $ ')
tip = input('How much tip would you like to give? 10, 12, or 15? ') 
split = input('How many people to split the bill? ')

exactly_split = float(total_bill) / int(split)
exactly_tip = exactly_split + (exactly_split * float(int(tip) / 100))
round_fix_bill = round(exactly_tip,2)
print(f"Each person should pay: {round_fix_bill}")

# day 3 tresure island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
arah = input("ketik 'right'jika mau belok kanan, ketik 'left' jika mau belok kiri\n ")
arah_low = arah.lower()
if arah_low == "right":
  action = input("Sekarang anda di pulau  jika mau menunggu ketik 'wait', jika mau berenang ketik 'swim'\n ")  
  action_low = action.lower()
  if action_low == "wait":
    pintu = input("ada perahu datang! , kemudian berlayar ke pulau dan ada sebuah rumah dengan 3 pintu mau masuk lewat pintu biru, merah atau kuning? ketik 'blue' unutk lewat pintu biru,ketik 'red' untuk pintu merah, ketik 'yellow' untuk pintu kuning\n ")
    pintu_low = pintu.lower()
    if pintu_low == "red":
      print(" selamat kamu dapat harta karun")
    else:
      print("game over")
  else :
    print("anda kurang beruntung")
else:
  print("zonk")



# day 4 Rock, paper, scissors

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
suit = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
if suit == '0':
  print(rock)
elif suit == '1':
  print(paper)
elif suit == '2':
  print(scissors)
else :
  print("your type wrong")
suit_int =int(suit)
print("computer respond :")
ai = random.randint(0,2)
if suit_int > 2 or suit_int<0:
  print("i dont understand what are u doin?")
elif ai == 0:
  print(rock)
elif ai == 1:
  print(paper)
else:
  print(scissors)
if suit_int > 2 or suit_int < 0:
  print("wrong type, you lose")
elif suit_int == 0 and ai == 2:
  print("Congrats. you win")
elif suit_int == 1 and ai == 0:
  print("Congrats. you win")
elif suit_int == 2 and ai == 1:
  print("Congrats. you win") 
elif suit_int == ai:
  print("its a Draw")
else:
  print("Oh no, you lose")

#Day 5 Password Generator Project


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

alphabet_for_pass = []
for i in range(0,nr_letters+1):
  alphabet_for_pass.append((letters[random.randint(0,len(letters)-1)]))
print(alphabet_for_pass)
symbols_for_pass = []
for i in range(0,nr_symbols+1):
  symbols_for_pass.append((symbols[random.randint(0,len(symbols)-1)]))
print(symbols_for_pass)
numbers_for_pass = []
for i in range(0,nr_numbers+1):
  numbers_for_pass.append((numbers[random.randint(0,len(numbers)-1)]))
print(numbers_for_pass)
your_EZ_pass = alphabet_for_pass+symbols_for_pass+numbers_for_pass
print(your_EZ_pass)
your_pass = ''.join(your_EZ_pass)
print(f"your pass should be: {your_pass}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

alphabet_for_pass = []
for i in range(0,nr_letters+1):
  alphabet_for_pass.append((letters[random.randint(0,len(letters)-1)]))
print(alphabet_for_pass)
symbols_for_pass = []
for i in range(0,nr_symbols+1):
  symbols_for_pass.append((symbols[random.randint(0,len(symbols)-1)]))
print(symbols_for_pass)
numbers_for_pass = []
for i in range(0,nr_numbers+1):
  numbers_for_pass.append((numbers[random.randint(0,len(numbers)-1)]))
print(numbers_for_pass)
your_EZ_pass = alphabet_for_pass+symbols_for_pass+numbers_for_pass
your_HARD_pass = []
for i in your_EZ_pass:
  your_HARD_pass.append(your_EZ_pass[random.randint(0,len(your_EZ_pass)-1)])
print(your_HARD_pass)
your_pass2 = ''.join(your_HARD_pass)
print(f"your pass should be: {your_pass2}")



# Day 6 Reeborg.org

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_around()
    
while not at_goal() == True:
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right():
        turn_left()
        
# Day 7 Hangman


import random
import hangman_art
import hangman_words
from replit import clear

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_game = False
lives = 6
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
#Create blanks
display = []
for i in chosen_word:
    #print(i)
    display.append("-")

while not end_game:
  guess = input("Guest the letter: ")
  guess = guess.lower()
  clear()
  if guess in display:
    print(f"You've already guessed that: {guess}")
    #Check guessed letter
  for i in range (len(chosen_word)):   
    if guess == chosen_word[i]:
      display[i] = guess
  print(f"{' '.join(display)}")
    #Check if user is wrong.
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's wrong. You lose gonna die.")
    lives -= 1
    if lives == 0:
      end_game =True
      print("you lose. ")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    #Check if user has got all letters.
  if "-" not in display:
      end_of_game = True
      print("You win.")
  print(hangman_art.stages[lives])
  





