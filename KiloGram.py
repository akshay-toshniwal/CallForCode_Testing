from PlayAudio import playAudio
from Recognize import recognize
import re
import csv
from csv import writer


def identifyUnit(prd,qty,temp):
    regex = re.compile("KG|KGS|KILOGRAMS|GRAMS|GRAM|Pound|KILOGRAM|GM")
    word = regex.findall(temp)
    lst=[]
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

    if flg==1:
        identifyUnit(prd,qty,temp)
    else:
        acceptQuantityKg(prd)

def acceptQuantityKg(prd):
    quantity=None
    playAudio('audiokg.wav')
    quantity=recognize()
    print(quantity)
    if quantity=="unknown error occured":
         acceptQuantityKg(prd)
    else:
        print('kg call')
        identifyQuantity(quantity,prd)
        print('kg after call')

