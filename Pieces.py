from PlayAudio import playAudio
from Recognize import recognize
import re
import csv
from csv import writer


def identifyUnit(temp, qty,prd):
    regex = re.compile("PIECE|PIECES")
    print(temp)
    word = regex.findall(temp)
    print(qty, word)
    lst = []
    lst.append(prd)
    lst.append(qty)
    lst.extend(word)
    with open("record.csv", 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(lst)


def identifyQuantity(quantity,prd):
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

    if flg == 1:
        identifyUnit(temp, qty,prd)
    else:
        acceptQuantityPc(prd)


def acceptQuantityPc(prd):
    quantity = None
    playAudio('audiopc.wav')
    quantity = recognize()
    print(quantity)
    if quantity == "unknown error occured":
        acceptQuantityPc(prd)
    else:

        identifyQuantity(quantity,prd)


