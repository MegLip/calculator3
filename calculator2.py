import sys                                                      #1 def function
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator1(choice, num1, num2, *args):
    if int(choice) == 1:
        result = float(num1) + float(num2) + float(sum(args))
    elif int(choice) == 3:
        x = 1
        for num in args:
            x = x * float(num)
            y = x * float(num1) * float(num2)
        result = (float(y)) 
    return result

def calculator2(choice, num1, num2):
    if int(choice) == 2:
        result = round(float(num1) - float(num2),2) 
    elif int(choice) == 4:
        result = round(float(num1)/float(num2),2)
    return result

choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")         #2 choice operation
if choice not in ("1","2","3","4"):
    logging.info("Niepoprawna wartość! Spróbuj raz jeszcze")
    exit(1)
num1 = float(input("Podaj liczbę nr 1: "))
num2 = float(input("Podaj liczbę nr 2: "))

