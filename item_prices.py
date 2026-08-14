prices = (100, 250, 150, 500, 200)

total = sum(prices)
average = total / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

print("Total Bill =", total)
print("Average Price =", average)
print("Highest Price =", highest)
print("Lowest Price =", lowest)
