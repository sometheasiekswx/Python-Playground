from fractions import Fraction


def proper_fraction(dec):
    sign = '-' if dec < 0 else ''
    frac = Fraction(abs(dec)).limit_denominator()

    whole = frac.numerator // frac.denominator
    numerator = frac.numerator % frac.denominator
    denominator = frac.denominator

    if whole == 0:
        return (f'{sign} {numerator}/{denominator}')
    if numerator == 0:
        return (f'{sign}{whole}')

    return (f'{sign}{whole} {numerator}/{denominator}')


if __name__ == "__main__":
    whole_measurements = [1, 5, 2, 1, 4, 1, 4]
    one_third_measurements = [proper_fraction(i/3) for i in whole_measurements]
    print(one_third_measurements)
