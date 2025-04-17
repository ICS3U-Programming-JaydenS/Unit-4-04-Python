#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: April 16, 2025
# This program tells gives user multiple guesses for a random number

import random


def main():

    # Get random variable
    random_number = random.randint(0, 9)

    while True:

        # Get the user number
        user_number_as_string = input("Enter a number 1-9: ")
        try:

            # Converts user num to int
            user_number_as_int = int(user_number_as_string)

            # If its negative this happens
            if user_number_as_int < 0:
                print((user_number_as_int), "is not a possible guess")

            elif user_number_as_int > 9:
                print((user_number_as_int), "is not a possible guess")

            # If not any of those code continues
            elif random_number != user_number_as_int:
                print("Your wrong the answer is not ", (user_number_as_int))

            # Checks if you got it right or wrong
            else:
                print("")
                print("Your right! It is", (random_number))
                break

        # If user num is not a int this happens
        except Exception:
            print(
                (user_number_as_string), "is not a possible guess. (Only whole numbers)"
            )


if __name__ == "__main__":
    main()
