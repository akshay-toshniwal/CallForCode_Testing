from Recognize import recognize
from Translator import trans
from Product import identifyProduct
from PlayAudio import playAudio



def orderStart():
    audioFile = 'ordertitle.wav'
    playAudio(audioFile)
    speechToText=recognize()
    print(speechToText)
    if speechToText == "unknown error occured":
        orderStart()
        speechToText=None
    else:
        tranlatedText=trans(speechToText)
        identifyProduct(tranlatedText)

print('Online start ')
orderStart()
print('online end')