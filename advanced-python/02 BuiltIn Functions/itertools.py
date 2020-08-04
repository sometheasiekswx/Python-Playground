# advanced iteration functions in the itertools package

import itertools


def testFunction(x):
    return x <= 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    # cycle1 = itertools.cycle(seq1)
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))

    # TODO: use count to create a simple counter
    count1 = itertools.count(start=10, step=2)
    # print(next(count1))
    # print(next(count1))
    # print(next(count1))
    # print(next(count1))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    # acc = itertools.accumulate(vals, min)
    # print(list(acc))
    # acc = itertools.accumulate(vals, max)
    # print(list(acc))
    # acc = itertools.accumulate(vals)
    # print(list(acc))

    # TODO: use chain to connect sequences together
    chained_seq = itertools.chain('AS', '134', '34', 'sdf', ['sd', 1, ['2', '3']])
    print(list(chained_seq))

    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))


if __name__ == "__main__":
    main()
