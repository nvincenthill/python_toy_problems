# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.


def remove_smallest(numbers):
    return sorted(numbers[:])[1:]


# tests
# print(remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5])
