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
set = [rock, paper, scissors]
choice = set[int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissors."))]
print(choice)

comptchoice = random.choice(set)
print("computer's choice: \n" + comptchoice)

if choice == comptchoice:
    print("its a Draw")

while choice == set[0]:
    if comptchoice == set[1]:
        print("computer wins")
    else:
        print("you win")
    break

while choice == set[1]:
    if comptchoice == set[2]:
        print("computer wins")
    else:
        print("you win")
    break

while choice == set[2]:
    if comptchoice == set[0]:
        print("computer wins")
    else:
        print("you win")
    break
        
