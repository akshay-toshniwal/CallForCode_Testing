from PlayAudio import playAudio
from Recognize import recognize
import re
import csv
from csv import writer


def identifyUnit(temp, qty):
    regex = re.compile("PIECE|PIECES")
    print(temp)
    word = regex.findall(temp)
    print(qty, word)


def identifyQuantity(quantity):
    flg = None
    q = quantity.upper()
    temp = q
    print(temp)
    if len(temp) != 0:
        x1 = temp.split()
        print(x1)
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
    print('a')
    if flg == 1:
        identifyUnit(temp, qty)
    else:
        acceptQuantityPc()


def acceptQuantityPc():
    quantity = None
    playAudio('audiopc.wav')
    quantity = recognize()
    print(quantity)
    if quantity == "unknown error occured":
        acceptQuantityPc()
    else:
        print('pc call')
        identifyQuantity(quantity)
        print('pc after call')

