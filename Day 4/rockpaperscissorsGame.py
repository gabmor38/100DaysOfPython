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

choiceItems = [rock, paper, scissors]
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissors"))
userChoiceItem = choiceItems[userChoice]
computerChoice = random.choice(choiceItems)

print(f"comp:{computerChoice}")
print(f"yourChoice:{userChoiceItem}")

if computerChoice == userChoiceItem:
    print("it's a draw!")
elif computerChoice == rock and userChoiceItem == scissors:
    print("you loose!")
elif computerChoice == scissors and userChoice == paper:
    print("you loose!")
elif computerChoice == paper and userChoice == rock:
    print("you loose!")
else:
    print("you win!")


