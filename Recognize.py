import speech_recognition as sr
from PlayAudio import playAudio
def recognize():
    r = sr.Recognizer()
    try:
       with sr.Microphone() as source2:
        print("say Something....")
        playAudio('beep.wav')
        audio2 = r.listen(source2, timeout=8)
        MyText = r.recognize_google(audio2)
        x = MyText

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        x = "Could not request results; {0}".format(e)
    except sr.UnknownValueError:

        x= "unknown error occured"
    return x
