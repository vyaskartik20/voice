# pip install pyttsx3
#pip install SpeechRecognition

import pyttsx3
import speech_recognition as sr
import datetime
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio) :
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
#audio input to text
def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source :
        #manual error handling
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout = 3, phrase_time_limit = 5 )
        
    try : 
        print("Recognizing ...")
        query = r.recognize_google(audio, language = "en-in")
        print(f"You said : {query}")
        
    except :
        speak("Say that again please ...")
        return "none"
    
    return query

#greet
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <= 12 :
        speak("Good Morning ! ")
    elif hour >12 and hour <= 18 :
        speak("Good Afternoon ! ")
    else :
        speak("Good Evening ! ")

    speak("Hello on the other side. I am Jarvis, pleased " + 
        "to be here ! How may I be of assistance to you")

if __name__ == "__main__" : 
    wish()
    
    while True:
        query = takeCommand().lower()
    
        #logic building for task

        if "open notepad" in query : 
            notepadPath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(notepadPath)
    
    pass