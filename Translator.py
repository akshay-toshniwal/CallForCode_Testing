from googletrans import Translator

def trans(SpeechToText):
    translator = Translator()
    translatedText = (translator.translate(SpeechToText))

    return translatedText.text