# demonstrate built-in utility functions


def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]

    # TODO: any will return true if any of the sequence values are true
    print('----- any() -----')
    print(any(list1))
    print(any([]))
    print(any([[1]]))
    print(any([[0]]))
    print(any([[0]][0]))

    # TODO: all will return true only if all values are true
    print('----- all() -----')
    print(all(list1))
    print(all([]))  # all returns true
    print(all([[1]]))
    print(all([[0]]))
    print(all([[0]][0]))


if __name__ == "__main__":
    main()
