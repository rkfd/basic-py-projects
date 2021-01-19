#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  File name: app.py
  Author: Satwik Gawand
  Date Created: 19/01/2021
  Date Last Modified: 19/01/2021
  Python Version: 3.8.6
'''

import random

score_computer = 0
score_user = 0

end_game = False

def play(user):
  user = user.lower()
  computer = random.choice(['r','p','s'])

  global score_computer
  global score_user

  if user == computer:
    print(f"It's a Tie. You and the Computer chose {user}")
  
  elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
    score_user += 1
    print(f"You Win. You chose {user} and the Computer chose {computer}.")
  
  elif (computer == 'r' and user == 's') or (computer == 'p' and user == 'r') or (computer == 's' and user == 'p'):
    score_computer += 1
    print(f"You Lose. You chose {user} and the Computer chose {computer}.")

while (end_game == False):
  user_choice = input('\n\nRock (r)(R)\nPaper (p)(P)\nScissors (s)(S)\nView Scores (v)(V)\nEnd Game (e)(E)\n\nEnter your choice: ')

  if user_choice == 'v' or user_choice == 'V':
    print(f"\nComputer's Score: {score_computer}\nYour Score: {score_user}.")
    
    if score_computer == score_user:
      print("Looks like a tie!")
    elif score_computer > score_user:
      print("The Computer seems to have taken the lead!")
    elif score_computer < score_user:
      print("You are ahead, keep up the lead!")
    else:
      print("Unknown Error.")
  
  elif user_choice == 'e' or user_choice == 'E':
    print(f"\nComputer's Score: {score_computer}\nYour Score: {score_user}.")

    if score_computer > score_user:
      score_diff = score_computer-score_user
      print(f"Computer Wins by {score_diff} point(s)!")
    elif score_computer < score_user:
      score_diff = score_user - score_computer
      print(f"You Win by {score_diff} point(s)!")

    end_game = True
  
  else:
    play(user_choice)