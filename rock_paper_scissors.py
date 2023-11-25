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

"""
Game rules
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
"""

import random
list_of_choices = [rock, paper, scissors]
computer_choice_index = random.randrange(len(list_of_choices))
user_choice = int(input("Chosse what would like to play with 1.rock, 2.paper, 3.scissors\n "))
if user_choice <= 3:
    if user_choice == 1:
        user_choice = list_of_choices[0]
    elif user_choice == 2 :
        user_choice= paper
    elif user_choice == 3:
        user_choice = scissors 
    user_choice_index = list_of_choices.index(user_choice)
    computer_choice = list_of_choices[computer_choice_index]
    print(f"computer choice {computer_choice}")
    print(f"user choice {user_choice}")
    if user_choice_index ==  computer_choice_index:
        print("Draw")
    if user_choice_index == 0:
        if computer_choice_index== 2:
            print("You won")
        else:
            print("You Lost better luck next time")
    if user_choice_index == 2:
        if computer_choice_index == 1:
            print("You Won")
        else:
            print("You Lost better luck next time")
    if user_choice_index == 1:
        if computer_choice_index == 0:
            print("You Won")
        else:
            print("You Lost better luck next time")
    # if int(user_choice) > 3:
    #     print("end game")
else:
    print("please choose between 1,2,3 only!! \n")
# print(f'user choice {user_choice}')
# # list_of_choices.index()
# # print(f("computer choice {list_of_choices[computer_choice]}"))


# print(f"user choice idex {user_choice_index}")
# print(f"computer choice index {[computer_choice_index]}")
# print(f'type of user choice {type(user_choice)}')
#Comparison

# # if user_choice == 1:
    