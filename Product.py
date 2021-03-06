import csv
import random

from KiloGram import acceptQuantityKg
from Liter import acceptQuantityLt
from Pieces import acceptQuantityPc
from PlayAudio import playAudio

number = (random.randint(8888888888, 9999999999))
def identifyProduct(translatedText):
    finalProduct = str(number)
    flg = None
    product = translatedText.upper()
    temp = product
    if len(temp) != 0:
        x1 = temp.split()
        if len(x1) != 0:
            f1 = open('productkg.csv')
            csv_f1 = csv.reader(f1)
            prd = None
            for column in csv_f1:
                for y in x1:
                    y = y.capitalize()
                    if y == column[0]:
                        prd = y
                        flg = 1
                        finalProduct = finalProduct + "" + prd

            f1 = open('productlit.csv')
            csv_f1 = csv.reader(f1)
            if flg == None:
                for column in csv_f1:
                    for y in x1:
                        y = y.capitalize()
                        if y == column[0]:
                            prd = y
                            flg = 2
                            finalProduct = finalProduct + "" + prd
            f1 = open('productpc.csv')
            csv_f1 = csv.reader(f1)
            if flg == None:
                for column in csv_f1:
                    for y in x1:
                        y = y.capitalize()
                        if y == column[0]:
                            prd = y
                            flg = 3
                            finalProduct = finalProduct + "" + prd

    if (flg == 1):
        acceptQuantityKg(finalProduct)

    elif (flg == 2):
        acceptQuantityLt(finalProduct)

    elif (flg == 3):
        acceptQuantityPc(finalProduct)
    else:
        playAudio("notinlist.wav")
        import onlineOrder
        onlineOrder.orderStart(1)
