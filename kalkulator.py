from decimal import Decimal
import sys
import logging
from unicodedata import decimal
logging.basicConfig(level=logging.DEBUG)

print("Kalkulator")
result = None
math_op = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
if math_op == '1':
    arg1 = Decimal(input("Podaj składnik1:"))
    arg2 = Decimal(input("Podaj składnik2:"))
    logging.info("Dodajemy: %s i %s" % (arg1, arg2))
    result = (arg1 + arg2)
elif math_op == '2':
    arg1 = Decimal(input("Podaj składnik1:"))
    arg2 = Decimal(input("Podaj składnik2:"))
    logging.info("Odejmujemy: %s i %s" % (arg1 , arg2))
    result = (arg1 - arg2)
elif math_op == '3':
    arg1 = Decimal(input("Podaj składnik1:"))
    arg2 = Decimal(input("Podaj składnik2:"))
    logging.info("Mnożymy: %s i %s" % (arg1, arg2))
    result = (arg1 * arg2)
elif math_op == '4':
    arg1 = Decimal(input("Podaj składnik1:"))
    arg2 = Decimal(input("Podaj składnik2:"))
    logging.info("Dzielimy: %s i %s" % (arg1, arg2))
    result = (arg1 / arg2)
else:
    print("Nie ma takiego działania!")
    exit(1)
print("Wynik to: %s" % str(result))