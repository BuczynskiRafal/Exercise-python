def display_info(company, **kwargs):
    if 'price' in kwargs:
        print(f"Company name: {company}")
        print(f"Price: {kwargs['price']}")
    else:
        print(f"Company name: {company}")


display_info(company='CD Projekt', price=100)