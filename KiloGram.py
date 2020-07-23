from PlayAudio import playAudio
from Recognize import recognize
import re
import csv
from csv import writer


def identifyUnit(temp,qty):
    regex = re.compile("KG|KGS|KILOGRAMS|GRAMS|GRAM|Pound|KILOGRAM|GM")
    print(temp)
    word = regex.findall(temp)
    print(qty, word)
    


def identifyQuantity(quantity):
    flg = None
    q=quantity.upper()
    temp = q
    if len(temp) != 0:
        x1 = temp.split()
        if len(x1) != 0:
            f1  = open('quantity.csv')
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
    if flg==1:
        identifyUnit(temp,qty)
    else:
        acceptQuantityKg()
    print(flg,temp)

def acceptQuantityKg():
    quantity=None
    playAudio('audiokg.wav')
    quantity=recognize()
    if quantity=="unknown error occured":
         acceptQuantityKg()
    print('call')
    identifyQuantity(quantity)
    print('after call')

