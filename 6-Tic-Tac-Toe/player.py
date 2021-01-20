#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
  File name: player.py
  Author: Satwik Gawand
  Date Created: 20/01/2021
  Date Last MOdified: 20/01/2021
  Python Version: 3.8.6
'''

import math
import random


class Player():

  def __init__(self, letter):
    self.letter = letter
  
  def get_move(self, game):
    pass


class RandomComputerPlayer(Player):

  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
    square = random.choice(game.available_moves())


class HumanPlayer(Player):

  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
    valid_square = False
    val = None

    while not valid_square:
      square = input(self.letter + '\'s turn. Input move (0-9): ')

      try:
        val = int(square)
        if val not in game.available_moves():
          raise ValueError
        valid_square = True
      except:
        print('Invalid square. Try again.')

    return val