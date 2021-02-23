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
    
def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source :
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

if __name__ == "__main__" : 
    # speak(" input in here")
    # takeCommand()