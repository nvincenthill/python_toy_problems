# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# string_ends_with('abc', 'bc') # returns true
# string_ends_with('abc', 'd') # returns false


def string_ends_with(string, ending):
    length = len(ending)
    sliced = string[len(string) - length:]
    return sliced == ending


# print(string_ends_with('abc', 'bc'))
