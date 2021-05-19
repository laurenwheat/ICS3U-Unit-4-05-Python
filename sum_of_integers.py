#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game

def main():

    total = 0

    num = input("Enter how many numbers you want to add up: ")

    try:
        num_int = int(num)

        if num_int > 0:
            while num_int > 0:
                user_add = input("Enter a number to add: ")
                try:
                    user_add_int = int(user_add)

                    num_int = num_int - 1
                    if user_add_int < 0:
                        print("Negative numbers will not be added!!!")
                        continue
                    else:
                        total = total + user_add_int
                except Exception:
                    print("That's not a number!!!")

            print("The sum is {}.".format(total))
        else:
            print("{} is not a valid input!!!".format(num_int))
    except Exception:
        print("That is not a number!!!")
    finally:
        print("Thanks for playing <3")


if __name__ == "__main__":
    main()
