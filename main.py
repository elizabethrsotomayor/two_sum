def two_sum(numbers: list, target: int) -> list:
    """
    A function that takes an array of numbers and a target number. It finds two different items in
    the array that, when added together, give the target value.
    :param numbers: list of three values
    :param target: value to be obtained from adding two items in the list
    :return: list of indices from numbers list
    """
    lst = []
    prev = 0
    is_iterating = True

    while is_iterating:
        for i in range(1, len(numbers)):
            if numbers[prev] + numbers[i] == target:
                lst.append(prev)
                lst.append(i)
                is_iterating = False
        prev += 1

    return lst
