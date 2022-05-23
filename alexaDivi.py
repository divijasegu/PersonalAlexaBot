from sys import int_info
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time
import wikipedia
import pyjokes
listener = sr.Recognizer() # used to recognize the voice come from microphone
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#5,6 lines to change the voice to female version
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    
    try:
        with sr.Microphone() as source:
            print("LISTENING....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                #talk(command)# repeats the words speaken by us     
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is'+time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person)
        print(info[:300])
        talk(info[:300])
    elif 'date' in command:
        talk('sorry,I have an headache')
    elif 'are you single' in command:
        talk('I am in relationship')
    elif 'who is your lover' in command:
        talk('I have a crush on siri')
    elif 'joke' in command:
        talk(pyjokes.get_joke()) 
    else:
        talk('Please say the command again') 
           
        
timeout  = time.time() + 100    
while True:
    run_alexa() 
    if time.time()>timeout:
        break
           
    

    
