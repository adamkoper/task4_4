
import logging
logging.basicConfig(level=logging.INFO)

def calculator(operation):
    if operation == 1:
        logging.info(f"Dodaję {num1} i {num2}")
        result_1 = num1+num2
        print("Wynik to ", result_1)
    elif operation == 2:
        logging.info(f"Odejmuję {num1} i {num2}")
        result_2 = num1-num2
        print("Wynik to ", result_2)
    elif operation == 3:
        logging.info(f"Mnożę {num1} i {num2}")
        result_3 = num1*num2
        print("Wynik to ", result_3)
    elif operation == 4:
        logging.info(f"Dzielę {num1} i {num2}")
        result_4 = num1/num2
        print("Wynik to ", result_4)
    else:
        print("podana wartość nie jest liczbą od 1 do 4 ")


if __name__ == "__main__":
    operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    num1 = int(input("Podaj składnik 1. "))
    num2 = int(input("Podaj składnik 2. "))
    print(calculator(operation))







