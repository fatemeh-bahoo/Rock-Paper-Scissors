import random
rock = '''
    __________
---'   _______)
      (________)
      (________)
      (_______)
---.__(______)

'''
paper ='''
    _________
---'   ______)____  
          ________)  
          _________)  
         _________)
---.____________)  

'''
scissors ='''
    _______
---'   ____)______  
          ________)_  
       _____________)  
      (_________)
---.__(_______) 

'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You Chose an invalid number, You lose!")
print(game_images[user_choice])

computer_choice = random.randint(0 , 2)
print("Computer Chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice :
    print("You Win!")
elif computer_choice == user_choice:
    print("It's a draw!")