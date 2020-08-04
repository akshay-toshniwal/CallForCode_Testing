from Recognize import recognize
from Translator import trans
from Product import identifyProduct
from PlayAudio import playAudio
import re


def orderStart(flg):
    if flg==0:
        audioFile = 'ordertitle.wav'
    elif flg==1:
        audioFile = 'afteraddmore.wav'
    playAudio(audioFile)
    speechToText = recognize()
    print(speechToText)
    if speechToText == "unknown error occured":
        orderStart(0)
        speechToText = None
    else:
        translatedText = trans(speechToText)
        identifyProduct(translatedText)




orderStart(0)
