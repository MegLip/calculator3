import logging
logging.basicConfig(level=logging.DEBUG)


def add(num1, num2, *args):      # 1 def function
    return num1 + num2 + sum(args)


def substract(num1, num2):
    return num1 - num2


def multiply(num1, num2, *args):
    x = 1
    for num in args:
        x *= num
        y = x * num2 * num1
    return(y)


def divide(num1, num2):
    return num1/num2


# 2 choice of operation
operations = {1: add, 2: substract, 3: multiply, 4: divide}
action = {1: "dodawanie", 2: "odejmowanie", 3: "mnożenie", 4: "dzielenie"}

