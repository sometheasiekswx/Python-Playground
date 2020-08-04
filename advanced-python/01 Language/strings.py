# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values


def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    # TODO: Try combining them.
    # does not work
    # print(b + s)
    # works (maybe not best)
    print(str(b) + s)

    # TODO: Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    b2 = b.decode('utf-8')
    print(type(b2))
    print(b2 + s)

    s2 = s.encode('utf-8')
    print(type(s2))
    print(b + s2)

    # TODO: encode the string as UTF-32
    s3 = s.encode('utf-32')
    print(s3)


if __name__ == "__main__":
    main()
