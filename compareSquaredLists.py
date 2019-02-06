# Given two arrays a and b write a function comp(a, b) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

# Examples
# Valid arrays
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]


def comp(array1, array2):
    is_same = True
    sorted_array_one = array1.sort()
    sorted_array_two = array2.sort()
    for i in sorted_array_one:
        if sorted_array_one[i] ** 2 != sorted_array_two[i]:
            is_same = False
            break
    return is_same

# tests

# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# print("test passed" if comp(a, b) else "test failed")
