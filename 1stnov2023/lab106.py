products = [
    {"name": "laptop", "price": 1000},
    {"name": "smartphone", "price": 500},
    {"name": "headphone", "price": 100},
    {"name": "tablet", "price": 300},
]

print(type(products))
print(type(products[0]))


def is_affordable(atul):
    return atul["price"] < 500


def is_affordable_name(atul):
    return len(atul["name"]) > 6

affordable_item_price = list(filter(is_affordable,products))
affordable_item_name = list(filter(is_affordable_name,products))
for i in affordable_item_price:
    print(i["price"],i["name"])

for i in affordable_item_name:
    print(i["price"],i["name"])

    i = 10
    name = "atul"
    print(i)
    print(name)
    print(name+str(i))
    #print(int(name)+i)