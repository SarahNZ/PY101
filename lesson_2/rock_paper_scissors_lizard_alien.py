import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'alien']
FIRST_LETTER_OF_VALID_CHOICES = ['r', 'p', 's', 'l', 'a']

WINNING_COMBOS = {
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
        update_scoreboard(1, 0)
    elif player_choice == computer_choice:
        prompt("It's a tie!")
    else:
        prompt("Computer wins!")
        update_scoreboard(0, 1)

def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

def update_scoreboard(player_points, computer_points):
    global player_score
    player_score += player_points

    global computer_score
    computer_score += computer_points

def reset_scores_to_zero():
    global player_score
    player_score = 0

    global computer_score
    computer_score = 0

while True:
    prompt(f'Enter the first letter of your choice: '
           f'{", ".join(VALID_CHOICES)}')
    player_choice = input().lower()

    while player_choice not in FIRST_LETTER_OF_VALID_CHOICES:
        prompt("That's not a valid choice. Please enter the first letter "
               "of your choice again: ")
        player_choice = input()

    match player_choice:
        case 'r':
            player_choice = "rock"
        case 'p':
            player_choice = "paper"
        case 's':
            player_choice = "scissors"
        case 'l':
            player_choice = "lizard"
        case 'a':
            player_choice = "alien"

    computer_choice = random.choice(VALID_CHOICES)
    
    prompt(f"You chose {player_choice}, computer chose {computer_choice}")

    display_winner_of_game(player_choice, computer_choice)

    if player_score == 3:
        prompt("You won three games, so you won the match!")
        reset_scores_to_zero()

    elif computer_score == 3:
        prompt("The computer won three games, so they won the match!")
        reset_scores_to_zero()
    
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid option. Try again: ")
    
    if answer[0] == 'n':
        break