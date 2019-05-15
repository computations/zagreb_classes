#!/usr/bin/env python3

min_guess = 0
max_guess = 100

print("Pick a number in the range [%d,%d)" % (min_guess, max_guess))

guess = 50
for i in range(20):
    answer = input("Is your number greater than or equal to %d? " % guess)
    if answer.lower() == "yes":
        min_guess = guess
        guess += (max_guess - guess)//2
    else:
        max_guess = guess
        guess += (min_guess - guess)//2
    if max_guess == guess or guess == min_guess:
        answer = input("is your number %d? " % guess)
        if answer == "yes":
            print("yay!!")
            break
