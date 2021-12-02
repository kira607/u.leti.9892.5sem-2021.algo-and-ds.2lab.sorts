def count_sort(array, min_value=None, max_value=None):
    min_value = min(array) if min_value is None else min_value
    max_value = max(array) if max_value is None else max_value
    if min(array) < min_value or max(array) > max_value:
        raise ValueError(f'Array contains elements that either > {max_value} or < {min_value}')
    count_array = [0 for _ in range(min_value, max_value + 1)]
    for value in array:
        index = value - min_value
        count_array[index] += 1
    result = []
    for index, value in enumerate(count_array, min_value):
        result.extend([index for _ in range(value)])
    return result
