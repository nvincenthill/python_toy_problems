# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

# NOTE: All numbers will be whole numbers greater than 0.


def round_down(num, divisor):
    return num - (num % divisor)


def expanded_form(num):
    stringified = str(num)
    result = ''

    while True:
        stringified = str(num)
        if len(stringified) == 1:
            return result + str(num)
        else:
            base = int(round_down(num, 10 ** (len(stringified) - 1)))
            result = result + str(base) + " + "
            num = num - base


print(expanded_form(3) == '3')
print(expanded_form(12) == '10 + 2')
print(expanded_form(42) == '40 + 2')
print(expanded_form(70304) == '70000 + 300 + 4')
# print(expanded_form(4982342))
