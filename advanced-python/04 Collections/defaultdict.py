# Demonstrate the usage of defaultdict objects

from collections import defaultdict

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # # use a dictionary to count each element
    # fruitCounter = {}
    #
    # # Count the elements in the list
    # for fruit in fruits:
    #     if fruit in fruitCounter.keys():
    #         fruitCounter[fruit] += 1
    #     else:
    #         fruitCounter[fruit] = 1

    # # use a dictionary to count each element
    # fruitCounter = defaultdict(int)
    #
    # # Count the elements in the list
    # for fruit in fruits:
    #     fruitCounter[fruit] += 1

    # use a dictionary to count each element
    fruitCounter = defaultdict(lambda: 10)

    # Count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
