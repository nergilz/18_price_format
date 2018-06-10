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


def format_price(price):

    try:
        price = float(price)

    except ValueError:
        return None

    return '{:,}'.format(price).replace(',', ' ')


if __name__ == '__main__':

    argument = get_argument()
    print(format_price(argument.price))
