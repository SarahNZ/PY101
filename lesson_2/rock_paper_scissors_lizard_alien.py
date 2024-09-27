import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'alien']
FIRST_LETTER_OF_VALID_CHOICES = ['r', 'p', 's', 'l', 'a']

PLAYER_WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'], 
    'paper': ['rock', 'alien'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['alien', 'paper'],
    'alien': ['scissors', 'rock'],
}   

player_score = 0
computer_score = 0

def prompt(message):
    print(f"==> {message}")

def display_winner_of_game(player_choice, computer_choice):
    if player_wins(player_choice, computer_choice):
        prompt("You win!")
        return (1, 0)
    elif player_choice == computer_choice:
        prompt("It's a tie!")
        return (0, 0)
    else:
        prompt("Computer wins!")
        return (0, 1)

def player_wins(player_choice, computer_choice):
    return computer_choice in PLAYER_WINNING_COMBOS[player_choice]

while True:
    prompt(f'Hi Eva. Enter the first letter of your choice: '
           f'{", ".join(VALID_CHOICES)}')
    player_choice = input().lower()

    while player_choice not in FIRST_LETTER_OF_VALID_CHOICES:
        prompt("That's not a valid choice. Please enter the first letter "
               "of your choice again: ")
        player_choice = input()

    # player_choice = [choice for choice in VALID_CHOICES if choice[0] == player_choice][0]

    for choice in VALID_CHOICES: 
        if choice[0] == player_choice:
            player_choice = choice

    computer_choice = random.choice(VALID_CHOICES)
    
    prompt(f"You chose {player_choice}, computer chose {computer_choice}")

    result = display_winner_of_game(player_choice, computer_choice)

    player_score += result[0]
    computer_score += result[1]

    if player_score == 3:
        prompt("You won three games, so you won the match!")
        player_score = 0
        computer_score = 0

    elif computer_score == 3:
        prompt("The computer won three games, so they won the match!")
        player_score = 0
        computer_score = 0
    
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid option. Try again: ")
    
    if answer[0] == 'n':
        break