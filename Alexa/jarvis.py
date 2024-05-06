
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Listening")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)
except Exception as e:
    print("An error occurred:", e)
