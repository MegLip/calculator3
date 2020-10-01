import logging
logging.basicConfig(level=logging.DEBUG)


# 1 def function
def add(num1, num2, *args):
    return num1 + num2 + sum(args)


def substract(num1, num2, *args):
    return num1 - num2


def multiply(num1, num2, *args):
    x = 1
    for num in args:
        x *= num
        y = x * num2 * num1
    return(y)


def divide(num1, num2, *args):
    return num1/num2


# 2 choice of operation
action = {1: "dodawanie", 2: "odejmowanie", 3: "mnożenie", 4: "dzielenie"}


# 3 give arguments and run calculator
def get_data(op):
    num1 = float(input("Podaj składnik nr 1: "))
    num2 = float(input("Podaj składnik nr 2: "))
    args = []
    if op in (1, 3):
        while True:
            arg = input("Podaj liczbę lub k by zakończyć: ")
            if arg == "k":
                break
            args.append(float(arg))
        return num1, num2, args
    elif op in (2, 4):
        return num1, num2, args
    else:
        if op != (1, 2, 3, 4):
            print("Niepoprawna wartość! Wybierz działanie spośród 1,2,3,4")
    return result


operations = {1: add, 2: substract, 3: multiply, 4: divide}


if __name__ == "__main__":
    op = int(input("Podaj działanie, posługując się odpowiednią liczbą:\
                  \n1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    num1, num2, args = get_data(op)
    logging.info(f"Wykonuję działanie: {action[op]},\
        \ndla następujących liczb: {num1} i {num2} i {args}")
    result = operations[op](num1, num2, *args)
    logging.info(f"Wynik to: {round((result),2)}")
