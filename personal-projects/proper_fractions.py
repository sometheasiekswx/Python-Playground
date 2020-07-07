from fractions import Fraction
import sys


def get_measurement_number(ingredient):
    '''
    Return number from ingredient. 
        get_measurement_number('1T Korean Chilli Paste') returns 1
    '''

    num = ingredient.split(' ')[0].replace('T', '').replace('t', '')

    return int(num), ingredient.replace(num, '', 1)


def proper_fraction(num):
    '''
    Convert a number to a proper fraction.
    '''

    sign = '-' if num < 0 else ''
    fraction = Fraction(abs(num)).limit_denominator()
    whole = fraction.numerator // fraction.denominator
    new_numerator = fraction.numerator % fraction.denominator
    new_denominator = fraction.denominator

    if whole is 0:
        return f'{sign}{new_numerator}/{new_denominator}'
    if new_numerator is 0:
        return f'{sign}{whole}'

    return f'{sign}{whole} {new_numerator}/{new_denominator}'


if __name__ == "__main__":
    # 1T Korean Chilli Paste
    # 5T Ketchup
    # 2T Soy sauce
    # 1T Pepper Flakes
    # 4T Sugar
    # 1T Minced Garlic
    # 4T Starch Sirup

    ingredients = ['1T Korean Chilli Paste', '5T Ketchup', '2T Soy sauce',
                   '1T Pepper Flakes', '4T Sugar', '1T Minced Garlic', '4T Starch Sirup']

    whole_measurements = []
    measurements_text = []
    for ingredient in ingredients:
        num, text = get_measurement_number(ingredient)
        whole_measurements.append(num)
        measurements_text.append(text)

    try:
        divide_by = int(sys.argv[1])
    except IndexError:
        divide_by = 3

    new_measurements = [proper_fraction(i/divide_by)
                        for i in whole_measurements]

    for num, text in zip(new_measurements, measurements_text):
        print(f'{num}{text}')
