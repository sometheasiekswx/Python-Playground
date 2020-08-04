# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from

CURRENT_USER = {
    'user': 'sometheasiek123',
    'ip': '12.213.123.124'
}


def anotherFunction():
    logging.warning('This is a warning!!!', extra=CURRENT_USER)


def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    logging_format = '%(asctime)s | %(levelname)s | %(funcName)s() | Line %(lineno)d | %(user)s | %(ip)s | %(message)s'
    datefmt = '%d/%m/%Y %I:%M:%S %p'
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode='a',
                        format=logging_format,
                        datefmt=datefmt)

    logging.info("This is an info-level log message", extra=CURRENT_USER)
    logging.warning("This is a warning-level message", extra=CURRENT_USER)
    anotherFunction()


if __name__ == "__main__":
    main()
