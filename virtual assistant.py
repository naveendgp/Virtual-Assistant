import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import time
import webbrowser
import winshell
import pyjokes
import subprocess
import smtplib
import requests
import json
import wolframalpha
import pywhatkit
import sys



warnings.filterwarnings("ignore")


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("you said: " +  data)

    except sr.UnknownValueError:
        print("sorry I couldn't get you")

    except sr.RequestError as ex:
        print("sorry couldnl't recognize you " + ex)


    return data

def response(text):
    print(text)

    tts = gTTS(text=text, lang = "en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "assisant"

    text = text.lower()

    if action_call in text:
        return True

    return False

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "october",
        "November",
        "December",
    ]


    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return f'Today is {week_now}, {months[month_now -1]} the {ordinals[day_now -1]}'


def say_hello(text):
    greet = ["hi", "hello", " whats'up", "hey hi ", "hey there", "hi goood day"]

    response = ["hi", "hello", " whats'up", "hey hi ", "hey there", "hey naveen", "hi goood day"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + " ."

    return ""

def wiki_person(text):
    list_wiki  =  text.split()
    for i in range(0,len(list_wiki)):
        if i + 3 <= len(list_wiki) -1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]

def note(test):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("email", "password")
    server.sendmail("email", to, content)
    server.close()

while True:

    try:

        text = rec_audio()
        speak = " "

        if "Hermione" or "assistant" in text:

            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = ""

                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary( sentences=1)
                    speak = speak + " " + wiki


            elif "who are you" in text or "define yourself" in text:
                speak = speak + """hi, I am Hermione an virtual assistant. I can perform varies task to make you're life easier """

            elif "your name" in text:
                speak = speak + "my name is hermione"

            elif "I love you" in text:
                speak = speak + "Im in love with naveen"

            elif "who am I" in text:
                speak = speak + "You are probably a human"

            elif " can you talk to me" in text:
                speak = speak + "yes ofcourse I can"

            elif "can you talk to me" in text:
                speak = speak + "yes ofcourse of I can"

            elif "can I change your name" in text:
                speak = speak + "no you cannot"


            elif "who invented you" in text:
                speak = speak + "I am invented by the great genius naveen"

            elif "speak now" in text:
                speak = speak + "Please turn on your camera"

            elif "hi how are you" in text:
                speak = speak + "im good how are you"

            elif "what can you do" in text:
                speak = speak + "I can do varies task like "
                speak = speak + "\n sending email, getting direction and so on."

            elif "your version" in text:
                speak = speak + "My version is 1.0"

            elif "how are you" in text:
                speak = speak + "I am fine, thank you"
                speak = speak + "\n how are you?"

            elif 'nee epadi irruka' in text:
                speak = speak + 'na nalla iruuken'

            elif "fine" in text or "good" in text :
                speak = speak + "It's good to know that you are fine"

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening google chrome"
                    os.startfile(r"C:\Program Files\Google\Chrome\Application")

            elif "word" in text.lower():
                speak = speak + "Opening Microsoft word"
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")

            elif "excel" in text.lower():
                speak = speak + "Opening Microst excel"
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

            elif "power point" in text.lower() or "ppt" in text.lower():
                speak = speak + "Opening Microsoft Power point"
                os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")

            elif 'play' in text.lower():
                speak = speak + 'playing music'
                pywhatkit.playonyt(text)


            elif  "youtube" in text.lower():
                speak = speak + "Opening Youtube"
                webbrowser.open("https://youtube.com")

            elif  "google" in text.lower():
                speak = speak + "Opening Google"
                webbrowser.open("https://google.com")

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty( confirm = True, show_progress = False, sound = True)
                speak = speak + "recycle bin emptied"

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.youtube.com/results?search_query=" +
                    "+".join(search)
                )

                speak = speak + "Opening " + str(search) + " on youtube"

            elif "note" in text or "remember" in text:
                talk("what would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that"

            elif "tell me a joke" in text or "jokes" in text:
                speak = speak + pyjokes.get_joke()

            elif "where is" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)

            elif "send email to" in text:
                try:
                    talk("what should I send?")
                    content = rec_audio()
                    to = "Reciever email address"
                    send_email(to, content)
                    speak = speak + "Email has sent"

                except Exception as e:
                    print(e)
                    talk("sorry I can't send email")

            elif "mail" in text or "gmail" in text:
                try:
                    talk("what should I say?")
                    content = rec_audio()
                    talk("To whom should I send")
                    to = input("Enter the email address: ")
                    send_email(to, content)
                    speak = speak + "Email has been sent!"

                except Exception as e:
                    print(e)
                    speak = speak + "sorry I'm not able to send this email"

            elif "weather" in text:
                key = "e99818b702b7d15248a06d74063e16e7"
                weather_url = "http://api.openweathermap.org/data/2.5/weather?q"
                ind = text.split().index("in")
                location = text.split()[ind + 1:]
                location = ""
                "".join(location)
                url = weather_url + "appid=e99818b702b7d15248a06d74063e16e7" + key + "&q=" + location
                js = requests.get(url).json()
                if js["cod"] != "404":
                    weather = js["main"]
                    temprature = weather["temp"]
                    temprature = temprature - 273.15
                    humidity = weather["humidity"]
                    desc = js["weather"][0]["description"]
                    weather_response = "The temprature in Celcius is " + str(temprature) + " The humidity is" + str(humidity) + " and weather description is " + str(desc)
                    speak = speak + weather_response

                elif 'sleep' in text:
                    speak = speak + "I'm here to help you anytime"
                    time.sleep('5')

                else:
                    speak = speak + "Sorry City not found"

            elif "calculate" in text:
                app_id = "JVKX9Q-T688P9KKWV"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("calculate")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer

            elif "what is" in text or  "who is" in text:
                app_id = "JVKX9Q-T688P9KKWV"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("is")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer

            elif "don't listen" in text or "stop listening" in text or "sleep now" in text:
                talk("for how many seconds you want me to sleep")
                a = int(rec_audio())
                time.sleep(a)
                speak = speak + str(a) + " seconds completed. Now how can I help you"

            elif "exit" in text or "quit" in text:
                exit()


        else:
            speak = speak + "Application not found"

        response(speak)

    except:
        talk("")






