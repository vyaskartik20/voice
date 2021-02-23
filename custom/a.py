# pip install pyttsx3
#pip install SpeechRecognition

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio) :
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    


if __name__ == "__main__" : 
    # speak(" input in here")
    # takeCommand()