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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices = [rock, paper, scissors]
computer_choice = random.randint(0,2)
if computer_choice == user_choice:
  print (f"Computer chose {choices[computer_choice]} and you chose {choices[user_choice]}. It's a draw!")

elif computer_choice > user_choice:
  if computer_choice == 2 and user_choice == 0:
    print (f"Computer chose {choices[computer_choice]} and you chose {choices[user_choice]}. You win!")
  else:
    print (f"Computer chose {choices[computer_choice]} and you chose {choices[user_choice]}. You lose!")

elif computer_choice < user_choice:
  if computer_choice == 0 and user_choice == 2:
    print (f"Computer chose {choices[computer_choice]} and you chose {user_choice}. You lose!")
  else:
    print (f"Computer chose {choices[computer_choice]} and you chose {choices[user_choice]}. You win!")


