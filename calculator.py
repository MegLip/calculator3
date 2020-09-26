import logging

def add (num1, num2):                         #1 def function
    return num1 + num2
def add (num1, num2, *args):               
    return num1 + num2 + sum(args)  
def substract (num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
def multiply (num1, num2, *args):
    x = 1
    for num in args:
        x *= num
        y = x * num2 * num1
    return(y)
def divide (num1, num2):
    return num1/num2

if __name__ == "__main__":
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")        #2 choice operation
    choice = input("Podaj numer działania (1,2,3,4): ")
    if choice in ('2','4'):
        num1 = float(input ("Podaj liczbę nr 1: "))
        num2 = float(input ("Podaj liczbę nr 2: "))
        print(f"Sprawdzam, czy podane wartości są liczbami:", {type(num1)}, {type(num2)})
        if choice == '2':
            logging.info(f"Odejmuję {num1} i {num2}")
            print(f"Odejmuję", num1, "i", num2)
            print(f"Wynik odejmowania to:", substract(num1, num2))
        elif choice == '4':
            logging.info(f"Dzielę {num1} i {num2}")        
            print(f"Dzielę", num1, "i", num2)
            print(f"Wynik dzielenia to:", (round(divide(num1,num2),2)))
   
    elif choice in ('1','3'):
        num1 = float(input ("Podaj liczbę nr 1: "))
        num2 = float(input ("Podaj liczbę nr 2: "))
        print("Podaj następne argumenty lub wciśnij k by zakończyć")
        args = []
        while True:
            arg = input("Podaj kolejną liczbę lub k: ")                            #3 give more than 2 arguments
            if arg == "k":
                break
            args.append(float(arg))

        if choice == "1":
            #x = 0
            #for num in args:
           #     x += float(num)
           #     y = x + num1 + num2 
            result = add(num1, num2, *args) 
            print(f"Sprawdzam, czy podane wartości są liczbami:", {type(num1)}, {type(num2)}, {type(args)})       
            logging.info(f"Dodaję {num1} i {num2} i {sum(args)}")
            print(f"Dodaję", num1, "i", num2, "i", float(sum(args)))
            print("Wynik dodawania to:", add(num1, num2, sum(args)))

        elif choice == "3":
            x = 1
            for num in args:
                x = x * float(num)
                y = x * num2 * num1

            result = multiply(num1, num2, y)
            print(f"Sprawdzam, czy podane wartości są liczbami:", {type(num1)}, {type(num2)}, {type(y)})        
            logging.info(f"Mnożę {num1} i {num2} i {x}")
            print(f"Mnożę", num1, "i", num2, "i", (x))
            print(f"Wynik mnożenia to:", y)    
    else:
        print ("Niepoprawna wartość! Spróbuj raz jeszcze")
