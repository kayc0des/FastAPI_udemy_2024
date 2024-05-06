''' String Assignment '''

import math

days_to_birthday = input('How many days until your birthday? ')

try:
    days = int(days_to_birthday)
except Exception as e:
    print(f'There was an error: e')

def calc_weeks(num):
    if not isinstance(num, int):
        raise TypeError('Days to your birthday must be an integer value')
    value = math.floor(num / 7)
    return value

num_weeks = calc_weeks(days)
print(f'There are approximately {num_weeks} weeks until your birthday')