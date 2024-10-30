def max_num(num1, num2, num3):
    result = max(num1, num2, num3)
    return result


print(max_num(12, 43, 108))
# another way to do this would be using an if statement. Let's do that, just for practice. Also for practice's sake
# let's look for the smallest number, not the biggest.


def min_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3


print(min_num(12, 43, 108))
