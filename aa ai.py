import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import threading
import tkinter as tk

# ---------- Voice Engine ----------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------- GUI Window ----------
root = tk.Tk()
root.title("Prem AI Assistant")
root.geometry("400x300")
root.resizable(False, False)

status_text = tk.StringVar()
status_text.set("Click Start to speak")

# ---------- Voice Listening ----------
running = False

def listen_loop():
    global running
    r = sr.Recognizer()

    speak("Hello Prem, I am your assistant")

    while running:
        try:
            with sr.Microphone() as source:
                status_text.set("Listening...")
                audio = r.listen(source)

            command = r.recognize_google(audio, language='en-in').lower()
            status_text.set(f"You said: {command}")

            if "time" in command:
                time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {time}")

            elif "open youtube" in command:
                webbrowser.open("https://youtube.com")
                speak("Opening YouTube")

            elif "open google" in command:
                webbrowser.open("https://google.com")
                speak("Opening Google")

            elif "stop" in command or "exit" in command:
                speak("Goodbye Prem")
                stop_assistant()

        except:
            status_text.set("Didn't catch that")

# ---------- Control Buttons ----------
def start_assistant():
    global running
    if not running:
        running = True
        threading.Thread(target=listen_loop, daemon=True).start()

def stop_assistant():
    global running
    running = False
    status_text.set("Assistant stopped")

# ---------- GUI Layout ----------
title = tk.Label(root, text="🎙️ Prem AI Assistant", font=("Arial", 16, "bold"))
title.pack(pady=10)

status_label = tk.Label(root, textvariable=status_text, font=("Arial", 10))
status_label.pack(pady=10)

start_btn = tk.Button(root, text="Start Listening", command=start_assistant, width=20, bg="green", fg="white")
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop", command=stop_assistant, width=20, bg="red", fg="white")
stop_btn.pack(pady=5)

root.mainloop()
