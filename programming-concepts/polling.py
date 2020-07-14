from time import sleep


def poll():
    while(True):
        polling_file = open('polling.txt', 'r')
        if 'stop' in polling_file:
            print('Stop polling')
            break
        else:
            print('Keep polling')

        polling_file.close()

        sleep(1)


def main():
    poll()


if __name__ == "__main__":
    main()
