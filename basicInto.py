import random

choices = ['rock','paper','scissors']

computer_Choice = random.choice(choices)

print("Welcome to Python Rock Paper Scissors\n")
user_Choice = input('Please enter your choice of rock, paper or scissors:\n')

if user_Choice == computer_Choice:
    print('You tied!')
elif user_Choice == 'rock' and computer_Choice == 'scissors':
    print('You win!')
elif user_Choice == 'paper' and computer_Choice == 'rock':
    print('You win!')
elif user_Choice == 'scissors' and computer_Choice == 'paper':
    print('You win!')
else:
    print('You lose!')
