# customize string representations of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == 'rgb':
            return self.red, self.green, self.blue
        elif attr == 'hex':
            return f'#{self.red:02x}{self.green:02x}{self.blue:02x}'
        else:
            raise AttributeError

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == 'rgb':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # TODO: use dir to list the available properties
    def __dir__(self):
        return 'red', 'blue', 'green', 'rgb', 'hex'


def main():
    # create an instance of myColor
    cls1 = myColor()
    # TODO: print the value of a computed attribute
    print(cls1.rgb)
    print(cls1.hex)

    # TODO: set the value of a computed attribute
    cls1.rgb = (3, 33, 2)
    print(cls1.rgb)
    print(cls1.hex)

    cls1.red = 50
    cls1.blue = 50
    cls1.green = 50

    # TODO: access a regular attribute
    print(cls1.red, cls1.blue, cls1.green)

    # TODO: list the available attributes
    print(dir(cls1))


if __name__ == "__main__":
    main()
