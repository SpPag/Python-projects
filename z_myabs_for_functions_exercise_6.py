def is_int(num):
    if num.count("+") > 1 or num.count("-") > 1:
        return False
    else:
        if num.lstrip("+").isdigit() or num.lstrip("-").isdigit():
            return True
        else:
            return False


def is_float(num):
    if "," in num:
        num = num.replace(",", ".")
    if num.count(".") > 1:
        return False
    elif num.count(".") == 1:
        if num.replace(".", "").lstrip("+").isdigit() or num.replace(".", "").lstrip("-").isdigit():
            return True
        else:
            return False


def abs(num):
    if is_int(num):
        num = int(num)
    elif is_float(num):
        num = float(num)
    if type(num) is int or type(num) is float:
        if num < 0:
            return -num
        if num >= 0:
            return num