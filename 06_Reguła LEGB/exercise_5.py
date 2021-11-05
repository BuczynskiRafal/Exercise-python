def stock_info(company, country, price, currency):
    return f"Company: {company}\nCountry: {country}\nPrice: {currency} {price}"


print(stock_info.__code__.co_varnames)
