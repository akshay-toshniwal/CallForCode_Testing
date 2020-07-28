from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import re
import pyttsx3
import csv
from csv import writer
from googletrans import Translator
import os
import random
import sys


result=[]
crochckfnm=[]
quehin = ['donque.wav','doncty.wav','donmod.wav']
def audioGeneration (qtext ,filnm) :
    authenticator = IAMAuthenticator('JUmWiBlaFBXxwGIc3rIWu_Ed3RWrKlyDL63jldvCJeGZ')
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/8d2ac780-cc69-4350-9f2b-3f4439e0d590')

    with open(filnm, 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                qtext,
                voice='en-US_MichaelV2Voice',
                accept='audio/wav'
            ).get_result().content)
        audio_file.close()
    return(audio_file.name)

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)




def finalResult(reslt):
    result.append(reslt)





def readCity(inp,wavnm , hoe):
    temp = inp
    if len(temp) != 0:
        x1 = temp.split()
        if len(x1) != 0:
            f = open('worldcities.csv')
            csv_f = csv.reader(f)
            city = None
            for column in csv_f:
                for y in x1:
                    y = y.capitalize()
                    if y == column[0]:
                        city = y
                        finalResult(city)

            if city==None:
                if hoe == 1:
                    playsound('donwn.wav')
                    questCity(wavnm , hoe)
                if hoe == 0:
                    playAD(wavnm)
                    questCity(wavnm , hoe)


        else:
            pass

    else:
        if hoe == 1:
            playsound('donwn.wav')
            questCity(wavnm, hoe)
        if hoe == 0:
            playAD(wavnm)
            questCity(wavnm, hoe)


def readMOD(inp,wavnm , hoe):
    temp = inp
    if len(temp) != 0:
        x1 = temp.split()
        regex = re.compile("CASH|WEALTH|FOOD|MONEY|GRAIN|CLOTHES|CLOTH|ANA\w*")
        word = regex.findall(temp)
        if len(word) != 0:
            finalResult(str(word[0]))

        else:
            if hoe == 0:
                playAD(wavnm)
                questMOD(wavnm,hoe)
            if hoe == 1:
                playad(wavnm)
                questMODH(wavnm,hoe)


def questMOD(wavnm , hoe):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            print("say Something....")
            audio2 = r.listen(source2, timeout=6)
            MyText = r.recognize_google(audio2)
            x = MyText.upper()
            readMOD(x, wavnm,hoe)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
        if hoe == 0:
            playAD(wavnm)
            questMOD(wavnm,hoe)


def playAD(wavnm):
    song = AudioSegment.from_wav(wavnm)
    play(song)



def engFunction():
    for i in range(len(crochckfnm)):

        wavnm = crochckfnm[i]
        playAD(wavnm)

        if i == 0:
            questYn(wavnm ,0)
        elif i == 1:
            questCity(wavnm,0)

        elif i == 2:
            questMOD(wavnm,0)





def playad(wavnm1):
    playsound(wavnm1)


def questYnH(wavnm ,hoe):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            print("say Something....")

            audio2 = r.listen(source2, timeout=8)
            MyText = r.recognize_google(audio2)
            translator = Translator()
            MyText1 = (translator.translate(MyText, src='hi'))
            x = MyText1.text.upper()

            yon = readYoN(x, wavnm ,hoe)
            if yon == 'NO':
                exit()

            finalResult(yon)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
        playad(wavnm)
        questYnH(wavnm,hoe)


def questMODH(wavnm ,hoe):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            print("say Something....")

            audio2 = r.listen(source2, timeout=8)
            MyText = r.recognize_google(audio2)
            translator = Translator()
            MyText1 = (translator.translate(MyText, src='hi'))
            x = MyText1.text.upper()
            readMOD(x, wavnm ,hoe)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
        playad(wavnm)
        questMODH(wavnm ,hoe)



def hinFunction():
    for i in range(len(quehin)):
        wavnm1=quehin[i]
        playad(wavnm1)

        if i == 0:
            questYnH(wavnm1,1)
        elif i == 1:
            questCity(wavnm1,1)

        elif i == 2:
            questMODH(wavnm1,1)



def questCity(wavnm , hoe):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            print("say Something....")
            audio2 = r.listen(source2, timeout=6)
            MyText = r.recognize_google(audio2)
            x = MyText.upper()
            readCity(x, wavnm , hoe)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
        if hoe == 0 :
            playAD(wavnm)
            questCity(wavnm,hoe)
        if hoe == 1:
            playad(wavnm)
            questCity(wavnm, hoe)


def questYn(wavnm,hoe):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            print("say Something....")
            audio2 = r.listen(source2, timeout=6)
            MyText = r.recognize_google(audio2)
            x = MyText.upper()
            yon=readYoN(x , wavnm ,hoe)
            if yon ==  'NO':
                exit()

            finalResult(yon)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
        playAD(wavnm)
        questYn(wavnm,hoe)


def readYoN(inp , wavnm , hoe):
    temp=inp
    if len(temp) != 0:
        x1 = temp.split()
        regex = re.compile("YES|NO|SURE|SURELY|OFCOURSE|CERTAINLY|SOMETIMES|NEVER|NOT|NOPE|ABSOLUTELY|NOTHING|NAI\w*")
        word = regex.findall(temp)
        if len(word )!= 0:

            if (word[0] == 'YES' or word[0] == "SOMETIMES" or word[0] == "SURE" or word[0] == "SURELY" or word[0] == "CERTAINLY" or word[0] == "ABSOLUTELY"):
                #ans.append("YES")
                return "YES"
            elif (word[0] == 'NO' or word[0] == "NEVER" or word[0] == "NOT" or word[0] == "NOPE" or word[0] == "NOTHING"):
                #ans.append("NO")
                return  "NO"
        else:
            if hoe == 0:
                playAD(wavnm)
                questYn(wavnm,hoe)

            if hoe == 1:
                playad(wavnm)
                questYnH(wavnm,hoe)



def chckEngHi(rec):
    temp = rec
    if len(temp) != 0:
        x1 = temp.split()
        regex = re.compile("HINDI|ENGLISH\w*")
        word = regex.findall(temp)
        if len(word) != 0:

            if (word[0] == 'HINDI' ):
                return "HINDI"
            elif (word[0] == 'ENGLISH'):
                return "ENGLISH"
        else:
            playsound('langwarning.wav')
            langSelection()




def langSelection ():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            print("say Something....")
            audio2 = r.listen(source2, timeout=8)
            MyText = r.recognize_google(audio2)
            x = MyText.upper()
            lang=chckEngHi(x)
            if lang == 'ENGLISH':
                engFunction()
            elif lang == 'HINDI' :
                hinFunction()




    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
        playsound('donlngslt.wav')
        langSelection()


def textToAudio():
    listQ = ['Are      you       Interested       in     Donating   ', ' May i Know name of Your City ?', ' May    i     know     Your    form    of    Donation    either   Money   or   Food ']
    filnm = ['donenque.wav','donencty.wav','donenmod.wav']

    for i in range(len(listQ)):
        crochckfnm.append(audioGeneration(listQ[i],filnm[i]))
        print("<<<<< Loading >>>>>")


textToAudio()

#playsound('donlngslt.wav')
result.append(random.randint(8888888888,9999999999))
engFunction()
print(result)

append_list_as_row("dondb.csv", result)

os.system('main.py')