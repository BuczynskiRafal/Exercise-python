class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False

OnlineShop.country = 'Poland'

attrs = [attr for attr in OnlineShop.__dict__.keys() if not attr.startswith('_')]
print(attrs)