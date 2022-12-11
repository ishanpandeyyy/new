from random import *
import array


def gen(max):


    DIIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOWER_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

    UPPER_CASE= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

    SPECIAL_SYMBOL= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~','*', '(', ')']

    COMBINED_LIST = DIIGIT + UPPER_CASE + LOWER_CASE + SPECIAL_SYMBOL

    rand_digit = choice(DIIGIT)
    rand_upper = choice(UPPER_CASE)
    rand_lower = choice(LOWER_CASE)
    rand_symbol = choice(SPECIAL_SYMBOL)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(max-4):
        temp_pass = temp_pass + choice(COMBINED_LIST)

        temp_pass_list = array.array('u', temp_pass)
        shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
    return password


while (True):
    response = int(input("""\n\nTHIS IS PASSWORD GENERATOR
    \n\rPress 0 to Exit
    \n\rPress 1 to generate Password: """))
    if (response == 1):
        len = int(input("Please enter the password length: "))
        if (len >= 12):
            print("\n\nThe random password is: %s" % (gen(len)))
        elif (len < 12):
            print("Please enter a length less than or equal to 12")
        else:
            print("Error Please enter a correct value")
    elif (response == 0):
        break
    else:
        print("Invalid Input")