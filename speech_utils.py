import speech_recognition as sr
from gtts import gTTS
import os

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # Use 'afplay' on macOS or 'mpg123' on Linux
