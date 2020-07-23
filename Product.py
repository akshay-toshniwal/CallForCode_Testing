import csv
from csv import writer

from PlayAudio import playAudio
from KiloGram import acceptQuantityKg
from Liter import acceptQuantityLt
from Pieces import acceptQuantityPc



def identifyProduct(translatedText):
    flg = None
    finalProduct=""

    product=translatedText.upper()
    temp = product
    print(temp)
    if len(temp) != 0:
        x1 = temp.split()
        if len(x1) != 0:
            f1  = open('productkg.csv')
            csv_f1 = csv.reader(f1)
            prd = None
            for column in csv_f1:
                for y in x1:
                    y = y.capitalize()
                    if y == column[0]:
                        prd = y
                        flg = 1
                        finalProduct=finalProduct+""+prd

            f1 = open('productlit.csv')
            csv_f1 = csv.reader(f1)
            if flg == None:
                for column in csv_f1:
                    for y in x1:
                        y = y.capitalize()
                        if y == column[0]:
                            prd = y
                            flg = 2
                            finalProduct=finalProduct+""+prd
            f1 = open('productpc.csv')
            csv_f1 = csv.reader(f1)
            if flg == None:
                for column in csv_f1:
                    for y in x1:
                        y = y.capitalize()
                        if y == column[0]:
                            prd = y
                            flg = 3
                            finalProduct=finalProduct+""+prd

    if (flg==1):
        acceptQuantityKg()
        
    elif(flg==2):
        acceptQuantityLt()

    elif(flg==3):
        acceptQuantityPc()
    else:
        import onlineOrder
        onlineOrder.orderStart()

