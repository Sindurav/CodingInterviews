import sys


def solution(actual_price, given_price):
    if given_price < actual_price:
        print("ERROR")
        return
    elif given_price == actual_price:
        print("ZERO")
        return
    else:
        price_to_return = given_price - actual_price
        results = set([])

        for value in values:
            while price_to_return >= value:
                results.add(value)
                price_to_return = price_to_return - value

        results = list(results)
        results = [name2value[result] for result in results]

        results = sorted(results)
        print(",".join(results))
        return


name2value = {.01: 'PENNY', .05: 'NICKEL', .10: 'DIME', .25: 'QUARTER', .50: 'HALF DOLLAR', 1.00: 'ONE', 2.00: 'TWO',
              5.00: 'FIVE', 10.00: 'TEN', 20.00: 'TWENTY', 50.00: 'FIFTY'}

values = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

for line in sys.stdin:
    purchase_price, cash = line.split(";")
    purchase_price, cash = float(purchase_price), float(cash)
    solution(purchase_price, cash)
