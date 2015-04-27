products = set()
pandigital = "123456789"

for i in range(10000):
    for j in range(10000):
        product = i * j
        s = "".join(sorted(str(i) + str(j) + str(product)))
        if s == pandigital:
            products.add(product)
            print product

print sum(products)