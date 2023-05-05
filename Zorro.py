from __future__ import with_statement
import datetime
import os
import random
import sys
import time
import webbrowser
import json
import pyautogui
import pyttsx3
import pywhatkit as kit
import requests
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("My name is Zorro. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening.")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak("Recognizing.")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Say that again please.")
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how is the weather' in query:
            API_KEY = '118fa118e9d980233a7bdc3697610402'
            city = 'Mumbai'
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            # Make the API request and parse the JSON response
            response = requests.get(url)
            data = json.loads(response.text)
            # Extract relevant weather data from the JSON response
            description = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            # Generate the text-to-speech message
            message = f"The weather in {city} is {description}, with a temperature of {temp} degrees Celsius, a feels " \
                      f"like temperature of {feels_like} degrees Celsius, humidity of {humidity} percent, " \
                      f"and wind speed of {wind_speed} meters per second. "
            # Speak the message aloud
            engine.say(message)
            engine.runAndWait()

        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'close youtube' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'open google' in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)

        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif "shut down system" in query:
            os.system("shutdown /s /t 5")

        elif "restart system" in query:
            os.system("shutdown /r /t 5")

        elif "lock system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "stop zoro" in query:
            speak(' alright then, I am switching off')
            sys.exit()

        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "refresh" in query:
            pyautogui.moveTo(1551, 551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620, 667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

        elif "scroll down" in query:
            pyautogui.scroll(1000)

        elif "drag visual studio to the right" in query:
            pyautogui.moveTo(46, 31, 2)
            pyautogui.dragRel(1857, 31, 2)

        elif "rectangular spiral" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('paint')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.moveTo(100, 193, 1)
            pyautogui.rightClick
            pyautogui.click()
            distance = 300
            while distance > 0:
                pyautogui.dragRel(distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, distance, 0.1, button="left")
                pyautogui.dragRel(-distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, -distance, 0.1, button="left")

        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")

        elif "who are you" in query:
            print('My Name Is Zorro')
            speak('My Name Is Zorro')
            print('I can do Everything that my creator programmed me to do')
            speak('I can do Everything that my creator programmed me to do')

        elif "who created you" in query:
            print('I Do not Know His Name, I was created with Python Language, in Pycharm.')
            speak('I Do not Know His Name, I was created with Python Language, in Pycharm.')

        elif "open notepad and write something" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('notepad')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write("Hello Human.", interval=0.1)

        elif "what do you see" in query:
            print("I see someone gorgeous sitting in front of me. God bless you and have a good day!")
            speak("I see someone gorgeous sitting in front of me. God bless you and have a good day!")

        elif 'type' in query:  # 10
            query = query.replace("type", "")
            pyautogui.write(f"{query}")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'open chrome' in query:
            img = pyautogui.locateCenterOnScreen(
                'Screenshot1.png')  # [take a screenshot of chrome and crop it, then save the image in jarvis folder]
            pyautogui.doubleClick(img)
            time.sleep(1)
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
            time.sleep(1)
            img1 = pyautogui.locateCenterOnScreen(
                'screenshot2.png')  # [take screenshot where you wanted to make the click]
            pyautogui.click(img1)
            time.sleep(2)
            img2 = pyautogui.locateCenterOnScreen('screenshot3.png')
            pyautogui.click(img2)
            time.sleep(1)
            pyautogui.typewrite('Hello user!!!', 0.1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('esc')
            img3 = pyautogui.locateCenterOnScreen('screenshot4.png')
            pyautogui.click(img3)

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
