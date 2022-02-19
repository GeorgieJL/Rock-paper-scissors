import random

# function shows user what the computer chose
def computer_choice(integer):
    if integer == 0:
        print("Computer chose rock")
    elif integer == 1:
        print("Computer chose paper")
    elif integer == 2:
        print("Computer chose scissors")


# function that compares computer_attempt and user_attempt
def compare_function(computer, user):
    if user_attempt == 0 and computer_attempt == 2:
        print("You win!")
    elif computer_attempt == 0 and user_attempt == 2:
        print("Computer wins")
    elif computer_attempt > user:
        print("Computer won")
    elif user_attempt > computer_attempt:
        print("You won!")
    elif user_attempt == computer_attempt:
        print("It's a draw!")


# user prompted to enter R, P or S
user_attempt = input("Enter R for rock, P for paper or S for scissors: ")
if user_attempt == "R":
    user_attempt = 0
    print("You chose rock")
elif user_attempt == "P":
    user_attempt = 1
    print("You chose paper")
elif user_attempt == "S":
    user_attempt = 2
    print("You chose scissors")
else:
    print("Invalid selection")


# computer generates a random number between 0-2
computer_attempt = random.randint(0, 2)

# function prints computer rock, paper, scissors choice
computer_choice(computer_attempt)

# function compares computer_attempt and user_attempt and prints who won
compare_function(computer_attempt, user_attempt)


