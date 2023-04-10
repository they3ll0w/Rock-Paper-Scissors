import random
choices = ["rock", "paper", "scissors"]
pchoice = input("rock, paper, scissors? : ")
cchoice = random.choice(choices)
print("Computer's choise: "+ cchoice)
if pchoice == cchoice:
    print("This is a draw")

if pchoice == "rock" and cchoice =="scissors":
    print("Player wins")
if pchoice == "rock" and cchoice =="paper":
    print("Player losses")

if pchoice == "paper" and cchoice =="rock":
    print("Player wins")
if pchoice == "paper" and cchoice =="scissors":
    print("Player losses")

if pchoice == "scissors" and cchoice =="paper":
    print("Player wins")
if pchoice == "scissors" and cchoice =="rock":
    print("Player losses")

