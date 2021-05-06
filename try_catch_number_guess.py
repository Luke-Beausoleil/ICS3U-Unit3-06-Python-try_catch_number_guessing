#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program gets the user to guess a pseudo-random number

import random


def main():
    # this function generates a pseudo-random number and gets the user
    #   to guess the number

    # input
    correct_number = random.randint(0, 9)  # a number from 0 - 9
    guess_as_string = input("Guess a number from 0 - 9: ")

    # process & output
    try:
        guess_as_int = int(guess_as_string)
        if guess_as_int == correct_number:
            print("\nCorrect!")
        else:
            print("\nIncorrect! The number was {0}.".format(correct_number))
    except Exception:
        print("\n{0} is not a valid input".format(guess_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
