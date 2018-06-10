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


def check_type(price):

    if isinstance(price, str) or isinstance(price, int) or isinstance(price, float):
        return price

    else:
        return None


def format_price(price):

    if check_type(price):
        try:
            price = round(float(price), 4)

        except ValueError:
            return None

        return '{:,}'.format(price).replace(',', ' ')

    else:
        return None


if __name__ == '__main__':

    argument = get_argument()
    print(format_price(argument.price))
