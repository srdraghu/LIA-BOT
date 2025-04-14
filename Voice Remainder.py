from win10toast import ToastNotifier
import time
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
toaster = ToastNotifier()
print('\nWelcome!.SET A VOICE NOTIFICATION REMAINDER')
title = input('\nTitle of remainder : ')
msg = input('Message :')
minutes = float(input("Set time : "))
seconds = minutes * 60
print('\nRemainder set Successfully\n')
time.sleep(seconds)
toaster.show_toast(title, msg, duration=0.5, threaded=True)

while toaster.notification_active:
    time.sleep(0.1)
    talk(title)
    talk(msg)