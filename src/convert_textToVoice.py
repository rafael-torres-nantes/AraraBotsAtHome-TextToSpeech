import pyttsx3

def textToSpeech(textFile):

    textToSpeech = pyttsx3.init()

    textToSpeech.say(textFile)
    textToSpeech.runAndWait()

