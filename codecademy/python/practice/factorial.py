def factorial(x):
    product = 1
    for number in range(1, x + 1):
        product *= number
    return product