#!/usr/bin/env python3
# guessgame.py
# Jessica Lyles
# 10/30/2017
# single number guessing game

from random import randint

MIN = 1
MAX = 20

targetNumber = randint(MIN, MAX)

prompt = ('Please guess a number from ' + str(MIN) + ' to ' + str(MAX) + ': ')
guess = int(input(prompt))
print(guess)
