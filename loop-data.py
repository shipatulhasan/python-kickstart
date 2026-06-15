dollar_prices = [1.50,4.99,10.00,25.55]
cents_price = []

#loop to add convert from dollar to cent
for price in dollar_prices:
  cents = int(price*100);
  cents_price.append(cents);
print (cents_price)

# single line code list comprehension.
centes_price = [int(price*100) for price in dollar_prices]
print (cents_price)