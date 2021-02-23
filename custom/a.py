# pip install pyttsx3
#pip install SpeechRecognition
# pip install opencv-python
# pip install wikipedia

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser

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
    #manual
    # wish()
    
    while True:
        query = takeCommand().lower()
    
        #logic building for task

        if "open notepad" in query : 
            notepadPath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(notepadPath)
    
        if "open command prompt" in query : 
            os.system("start cmd")
            
        if "open camera" in query : 
            cap = cv2.VideoCapture(0)
            while True :
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k ==27 :
                    break
            
            cap.release()
            cv2.destroyAllWindows()
    
        if "play music" in query :
            music_dir = "D:\\voice\\custom\\songs"
            songs = os.listdir(music_dir)
            randomSong = random.choice(songs)
            os.startfile(os.path.join(music_dir, randomSong)) 
            
        if "ip address" in query :
         ip = get('https://api.ipify.org').text
         speak(f"IP address of your system is :  {ip}")
         
        if "wikipedia" in query : 
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            speak(results)
            # print(results)
            
        if "open youtube" in query :
            
            speak("What shoold I search on Youtube")
            
            requestYoutube = takeCommand().lower() 
            requestYoutube = f"https://www.youtube.com/results?search_query={requestYoutube}"
            webbrowser.open(requestYoutube)
            webbrowser.open(requestYoutube)
            
            
        if "open facebook" in query :
            webbrowser.open("www.facebook.com")
            
        if "open stackoverflow" in query :
            webbrowser.open("www.stackoverflow.com")
            
        if "open geeksforgeeks" in query :
            webbrowser.open("www.geeksforgeeks.org")
            
        if "open google" in query :
            speak("What shoold I search on Google")
            
            requestGoogle = takeCommand().lower() 
            requestGoogle = requestGoogle.replace(' ', '+')
            requestGoogle = f"https://www.google.com/search?q={requestGoogle}"
            webbrowser.open(requestGoogle)