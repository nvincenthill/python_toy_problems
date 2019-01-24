# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

# NOTE: All numbers will be whole numbers greater than 0.


def expanded_form(num):
    stringified = str(num)
    length_of_string = len(stringified)
    # base case
    if len(stringified) == 1:
        return stringified
    # recursive case
    else:
        base = int(round(num, (length_of_string - 1) * -1))
        return str(base) + " + " + expanded_form(num - base)


print(expanded_form(3) == '3')
print(expanded_form(12) == '10 + 2')
print(expanded_form(42) == '40 + 2')
print(expanded_form(70304) == '70000 + 300 + 4')
