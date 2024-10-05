import random
def calculate_outcome(user_action,computer_action):
    if computer_action==user_action:
        print("both have entered the same choice the game was a tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            winner="user",loser="computer"
        else:
            winner="computer",loser="user"        
    elif user_action == "paper":
        if computer_action == "rock":
            winner="user",loser="computer"
        else:
            winner="computer",loser="user"
    elif user_action == "scissors":
        if computer_action == "paper":
            winner="user",loser="computer"
        else:
            winner="computer",loser="user"
            return winner and loser 
        user_action=input("chose between rock,paper and scissor")
possible_actions=["rock","paper","scissor"]
computer_action=(random.choice(possible_actions)) 
print(computer_action)      
        