import os
import platform
from binary import Binary


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def menu():
    is_valid = False
    while not is_valid:
        number = input('Write a number: ')

        if(is_integer(number)):
            try:
                binary_challenge = Binary()
                binary_conversion, gap_max = binary_challenge.binary_gap_without_library(
                    int(number))
                is_valid = True

                print(
                    f"\nBinary conversion -> {bcolors.OKGREEN}{binary_conversion}{bcolors.ENDC}")

                if(gap_max > 0):
                    print(
                        f"Binary gap -> {bcolors.OKGREEN}{gap_max}{bcolors.ENDC}")
                else:
                    print(
                        f"The entered number doesn't contain a binary gap. Binary gap -> {bcolors.OKGREEN}{gap_max}{bcolors.ENDC}")
            except(ValueError):
                error_message(f'An error has occurred: {ValueError}')
        else:
            warning_message('Please write a whole number')

    question = input(
        '\nDo you want to try another number? (S/n) \n').lower()[:1]

    if(question == 's' or question == 'y'):
        clear_terminal()
        menu()
    else:
        close_program()


def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def close_program():
    clear_terminal()
    exit(0)


def warning_message(message):
    print(f"{bcolors.WARNING}{message}{bcolors.ENDC}")


def error_message(message):
    print(f"{bcolors.FAIL}{message}{bcolors.ENDC}")


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


print('Hello')
menu()