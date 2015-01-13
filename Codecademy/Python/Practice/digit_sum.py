def digit_sum(n):
    sum = 0
    for digits in range(len(str(n))):
        sum += n % 10
        n /= 10
    return sum