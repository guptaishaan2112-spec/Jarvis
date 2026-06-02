from email.mime import text

import speech_recognition as sr
import webbrowser
import pyttsx3 #package to convert text to speech

print('''   to start JARVIS say "HI JARVIS"
            say exit to "EXIT JARVIS"''')
recognizer = sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    # recognize speech using Sphinx
    while True: 
        if recognizer.recognize_sphinx(audio) == "jarvis":
            a="JARVIS is listening"
            print(a)
            speak(a)

        try:
            a="JARVIS thinks you said " + recognizer.recognize_sphinx(audio)
            print(a)
            speak(a)
        except sr.UnknownValueError:
            a="JARVIS could not understand audio"
            print(a)
            speak(a)
        except sr.RequestError as e:
            a=f"JARVIS error; {0}"
            print(a)
            speak(a)
        if recognizer.recognize_sphinx(audio) == "exit":
            a="Goodbye"
            print(a)
            speak(a)
            break
        
    