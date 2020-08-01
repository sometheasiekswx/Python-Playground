# define enumerations using the Enum base class

from enum import Enum, unique, auto


@unique
class FruitsUnique(Enum):
    APPLE = 1
    APPLE_PIE = 1.1
    ORANGE = 2
    ORANGE_JUICE = 2.1
    GRAPE = 3
    MANGO = 4


class Fruits(Enum):
    APPLE = 1
    APPLE_PIE = APPLE
    ORANGE = 2
    ORANGE_JUICE = ORANGE
    GRAPE = 3
    MANGO = 4
    PEAR = auto()
    BANANA = auto()
    JOHN = auto()


def main():
    # TODO: enums have human-readable values and types
    print(Fruits.APPLE)
    print(type(Fruits.APPLE))
    print(repr(Fruits.APPLE))

    # TODO: enums have name and value properties
    print(f'{Fruits.APPLE.name} = {Fruits.APPLE.value}')
    print(f'{Fruits.ORANGE_JUICE.name} = {Fruits.ORANGE_JUICE.value}')

    # TODO: print the auto-generated value
    print(f'{Fruits.JOHN.name} = {Fruits.JOHN.value}')

    # TODO: enums are hashable - can be used as keys
    bought = {FruitsUnique.APPLE: 345}
    print(bought)
    bought[FruitsUnique.APPLE_PIE] = 50
    print(bought)
    print(bought[FruitsUnique.APPLE_PIE])


if __name__ == "__main__":
    main()
