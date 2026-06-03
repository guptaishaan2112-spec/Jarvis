from email.mime import text

import time
import speech_recognition as sr
import webbrowser
import pyttsx3 #package to convert text to speech

print('''   to start JARVIS say "HI JARVIS"
            say exit to "EXIT JARVIS"''')
recognizer = sr.Recognizer()
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
if __name__ == "__main__":
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        # recognize speech using Sphinx
        if 'jarvis' in recognizer.recognize_google(audio).lower():
            a="JARVIS is listening"
            print(a)
            speak(a)

            print('listening...')
            
            try:
                while True:
                    with sr.Microphone() as source:
                        audio = recognizer.listen(source)
                    a=recognizer.recognize_google(audio)
                    print('jarvis thinks you said: ' + a)
                    speak('jarvis thinks you said: ' + a)
                    print('listening...')
                    if recognizer.recognize_google(audio) == "exit":
                        a="Goodbye"
                        print(a)
                        speak(a)
                        break
            except sr.UnknownValueError:
                a="JARVIS could not understand audio"
                print(a)
                speak(a)
            except sr.RequestError as e:
                a=f"JARVIS error; {e}"
                print(a)
                speak(a)
    except sr.UnknownValueError:
        a="JARVIS could not understand audio"
        print(a)
        speak(a)
                    
            
        