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

choice = input("Lets play Rock, Paper, Scissors!\nRock = 1 , Paper = 2, Scissors = 3\n")

if choice == 1:
    print(rock)
elif choice == 2:
    print(paper)
elif choice == 3:
    print(scissors)

computer_choice = random.randint(1, 3)

print(choice)
