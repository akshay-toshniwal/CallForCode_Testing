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


def doYouWantToContinue():
    print("DO YOU WANT TO ADD NEW PRODUCT SAY YES OR NO ADD AUDIO HERE")
    chck=None
    speechToText = recognize()
    print(speechToText)
    if speechToText == "unknown error occured":
        doYouWantToContinue()
        speechToText = None
    else:
        tranlatedText = trans(speechToText)
        temp = tranlatedText
        if len(temp) != 0:
            x1 = temp.split()
            regex = re.compile("YES|NO|SURE|SURELY|OFCOURSE|CERTAINLY|SOMETIMES|NEVER|NOT|NOPE|ABSOLUTELY|NOTHING|NAI\w*")
            word = regex.findall(temp)
            if len(word) != 0:
                if (word[0] == 'YES' or word[0] == "SOMETIMES" or word[0] == "SURE" or word[0] == "SURELY" or word[0] == "CERTAINLY" or word[0] == "ABSOLUTELY"):
                    chck="YES"
                elif (word[0] == 'NO' or word[0] == "NEVER" or word[0] == "NOT" or word[0] == "NOPE" or word[0] == "NOTHING"):
                    chck ="NO"
            else:
                playsound('predwn.wav')
                doYouWantToContinue()

    if chck=='YES':
            orderStart()
    else:
        quit()


orderStart()
doYouWantToContinue()