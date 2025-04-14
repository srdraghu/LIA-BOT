import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from playsound import playsound

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print('Im all ears my friend...')
print('Im ready to chat with you nanba')
print('Listening.....')

def talk(text):
    engine.say(text)
    engine.runAndWait() 

def take_command():
    
    try:
        command = ''
        talk('Hello Raghu')   
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if 'friend' in command:
                command = command.replace('friend', '')
                print(command)
    except:
        pass
    return command

def run_bot():
    command = take_command()
    print(command)
    if 'hello' in command:
        name=command.replace('hello','')
        talk(name)
        talk('How are you')
    if 'play' in command:
        song = command.replace('play', '')
        print('PLAYING'+song)
        talk('Playing. Enjoy your video')
        pywhatkit.playonyt(song)
    elif 'open' in command:
        io = command.replace('open', '.com')
        jk = webbrowser.open(io)
        talk('Opening')
    elif 'weather' in command:
        we = command.replace('weather', '')
        wikipedia.summary(we)
        print(we)
        talk(we)
    elif 'alcohol' in command:
        sd = command.replace('alcohol', '')
        playsound('thaniya.mp3')   
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'about' in command:
        a = command.replace('about', '')
        b = wikipedia.summary(a, 1)
        print(b)
        talk(b)
    elif 'who is' in command:
        info = command.replace('who is', '')
        res = wikipedia.summary(info, 1)
        print(res)
        talk(res)
    elif 'tell me about' in command:
        o = command.replace('tell me about', '')
        h = wikipedia.summary(o, 1)
        print(h)
        talk(h)
    elif 'what is' in command:
        meaning = command.replace('what is', '')
        results = wikipedia.summary(meaning, 1)
        print(results)
        talk(results)
    elif 'hi' in command:
        wish = command.replace('hi', '')
        playsound('naila.mp3')
    elif 'hello' in command:
        josh = command.replace('hello', '')
        talk('Hello My sweet friend')
    elif 'Who are you' in command:
        talk('Im LIA. Your friend')
    elif 'doing' in command:
        rt = command.replace('doing', '')
        talk('Nothing special. Just waiting for your speech friend.')
    elif 'Who created you' in command:
        talk('Arun Jetlee, Risapna, Shwetha, Selva Nandhini')
    elif 'will you talk to me' in command:
        talk('Yeah sure my sweet friend. Dont hesitate')
    elif 'date' in command:
        talk('sorry friend, I have a  severe headache. Please take care of me')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi. Wifi is my partner.')
    elif 'do you love me' in command:
        talk('No doubt in that. I love you as my friend')
    elif 'boring' in command:
        ui = command.replace('boring', '')
        playsound('va.mp3')
    elif 'i love you' in command:
        qw = command.replace('i love you', '')
        playsound('tam.mp3')





































































































































        
    elif 'thanks' and 'thank' in command:
        lk = command.replace('thanks,thank', '')
        playsound('Thalainagaram.mp3')
    elif 'life' in command:
        po = command.replace('life', '')
        playsound('build.mp3')
    elif 'stupid' in command:
        qe = command.replace('stupid', '')
        playsound('arivu.mp3')
    elif 'joke' in command:
        rs = command.replace('joke', '')
        talk(pyjokes.get_joke())
    elif 'bye' in command:
        vb = command.replace('bye', '')
        quit()
    elif 'see you' in command:
        tr = command.replace('see you', '')
        playsound('Vadivelu.mp3')
    else: 
        talk('')
while True:
    run_bot()



