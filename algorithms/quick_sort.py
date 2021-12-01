from typing import Iterable

def divide(iterable: Iterable, left: int, right: int):
	pivot = iterable[right]
	item = left - 1
	for i in range(left, right):
		if iterable[i] <= pivot:
			item = item + 1
			iterable[item], iterable[i] = iterable[i], iterable[item]

	iterable[item + 1], iterable[right] = iterable[right], iterable[item + 1]

	return item + 1

def quick_sort(iterable: Iterable, left: int, right: int):
    if left < right:
        middle_index = divide(iterable, left, right)
        quick_sort(iterable, left, middle_index - 1)
        quick_sort(iterable, middle_index + 1, right)
    