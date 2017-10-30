#!/usr/bin/env python3
# guessgame.py
# Jessica Lyles
# 10/30/2017
# single number guessing game

from random import randint

MIN = 1
MAX = 200000

targetNumber = randint(MIN, MAX)
print(targetNumber)
