import random
user_action=input("chose between rock,paper and scissor")
possible_actions=["rock","paper","scissor"]
computer_action=(random.choice(possible_actions))
if computer_action==user_action:
    print("both have entered the same choice the game was a tie")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")