# Rock Paper Scissors

import random
import hand

# Hands available
hands = [hand.rock, hand.paper, hand.scissors]

print("Welcome to Rock, paper, scissors game!\n")

# User choice
user_choice = input(
    "What do you choose: 0 for rock, 1 for paper, 2 for scissors?\n")

# Computer choice
random_number = random.randint(0, len(hands))
computer_choice = hands[random_number - 1]

# Compare user choice against computer
if user_choice == "0" and computer_choice == hands[0]:
    print(hands[0])
    print(f"The computer chose {computer_choice}\n")
    print("It's a draw!")
elif user_choice == "0" and computer_choice == hands[1]:
    print(hands[0])
    print(f"The computer chose {computer_choice}\n")
    print("Paper beats rock, you lose.")
elif user_choice == "0" and computer_choice == hands[2]:
    print(hands[0])
    print(f"The computer chose {computer_choice}\n")
    print("Rock beats scissors, you win!")

if user_choice == "1" and computer_choice == hands[0]:
    print(hands[1])
    print(f"The computer chose {computer_choice}\n")
    print("Paper beats rock, you win!")
elif user_choice == "1" and computer_choice == hands[1]:
    print(hands[1])
    print(f"The computer chose {computer_choice}\n")
    print("It's a draw!")
elif user_choice == "1" and computer_choice == hands[2]:
    print(hands[1])
    print(f"The computer chose {computer_choice}\n")
    print("Scissors beat paper, you lose.")

if user_choice == "2" and computer_choice == hands[0]:
    print(hands[2])
    print(f"The computer chose {computer_choice}\n")
    print("Rock beat scissors, you lose.")
elif user_choice == "2" and computer_choice == hands[1]:
    print(hands[2])
    print(f"The computer chose {computer_choice}\n")
    print("Scissors beat paper, you win!")
elif user_choice == "2" and computer_choice == hands[2]:
    print(hands[2])
    print(f"The computer chose {computer_choice}\n")
    print("It's a draw!")
