def enter_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            return amount

        except ValueError:
            print("Invalid input. Please enter a valid amount.")


def currency(label):
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        try:
            currency = input(f"{label} (USD/EUR/CAD)").upper()
            if currency not in currencies:
                raise ValueError()
            return currency
        except:
            print("Invalid currency input. Please enter a valid currency.")


def calculate_amount(source_currency, target_currency, amount):
    exchange_rates = {
        'USD': {'CAD': 1.50, 'EUR': 1.33},
        'CAD': {'USD': 0.95, 'EUR': 1.10},
        'EUR': {'USD': 0.91, 'CAD': 0.98}
    }

    if source_currency == target_currency:
        return amount

    return amount * (exchange_rates[source_currency])[target_currency]


def calculate_amount_all_currencies(source_currency, amount):
    exchange_rates = {
        'USD': {'CAD': 1.50, 'EUR': 1.33},
        'CAD': {'USD': 0.95, 'EUR': 1.10},
        'EUR': {'USD': 0.91, 'CAD': 0.98}
    }

    for currency, rate in exchange_rates[source_currency].items():
        conversion_amount = amount * rate
        print(f"{amount:.2f} {source_currency} is equal to {
            conversion_amount:.2f} {currency}")


def main():

    exchanges_made = []

    while True:
        amount = enter_amount()
        source_currency = currency("Source currency")
        calculate_amount_all_currencies(source_currency, amount)
        target_currency = currency("Target currency")
        conversion_amount = calculate_amount(
            source_currency, target_currency, amount)
        exchanges = f"{amount:.2f} {
            source_currency} is equal to {conversion_amount:.2f}"
        exchanges_made.append(exchanges)
        print(exchanges)
        wants_to_continue = input("Do you want to continue? (y/n)").lower()
        if wants_to_continue == 'n':
            print("Conversions made during this session")
            for exchange in exchanges_made:
                print(exchange)
            break


if __name__ == "__main__":
    main()
