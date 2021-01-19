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

def guess(x):
  random_number = random.randint(1,x)
  guess = 0
  while guess != random_number:
    guess = int(input(f"\nGuess a number between 1 and {x}: "))

    if guess < random_number:
      print("Incorrect. You are too low.")
    elif guess > random_number:
      print("Incorrect. You are too high.")
  
  print(f"\nCorrect. You have guessed the number {random_number}")

guess_range = int(input("Set the range for guessing: "))

guess(guess_range)