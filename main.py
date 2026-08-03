from email.mime import text

import time
import speech_recognition as sr
import webbrowser
import pyttsx3

from Project1_JARVIS import music_library #package to convert text to speech
'''there is another text to speech package called gTTS but it requires internet connection and also it 
saves the audio file in the system and then plays it which is not efficient for our use case so i have 
used pyttsx3 which is offline and does not save the audio file in the systema and it is free initially 
only but then it requires credits for every query after a certain limit but it is not a problem for us 
as we are not going to use it for heavy queries and also it is more efficient than gTTS for our use case
import music_library #importing music library file'''
from openai import OpenAI
print('''   to start JARVIS say "HI JARVIS"
            say "EXIT JARVIS" or "BYE JARVIS" to stop JARVIS''')
recognizer = sr.Recognizer()
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def open_website(url):
    l=url.split()
    for i in l:
        if i.lower() in music_library.music:
            webbrowser.open(music_library.music[i.lower()])
        else:
            continue
    else:
        pass
    if 'open google' in url.lower():
        webbrowser.open('https://www.google.com')
    elif 'open youtube' in url.lower():
        webbrowser.open('https://www.youtube.com')
    elif 'open facebook' in url.lower():
        webbrowser.open('https://www.facebook.com')
    elif 'open twitter' in url.lower():
        webbrowser.open('https://www.twitter.com')
    elif 'open instagram' in url.lower():
        webbrowser.open('https://www.instagram.com')
    elif 'open linkedin' in url.lower():
        webbrowser.open('https://www.linkedin.com')
    elif 'open github' in url.lower():
        webbrowser.open('https://www.github.com')
    elif a.split()[0].lower() in music_library.music:
        webbrowser.open(music_library.music[a.split()[0].lower()])
    else:
        #let open ai handle the rest of the queries in future updates
        #this will use api key from openai to get the response from the model and then speak it out
        #it will use credits for every query that gets into this clause 
        #so i have let it like this for now and will update it in future updates
        client = OpenAI(api_key="")
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "you are JARVIS", "content": "You are a helpful assistant."},
                {"role": "user", "content": "print hello world in python"}])
    
if __name__ == "__main__":
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        # recognize speech using google speech recognition
        if 'jarvis' in recognizer.recognize_google(audio).lower():
            a="JARVIS is listening"
            print(a)
            speak(a)
            i=0
            
            while i==0:
                try:
                    print('listening...')
                    with sr.Microphone() as source:
                        audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
                    a=recognizer.recognize_google(audio)
                    print('jarvis thinks you said: ' + a)
                    speak('jarvis thinks you said: ' + a)
                    if recognizer.recognize_google(audio).lower() == "bye jarvis" or recognizer.recognize_google(audio).lower() == "exit":
                        a="Goodbye"
                        print(a)
                        speak(a)
                        i=1
                    open_website(a)
                except sr.UnknownValueError:
                    a="JARVIS could not understand audio"
                    print(a)
                except sr.RequestError as e:
                    a=f"JARVIS error; {e}"
                    print(a)
                except sr.WaitTimeoutError:
                    a="JARVIS timed out while listening"
                    print(a)
    except sr.UnknownValueError:
        a="JARVIS could not understand audio"
        print(a)
        speak(a)


print('archivist sync testing')
print('archivist sync testing part 2')
        