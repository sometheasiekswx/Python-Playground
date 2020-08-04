# use transform functions like sorted, filter, map


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_lower(x):
    if x.islower():
        return True
    else:
        return False


def squareFunc(x):
    return x ** 2


def pass_or_fail(x):
    if x >= 50:
        return 'Pass'
    else:
        return 'Fail'


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (34, 81, 89, 94, 78, 61, 66, 99, 74, 40)

    # TODO: use filter to remove items from a list
    # evens = list(filter(is_even, nums))
    # print(evens)

    # TODO: use filter on non-numeric sequence
    # lowers = list(filter(is_lower, chars))
    # print(lowers)

    # TODO: use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares)

    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades, reverse=True)
    grade_status = list(map(pass_or_fail, grades))
    print(grade_status)


if __name__ == "__main__":
    main()
