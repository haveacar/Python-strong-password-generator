import random
from datetime import datetime

# this can be changed to your password length
MAX_LEN = 12

# list comprehension of indexes Low and Up characters, numbers
LOCASE_CHARACTERS = [x for x in range(97, 123)]
UPCASE_CHARACTERS = [i for i in range(65, 90)]
NUMBERS = [j for j in range(48, 58)]
SYMBOLS = [35, 36, 37, 38, 40, 41, 42, 59, 60, 62, 64, 94, 123, 125, 126]

# list of all indexes together
temp_pass = LOCASE_CHARACTERS + UPCASE_CHARACTERS + NUMBERS

# get special index with datetime "seconds"
temp_pass2 = temp_pass[int(datetime.now().strftime("%S"))]

# get special random symbol or character
temp_pass3 = random.choice(SYMBOLS)


def gen_password():
    """
    loop func, generate random password and convert indexes
    to characters.
    Last character generated from seconds
    :return:
    """

    password = ""
    for i in range(MAX_LEN - 2):
        password += chr(random.choice(temp_pass))

    password += chr(temp_pass2)
    password += chr(temp_pass3)
    print(password)


gen_password()
