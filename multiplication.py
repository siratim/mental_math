# 20241126

from random import randint
from time import time, sleep
# from IPython.display import clear_output

point = total_played = skip = 0
total_time = 0


def run():
    global num1, num2, mult, total_time
    instruction()
    num1, num2, mult = round((2, 99), (11, 99))
    while True:
        t1 = time()
        user = input(f"{num1}X{num2} = ")
        if str(mult)==user:
            correct_ans()
        elif user=="-":
            skip_ans()
        elif user==".":
            result()
            return
        else:
            wrong_ans()
            continue
        t = time()-t1
        total_time += t
        print(f"time: {t:.2f}")
        break
    # sleep(3)
    # clear_output()
    run()


def instruction():
    print(
    """
    You will be provided with some multiplication problems.
    You have to provide the answer. The game will be skipped if you type '-'.
    Type '.' if you want to exit the game. Then score will appear.
    """)


def round(range1=(2, 99), range2=(11, 99)):
    num1 = randint(*range1)
    num2 = randint(*range2)
    mult = num1*num2
    return num1, num2, mult


def correct_ans():
    # function can access but can't modify the global variable without declaration
    global point, total_played
    point += 1
    total_played += 1
    print("Correct answer!")


def skip_ans():
    global total_played, skip
    skip += 1
    # total_played += 1
    print(f"{num1}X{num2} = {mult}")


def wrong_ans():
    global total_played
    total_played += 1
    print("Incorrect answer. Let's try again")


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
run()
