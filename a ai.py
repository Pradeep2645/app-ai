import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='en-in')
        print("You said:", command)
        return command.lower()
    except:
        return ""

speak("Hello Prem, I am your assistant")

while True:
    cmd = listen()

    if "time" in cmd:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "open youtube" in cmd:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in cmd:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "stop" in cmd or "exit" in cmd:
        speak("Goodbye Prem")
        break
