# use iterator functions like enumerate, zip, iter, next

import os

def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))

    # TODO: iterate using a function and a sentinel
    # with open(f'testfile.txt', 'r') as f:
    #     for line in iter(f.readline, ''):
    #         print(line)

    # TODO: using enumerate reduces code and provides a counter
    # for i, day in enumerate(days, start=1):
    #     print(f'{i}. {day}')

    # TODO: use zip to combine sequences
    for i, (eng, fr) in enumerate(zip(days, daysFr)):
        print(f'{i}. {eng}, which is {fr} in french')



if __name__ == "__main__":
    main()
