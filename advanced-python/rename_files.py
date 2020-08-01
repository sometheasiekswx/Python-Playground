import os
from re import split


def main():
    for directories in list(os.walk(os.getcwd()))[1:]:
        folder = directories[0]
        files = directories[2]
        for file in files:
            original_path = f'{folder}/{file}'
            filenames = split('_|.py', file)
            if 'finished' in filenames or 'start' in filenames:
                new_path = original_path.replace('_finished', '').replace('_start', '')
                os.rename(original_path, new_path)


if __name__ == '__main__':
    main()
