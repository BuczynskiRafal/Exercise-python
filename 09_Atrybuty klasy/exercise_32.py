class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


# print(f"sector -> {OnlineShop.sector}")
# print(f"sector_code -> {OnlineShop.sector_code}")
# print(f"is_public_company -> {OnlineShop.is_public_company}")

for attr, value in OnlineShop.__dict__.items():
    if not attr.startswith('_'):
        print(f"{attr} -> {value}")