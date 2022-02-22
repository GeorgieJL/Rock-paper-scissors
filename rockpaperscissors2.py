import random


# function shows the user whether the computer chose rock, paper or scissors
def computer_choice(integer):
    if integer == 0:
        print("Computer chose rock")
    elif integer == 1:
        print("Computer chose paper")
    elif integer == 2:
        print("Computer chose scissors")


# function that compares the computer_attempt and user_attempt to decide who wins
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



# Rock (R) = 0
# Paper (P) = 1
# Scissors (S) = 2

# user prompted to enter R, P or S, and assigns input to user_attempt
user_attempt = input("Enter R for rock, P for paper or S for scissors: ")

# conditional statements to confirm user choice, and convert it to integer to be compared with computer choice later
if user_attempt == "R":
    user_attempt = 0
    print("You chose rock...")
elif user_attempt == "P":
    user_attempt = 1
    print("You chose paper...")
elif user_attempt == "S":
    user_attempt = 2
    print("You chose scissors...")
else:
    print("Invalid selection. User may only input R, P or S.")

# computer generates a random number between 0-2
computer_attempt = random.randint(0, 2)

# the computer_attempt is put in the computer_choice function to print whether computer chose rock, paper or scissors
computer_choice(computer_attempt)

# computer_attempt and user_attempt put into compare_function to see who won
compare_function(computer_attempt, user_attempt)



