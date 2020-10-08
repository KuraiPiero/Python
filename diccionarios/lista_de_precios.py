def add_prices(basket):
    total = 0
    for item in basket:
        total += basket[item]
        
    return "{:.2f}".format(total)


add_prices(
    {
        "bananas": 1.56,
        "apples": 2.50,
        "oranges": 0.99,
        "bread": 4.59,
        "coffee": 6.99,
        "milk": 3.39,
        "eggs": 2.98,
        "cheese": 5.44,
    }
)  # Should print 28.44

