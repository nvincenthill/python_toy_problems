import re


def validate_pin(pin):
    return True if re.match(r"^\d{4}$|^\d{6}$", pin) is not None else False

# tests


# print(validate_pin('4235') == True)
# print(validate_pin('242492') == True)
# print(validate_pin('22') == False)
# print(validate_pin('adb4') == False)
