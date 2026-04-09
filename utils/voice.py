import pyttsx3

engine = pyttsx3.init()

def speak(message):
    print("[VOICE]", message)
    engine.say(message)
    engine.runAndWait()