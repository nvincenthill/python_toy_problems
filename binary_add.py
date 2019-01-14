# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.


def add_binary(a, b):
    x = format(a, "b")
    y = format(b, "b")
    max_len = max(len(x), len(y))

    x = x.zfill(max_len)
    y = y.zfill(max_len)

    # initialize the result
    result = ''

    # initialize the carry
    carry = 0

    # traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1     # compute the carry

    if carry != 0:
        result = '1' + result

    return result.zfill(max_len)

# tests

# print(add_binary(1, 1) == "10")
# print(add_binary(0, 1) == "1")
# print(add_binary(1, 0) == "1")
# print(add_binary(2, 2) == "100")
# print(add_binary(51, 12) == "111111")
