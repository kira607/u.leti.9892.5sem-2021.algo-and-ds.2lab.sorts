def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        j = i - 1
        while j >= 0 and current_value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_value
