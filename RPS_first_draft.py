import random


# compare_function compares the rock, paper, scissors choice of the user and computer, then prints who has won.
def compare_function(computer, user, computer_wins, user_wins):
    if computer == 0 and user == 2:
        print("Computer wins!")
        computer_wins += 1
    elif user == 0 and computer == 2:
        print("You win!")
        user_wins += 1
    elif computer > user:
        print("Computer wins!")
        computer_wins += 1
    elif user > computer:
        print("You win!")
        user_wins += 1
    elif user == computer:
        print("It's a draw!")
    print("User: ", user_wins, " ", "Computer: ", computer_wins)
    return computer_wins, user_wins


# player_1_function asks user for input and confirms choice, returns value
def player_function():
    player_choice = int(input("Type in 0 for rock, 1 for paper, or 2 for scissors: "))
    if player_choice == 0:
        print("You chose rock")
    elif player_choice == 1:
        print("You chose paper")
    elif player_choice == 2:
        print("You chose scissors")
    else:
        print("Input invalid")
    return int(player_choice)


# computer_function chooses random integer between 0-2, prints computer's choice and returns value
def computer_function():
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose rock")
    elif computer_choice == 1:
        print("Computer chose paper")
    elif computer_choice == 2:
        print("Computer chose scissors")
    return computer_choice

computer_wins = 0
user_wins = 0
rounds = 1

while rounds <= 3:
    print("Round:", rounds)
    player = player_function()
    computer = computer_function()
    computer_wins, user_wins = compare_function(computer, player, computer_wins, user_wins)
    rounds += 1
