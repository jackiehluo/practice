def remove_duplicates(numbers):
    new_list = []
    for i in range(len(numbers)):
        if numbers[i] not in new_list:
            new_list.append(numbers[i])
    return new_list