class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


def describe_attrs():
    for attr, value in OnlineShop.__dict__.items():
        if not attr.startswith('__'):
            print(f"{attr} -> {value}")

describe_attrs()