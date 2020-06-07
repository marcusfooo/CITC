from time import sleep
from random import randrange
from random import choice


while True:
  option_list = ["rock", "paper", "scissors"]
  player_input = input("Choose rock paper or scissors? ")

  computer_input = choice(option_list)

  if computer_input == player_input:
    print("Draw!")

  elif player_input == "scissors":
    if computer_input == "rock":
      print("We lose!")
    elif computer_input=="paper":
      print("We win!")

  elif player_input == "paper":
    if computer_input == "scissors":
      print("We lose!")
    elif computer_input=="rock":
      print("We win!")

  elif player_input == "rock":
    if computer_input == "paper":
      print("We lose!")
    elif computer_input=="scissors":
      print("We win!")
