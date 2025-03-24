# 20241126

from random import randint
from time import time

point = total_played = skip = 0
total_time = 0

weekly_days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
month_dict = {'JAN': 31,
         'FEB': 28,
         'MAR': 31,
         'APR': 30,
         'MAY': 31,
         'JUN': 30,
         'JUL': 31,
         'AUG': 31,
         'SEP': 30,
         'OCT': 31,
         'NOV': 30,
         'DEC': 31}


def instruction():
    print(
    """
    You will be provided with a random date starting from 1901 to 2099.
    You have to input integers from 1 to 7 for the weekly day. 1 refers to SAT and so on...
    Type '-' if you want to skip.
    Type '.' if you want to exit the game.
    """
    )
# The game will be skipped if you don't maintain format.


def run():
    global d, m, y, day, total_time
    d, m, y = generate_date()
    print(return_date_str(d, m, y))
    day = determine_day(d, m, y)
    while True:
        t1 = time()
        user = input("What day is it? ")
        if evaluate(day, user):
            print(f"{return_date_str(d, m, y)}: {weekly_days[day]}")
            correct_ans()
        elif user=="-":
            print(f"{return_date_str(d, m, y)}: {weekly_days[day]}")
            skip_ans()
        elif user==".":
            print(f"{return_date_str(d, m, y)}: {weekly_days[day]}")
            result()
            return
        else:
            wrong_ans()
            continue
        t = time()-t1
        print(f"time: {t:.2f} second")
        print()
        total_time += t
        break
    run()


def generate_date():
    y = randint(1901, 2099)
    m = randint(0, 11)
    if y%4==0 and m==1:
        d = randint(1, 29)
    else:
        d = randint(1, list(month_dict.values())[m])
    return d, m, y


def return_date_str(d:int, m:int, y:int)->str:
    return f"{d}-{list(month_dict.keys())[m]}-{y}"


def determine_day(d:int, m:int, y:int)->int:
    cumulative_month = 0
    for i in range(m):
        cumulative_month += month_dict[list(month_dict.keys())[i]]
    total_day = y*365 + y//4 + cumulative_month + d
    if y%4==0 and m<2:
        total_day -= 1
    return total_day%7


def evaluate(day:int, user:str)->bool:
    if day==0:
        day = 7
    return str(day)==user


def correct_ans():
    global point, total_played
    point += 1
    total_played += 1
    print("!!! Correct answer !!!")


def skip_ans():
    global skip
    skip += 1
    print("--- The question was skipped ---")


def wrong_ans():
    global total_played
    total_played += 1
    print("?!? Incorrect answer. Let's try again !?!")


def result():
    percent = point*100/total_played if total_played!=0 else -1
    print()
    if percent!=-1:
        print(f"Score: {point}/{total_played}, accuracy: {percent:.2f}%")
    else:
        print(f"Score: {point}/{total_played}, accuracy: NO RECORD")
    print(f"Total time: {total_time:.2f} second")
    print(f"Total skipped: {skip}")


# driver code
instruction()
run()
