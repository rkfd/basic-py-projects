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

def computer_guess(x):
  low = 1
  high = x
  feedback = ''

  while feedback != 'c':
    if low != high:
      guess = random.randint(1,x)
    else:
      guess = low
    
    feedback = input(f"\nIs the number {guess} too high (H), too low (L), or correct (C)?: ")
    if feedback == 'h' or feedback == 'H':
      high = guess-1
    elif feedback == 'l' or feedback == 'L':
      low = guess + 1

  print(f"\nYay! The computer guessed your number, {guess}, correctly.")

guess_range = int(input("Set a Range for the number: "))
computer_guess(guess_range)