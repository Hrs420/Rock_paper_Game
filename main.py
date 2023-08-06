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

import random

choice = int(
    input(
        "What do you Choose? Type 0 for Rock, 1 for paper, 2 for Scissors\n"))

if (choice == 0):
    print(rock)
elif (choice == 1):
    print(paper)
elif (choice == 2):
    print(scissors)
else:
    print("Invalid Input\n")

print("Computer Choice")

pc_choice = int(random.randint(0, 2))

if (pc_choice == 0):
    print(rock)
elif (pc_choice == 1):
    print(paper)
elif (pc_choice == 2):
    print(scissors)
else:
    print("Invalid Input")

if (choice == pc_choice):
    print("It's a Draw ")
elif (choice == 0 and pc_choice == 1):
    print("You Lose!")
elif (choice == 0 and pc_choice == 2):
    print("You Win !")
elif (choice == 1 and pc_choice == 2):
    print("You Lose!")
elif (choice == 1 and pc_choice == 0):
    print("You Win!")
elif (choice == 2 and pc_choice == 0):
    print("You Lose !")
elif (choice == 2 and pc_choice == 1):
    print("You Win !")
