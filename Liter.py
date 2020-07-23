from PlayAudio import playAudio
from Recognize import recognize
import re
import csv
from csv import writer


def identifyUnit(temp, qty):
    regex = re.compile("LITRES|LITRE|ML|MILI|LETTERS")
    print(temp)
    word = regex.findall(temp)
    if word == 'LETTERS':
        word='LITRES'

    print(qty, word)


def identifyQuantity(quantity):
    flg = None
    q = quantity.upper()
    temp = q
    if len(temp) != 0:
        x1 = temp.split()
        if len(x1) != 0:
            f1 = open('quantity.csv')
            csv_f1 = csv.reader(f1)
            qty = None

            for column in csv_f1:
                for y in x1:
                    y = y.capitalize()
                    if y == column[0]:
                        qty = y
                        flg = 1
                        break
                    else:
                        continue
    print('a')
    if flg == 1:
        identifyUnit(temp, qty)
    else:
        acceptQuantityLt()


def acceptQuantityLt():
    quantity = None
    playAudio('audiolit.wav')
    quantity = recognize()
    if quantity == "unknown error occured":
        acceptQuantityLt()
    else:
        print('lit call')
        identifyQuantity(quantity)
        print('lit after call')

