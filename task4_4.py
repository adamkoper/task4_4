import sys
import logging

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
num1 = input("Podaj składnik 1. ")
num2 = input("Podaj składnik 2. ")

def calculator(operation):
    if operation == 1:
        return logging.info("Dodaję ", num1, "i ", num2)
        result_1 = num1+num2
        return "Wynik to ", result_1
    elif operation == 2:
        return logging.info("Odejmuję ", num1, "i ", num2)
        result_2 = num1-num2
        return "Wynik to ", result_2
    elif operation == 3:
        return logging.info("Mnożę ", num1, "i ", num2)
        result_3 = num1*num2
        return "Wynik to ", result_3
    elif operation == 4:
        return logging.info("Dzielę", num1, "i ", num2)
        result_4 = num1/num2
        return "Wynik to ", result_4
    else:
        return "podana wartość nie jest liczbą od 1 do 4 "


print(calculator(operation))







