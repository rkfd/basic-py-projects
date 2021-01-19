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
import string

from words import words

def get_valid_word(words):
  word = random.choice(words)
  while '-' in word or ' ' in word:
    word = random.choice(words)
  
  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()

  while len(word_letters) > 0:
    print("You've used these letters: ", ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('\nCurrent Word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
    
    elif user_letter in used_letters:
      print("You've already used that character. Please try again.")

    else:
      print('Invalid character. Please try again.')

  print(f"\n\nYay! You got the word.\nThe word is: {word}.\nYou solved this puzzle in {len(used_letters)} attempts.\n\n")

hangman()