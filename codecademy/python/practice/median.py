def median(numbers):
    new_list = sorted(numbers)
    half = len(new_list) / 2
    if len(new_list) % 2 == 0:
        median = (new_list[half - 1] + new_list[half]) / 2.0
    elif len(new_list) == 1:
        median = new_list[0]
    else:
        median = new_list[half]
    return median