# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple('Point', 'x y z')
    p1 = Point(1, 3, 3)
    p2 = Point(5, 2, -1)
    print(p1, p2)
    print(p1.x, p2.y, p1.z)

    # TODO: use _replace to create a new instance
    p1 = p1._replace(y=300, z=-200)
    print(p1)


if __name__ == "__main__":
    main()
