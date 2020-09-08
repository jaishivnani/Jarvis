#Just Another Very Intelligent System JARVIS
import pyttsx3
import datetime
import speech_recognition as sr
# pyttsx3 is a text-to-speech conversion library in Python. 
# Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may i help you.")

def takeCommand():

 r = sr.Recognizer()
 with sr.Microphone() as source:
     print("Listening")
     r.pause_threshold = 1
     audio = r.listen(source)

     try:
         print("Recognizing...")
         query = r.recognize_google(audio,language='en-in')
         print(f"User said: {query}\n")

     except Exception as e:
         # print(e)

         print("Say that again please...")
         return "None"
     return query






if __name__ == "__main__":
    WishMe()
    takeCommand()