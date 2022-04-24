items = [
    ("prod1", 2),
    ("prod2", 109),
    ("prod3", 76),
]


# python doesn't know how to sort this list of objects, we have to define it.


# use lambda as an anonnymous function for shorter and cleaner way
# order items by price
items.sort(key=lambda item: item[1])

print(items)
