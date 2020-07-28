import speech_recognition as sr
import pyttsx3
import re
from googletrans import Translator
from playsound import playsound
import csv
from csv import writer
import os
import sys
import random

ans = []
fans = []

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)



def fresult(g , q):

    im=g[0]
    G=g[1:]
    res_list = []
    for i in range(0, len(q)):
        res_list.append(q[i] * G[i])
    fan=im-sum(res_list)
    print(fan)
    c1=(im*40)/100
    c2=(im*70)/100
    if fan<=c1 :
        playsound('engpredhighrisk.wav')
        fans.append('HIGH RISK')
        append_list_as_row("preddb.csv", fans)
    elif fan<=c2 and fan>c1 :
        fans.append('MODERATE RISK')
        playsound('engpredmrisk.wav')
        append_list_as_row("preddb.csv", fans)
    else :
        fans.append('LOW RISK')
        playsound('engpredlowrisk.wav')
        append_list_as_row("preddb.csv", fans)




def finalAnswer(result):
    fans.append(result)







def acceptAge():
    playsound('engpredage.wav')
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source2:
            print("say Something....")
            audio2 = r.listen(source2, timeout=12)
            MyText = r.recognize_google(audio2)
            translator = Translator()
            MyText1 = (translator.translate(MyText, src='hi'))
            x = MyText1.text.upper()
            numbers = []
            flag=0
            for word in x.split():
                if word.isdigit():
                    numbers.append(int(word))
                    flag = 1
            if flag == 1:
                age = numbers[0]
                finalAnswer(age)

            else:
                acceptAge()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
        acceptAge()

def playAccept():
    playsound(audiofile)
    readAudio()


def readText(inp):
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
            playsound('engpredwn.wav')
            readAudio()


def binaryConvert(list1):
    list2=[]
    #for i in list1:
    if list1 == 'YES':
        finalAnswer(1)
       # list2.append(1)

    elif list1 == 'NO':
        finalAnswer(0)
        #list2.append(0)
    else:
        pass
    #return list2

def readAudio():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Function to convert text to
    # speech
    def SpeakText(command):
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    # Loop infinitely for user to
    # speak

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:
            print("say Something....")

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            #r.adjust_for_ambient_noise(source2, duration=0)

            # listens for the user's input
            audio2 = r.listen(source2,timeout=8)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)

            translator = Translator()
            MyText1= (translator.translate(MyText , src='hi'))
            x=MyText1.text.upper()
            ans = readText(x)
            binaryConvert(ans)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
        playAccept()

fnm=['engpredfever.wav','engpredsob.wav','engpreddib.wav','engpredbp.wav','engpredtastesmell.wav','engpredcgh.wav','engpredfat.wav']
fans.append(random.randint(8888888888,9999999999))
playsound('engpredtitle.wav')
acceptAge()

for i in range(len(fnm)):
    audiofile=fnm[i]
    print(audiofile)
    playAccept()

print(fans)
ag = fans[1]
q = fans[2:]
print(ag)
print(q)
g1 = [35, 5.5, 4, 3.1, 3.1, 6.5, 6.0, 6.8]
g2 = [40, 6.2, 4.7, 3.8, 3.9, 7.2, 6.7, 7.5]
g3 = [60, 9.1, 7.6, 6.6, 6.6, 10.1, 9.6, 10.4]
g4 = [45, 6.92, 5.42, 4.55, 4.55, 7.92, 7.42, 8.22]
g5 = [30, 4.79, 3.29, 2.38, 2.37, 5.79, 5.29, 6.09]

if ag <= 10:
    fresult(g1, q)

elif ag >= 11 and ag <= 20:
    fresult(g2, q)

elif ag >= 21 and ag <= 50:
    fresult(g3, q)

elif ag >= 51 and ag <= 70:
    fresult(g4, q)

else:
    fresult(g5, q)


os.system('main.py')