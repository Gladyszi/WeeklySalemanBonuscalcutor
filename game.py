#Rock, Paper, Scissors


import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Make your pick- rock, paper, scissors: ").lower()

computer_score = 0
user_score = 0

play_again = ""

while True:
    play_again == "yes"
    user = input("Make your pick-rock, paper, scissors: ").lower()

    while user not in choices:
        user = input("Please pick a valid option -rock, paper, scissors: ").lower()

    if computer == user:
        print(f"user: {user}")
        print(f"computer: {computer}")
        print("Its a Tie!")

    elif computer == "rock" and user == "paper":
        print(f"user: {user}")
        print(f"computer: {computer}")
        print("You Win!")
        user_score += 1
        computer_score += 0

    elif computer == "rock" and user == "scissors":
        print(f"user: {user}")
        print(f"computer: {computer}")
        print("You Lose!")
        user_score += 0
        computer_score += 1

    elif computer == "paper" and user == "rock":
        print(f"user: {user}")
        print(f"computer: {computer}")
        print("You Lose!")
        user_score += 0
        computer_score += 1


    elif computer == "paper" and user == "scissors":
        print(f"user: {user}")
        print(f"computer: {computer}")
        print(f"You Win!")
        user_score += 1
        computer_score += 0

    elif computer == "scissors" and user == "rock":
        print(f"user: {user}")
        print(f"computer: {computer}")
        print("You Win!")
        user_score += 1
        computer_score += 0


    elif computer == "scissors" and user == "paper":
        print(f"user: {user}")
        print(f"computer: {computer}")
        print("You Lose!")
        user_score += 0
        computer_score += 1

    play_again=input("Do you want to play again? Yes/ No: ").lower()
    if play_again!="yes":
        print(f"Total score: User_score:{user_score} Computer_score: {computer_score: }")
        print("Bye! See you some other time")
        quit()


