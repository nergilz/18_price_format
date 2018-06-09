import argparse


def get_argument():

    parser = argparse.ArgumentParser(
        description='Breaks the price into categories'
        )
    parser.add_argument(
        'price',
        help='Price for breakdown'
        )
    return parser.parse_args()


def check_argument(price):

    try:
        return str(float(price))

    except ValueError:
        return None


def format_price(price):

    price = price.split('.')
    int_part_of_number = price[0]
    fraction_of_the_number = price[1]

    int_part_of_number = [number for number in int_part_of_number]
    int_part_of_number.reverse()

    for number in range(3, len(int_part_of_number)+5, 4):
        int_part_of_number.insert(number, ' ')
    int_part_of_number.reverse()

    return ''.join(int_part_of_number).strip(), fraction_of_the_number


def main(price):

    price = check_argument(price)

    if price is not None:

        digids_of_number = format_price(price)
        return '.'.join(digids_of_number)

    else:
        return None


if __name__ == '__main__':

    argument = get_argument()

    digits_of_number = main(argument.price)
    print(digits_of_number)
