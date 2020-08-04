# Demonstrate the usage of Counter objects

from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
              "Kevin", "James", "James", "Melanie", "Penny", "Steve", "Frank"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy", "Frank", "Frank"]

    # TODO: Create a Counter for class1 and class2
    c1 = Counter(class1)
    print(c1)

    c2 = Counter(class2)
    print(c2)

    # TODO: How many students in class 1 named James?
    print(c1['James'])

    # TODO: How many students are in class 1?
    print(sum(c1.values()))

    # TODO: Combine the two classes
    c1.update(class2)
    print(sum(c1.values()))

    c2.update(class1)
    print(sum(c2.values()))

    # TODO: What's the most common name in the two classes?
    print(c1.most_common(2))
    print(c2.most_common(2))

    # TODO: Separate the classes again
    c1.subtract(class2)
    print(c1.most_common(2))

    c2.subtract(class1)
    print(c2.most_common(2))

    # TODO: What's common between the two classes?
    print(c1 & c2)


if __name__ == "__main__":
    main()
