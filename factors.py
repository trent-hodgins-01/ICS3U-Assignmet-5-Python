# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/13/2021
# This is an factor program
# The user enters in a number
# The program displays the factors


def main():
    # this function determines the factors

    # input
    number_as_string = input("Enter a number to see all factors (integer): ")

    # input process and output
    try:
        number = int(number_as_string)
        for counter in range(1, number + 1):
            if number % counter == 0:
                print("{0}, ".format(counter))

    except Exception:
        print("Invalid input.")

    print("\nDone")


if __name__ == "__main__":
    main()
