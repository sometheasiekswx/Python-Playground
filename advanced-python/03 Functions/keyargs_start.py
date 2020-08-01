# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def my_function(arg1, arg2, *, suppress_life=False):
    return arg1 * arg2 * suppress_life


def main():
    # try to call the function without the keyword
    # myFunction(1, 2, True)  # Does not work
    my_function(1, 2, suppress_life=True)


if __name__ == "__main__":
    main()
