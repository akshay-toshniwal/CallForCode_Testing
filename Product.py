import csv
from csv import writer

from PlayAudio import playAudio
from KiloGram import acceptQuantityKg





def identifyProduct(translatedText):
    flg = None
    product=translatedText.upper()
    temp = product
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
                        break
            f1 = open('productlit.csv')
            csv_f1 = csv.reader(f1)

            if flg == None:
                for column in csv_f1:
                    for y in x1:
                        y = y.capitalize()
                        if y == column[0]:
                            prd = y
                            flg = 2
                            break
            f1 = open('productpc.csv')
            csv_f1 = csv.reader(f1)
            if flg == None:
                for column in csv_f1:
                    for y in x1:
                        y = y.capitalize()
                        if y == column[0]:
                            prd = y
                            flg = 3
                            break            

    if (flg==1):
        acceptQuantityKg()
        
    elif(flg==2):
        print('Liter')

    elif(flg==3):
        print('Piece')
    else:
        import onlineOrder

        onlineOrder.orderStart()


