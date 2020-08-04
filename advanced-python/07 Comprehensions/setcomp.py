# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 5, 5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # TODO: build a set of unique Fahrenheit temperatures
    print({(t * 9 / 5) + 32 for t in ctemps})


    # TODO: build a set from an input sousrce
    sTemp = 'The quick brown fox jumped over the lazy dog.'
    print({c.upper() for c in sTemp if not c.isspace()})


if __name__ == "__main__":
    main()
