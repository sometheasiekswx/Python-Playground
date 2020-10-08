import sys
from fractions import Fraction


def get_new_measurements(old_measurement, has_fraction=False, multiplier=1):
    """
    Return number from ingredient.
        get_measurement_number('1T Korean Chili Paste') returns 1
    """

    new_measurement = old_measurement.split(' ')[0].replace('T', '').replace('t', '')
    text = old_measurement.replace(new_measurement, '', 1)

    if not has_fraction:
        number = int(new_measurement) * multiplier
    elif has_fraction:
        measurements = new_measurement.split('+')
        if len(measurements) == 1:
            number = Fraction(new_measurement)
        else:
            number = Fraction(0)
            for fraction_measurement in measurements:
                number += Fraction(fraction_measurement)
        number = int(float(number) * multiplier)

    return number, text


def get_proper_fraction(decimal):
    """
    Convert a number to a proper fraction.
    """

    sign = '-' if decimal < 0 else ''
    fraction = Fraction(abs(decimal)).limit_denominator()
    whole = fraction.numerator // fraction.denominator
    new_numerator = fraction.numerator % fraction.denominator
    new_denominator = fraction.denominator

    if whole is 0:
        return f'{sign}{new_numerator}/{new_denominator}'
    if new_numerator is 0:
        return f'{sign}{whole}'

    return f'{sign}{whole} {new_numerator}/{new_denominator}'


if __name__ == "__main__":
    # # Korean Chili Sauce
    # ingredients = ['1T Korean Chili Paste', '5T Ketchup', '2T Soy sauce',
    #                '1T Pepper Flakes', '4T Sugar', '1T Minced Garlic', '4T Starch Syrup']

    # 8 Buffalo Chicken Wings Sauce
    original_ingredients = ['2T hot sauce', '1+1/2T butter', '1/2t distilled vinegar']
    ingredients = []
    multiplier_for_ingredients = 2
    for ingredient in original_ingredients:
        measurement, measurement_description = get_new_measurements(ingredient, has_fraction=True, multiplier=multiplier_for_ingredients)
        ingredients.append(f'{measurement}{measurement_description}')
    other_ingredients = ['Optional: brown sugar (to taste) ', 'Optional: salt (to taste)']

    whole_measurements = []
    measurements_descriptions = []
    for ingredient in ingredients:
        whole_measurement, measurement_description = get_new_measurements(ingredient)
        whole_measurements.append(whole_measurement)
        measurements_descriptions.append(measurement_description)

    try:
        divisor = int(sys.argv[1])
    except IndexError:
        print('Divisor entered is not a whole number. Using default divisor of 3.')
        divisor = 3
    divisor = divisor * multiplier_for_ingredients

    proper_fractions_measurements = [get_proper_fraction(i / divisor) for i in whole_measurements]

    for number, text in zip(proper_fractions_measurements, measurements_descriptions):
        print(f'{number}{text}')

    for ingredient in other_ingredients:
        print(ingredient)
