import random

options = ('rock', "paper", "scissors")
running = True
player_score = 0
computer_score = 0

while running:
    computer = random.choice(options)
    player = None
    
    
    while player not in options:

        player = input("Enter a choice (rock, paper, scissors) ")

        print(f"Player: {player} ")
        print(f"Computer: {computer} ")

        if player == computer:
            player_score +=1
            computer_score +=1
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            player_score += 1
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
            player_score += 1
        elif player == "scissors" and computer == "paper":
            player_score += 1
            print("You win")
        else:
            computer_score += 1
            print("You lose!")

        play_again = input("Play again (y/n)").lower()
        if not play_again == "y":
            running = False
        print(f"Your score: {player_score}  Computer score: {computer_score}")
        