import sys
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