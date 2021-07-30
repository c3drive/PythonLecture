# reStructuredText
def multiply(num1, num2):
    """
    muliply num1 with num2 and return the result
    :param num1: first number that you want to multiply
    :param num2: second number that you want to multiply
    :return: num1 * num2
    """
    return num1 * num2

# def定義していない場合、importされた時、実行されてしまう
#print(multiply.__doc__)
#help(multiply)

# Google style
def dividend(num1, num2):
    """
    num1 is divided by num2 and return the result
    Args:
        num1: number that you want to divide
        num2: number that num1 is divided by

    Returns:
        num1 / num2

    """
    return num1 / num2

#dividend(1, 4)