from PlayAudio import playAudio
from Recognize import recognize
import re
import csv
from csv import writer
from Translator import trans


def doYouWantToContinue():
    playAudio("addmore.wav")
    chck = None
    speechToText=None
    speechToText = recognize()
    print(speechToText)
    if speechToText == "unknown error occured":
        doYouWantToContinue()
        speechToText = None
    else:
        tranlatedText = trans(speechToText)
        temp = tranlatedText.upper()
        if len(temp) != 0:
            x1 = temp.split()
            regex = re.compile("YES|NO|SURE|SURELY|OFCOURSE|CERTAINLY|SOMETIMES|NEVER|NOT|NOPE|ABSOLUTELY|NOTHING|NAI")
            word = regex.findall(temp)
            if len(word) != 0:
                if (word[0] == 'YES' or word[0] == "SOMETIMES" or word[0] == "SURE" or word[0] == "SURELY" or word[0] == "CERTAINLY" or word[0] == "ABSOLUTELY"):
                    audioFile = 'afteraddmore.wav'
                    playAudio(audioFile)
                    speechToText = recognize()
                    print(speechToText)
                    if speechToText == "unknown error occured":
                        audioFile = 'afteraddmore.wav'
                        speechToText = None
                    else:
                        from Product import identifyProduct
                        translatedText = trans(speechToText)
                        identifyProduct(translatedText)
                elif (word[0] == 'NO' or word[0] == "NEVER" or word[0] == "NOT" or word[0] == "NOPE" or word[0] == "NOTHING"):
                    print('Thank You your Order is Placed')
            else:

                doYouWantToContinue()



def identifyUnit(temp, qty,prd):
    regex = re.compile("LITRES|LITRE|ML|MILI|LETTERS")

    word = regex.findall(temp)
    if word == 'LETTERS':
        word='LITRES'

    lst = []
    lst.append(prd)
    lst.append(qty)
    lst.extend(word)
    with open("record.csv", 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(lst)
    doYouWantToContinue()

def identifyQuantity(quantity,prd):
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

    if flg == 1:
        identifyUnit(temp, qty,prd)
    else:
        acceptQuantityLt(prd)


def acceptQuantityLt(prd):
    quantity = None
    playAudio('audiolit.wav')
    quantity = recognize()
    if quantity == "unknown error occured":
        acceptQuantityLt(prd)
    else:

        identifyQuantity(quantity,prd)


