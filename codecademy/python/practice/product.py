def product(numbers):
    product = 1
    for i in range(len(numbers)):
        product *= numbers[i]
    return product