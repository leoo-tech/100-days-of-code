#tip calculator

print("Welcome to the tip calculator!")
bill = float(input("Total bill: $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people will split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")

"""#band generator name

forme sua banda aqui!
"""

print("Welcome to the Band Name Generator.")
street = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)

"""# ano bissexto
cheque se um ano em particular foi, ou será, bissexto
"""

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
  if year % 100 !=0:
    if year % 400 == 0:
      print("leap year")
    else:
      print("not leap year")
  else:
    print("leap year")
else:
  print("not leap year")

# alternative version
# if year % 4 == 0:
#   print("leap year")
# elif year % 100 != 0:
#   print("not leap year")
# elif year % 400 == 0:
#   print("leap year")
# else:
#   print("not leap year")

"""# caça ao tesouro
este desafio foi um dos mais complicados durante o curso. para um iniciante, é uma ótima forma de prática
"""

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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input('You\'re at a crossroad which direction you wanna go? Type "left" or "right". \n').lower()

if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input('You arrive at the island unharmed.There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n').lower()
    if choice3 == "red":
      print("Entered in a room full of fire. Game Over...")
    elif choice3 =="yellow":
      print("You found the fuck*n treasure! You Win!")
    elif choice3 =="blue":
      print("You enter a room of beasts. Game Over...")
    else:
      print("This door does not exists! Game Over...")
  else:
    print("You got attacked by an angry trout and Sherk couldn't saved you. Game Over...")
else:
  print("You met with the Dracarys\' dragon. Game Over...")

"""# pedra, papel e tesoura"""

import random

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

#Write your code below this line 👇
print("Welcome to RPS!")
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_choice >= 3 or user_choice < 0:
  print("Invalid number! You lose")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice == computer_choice:
    print("It's a draw")
  elif (user_choice == 0 and computer_choice == 2) or (user_choice > computer_choice):
    print("You win!")
  else:
    print("You lose!")