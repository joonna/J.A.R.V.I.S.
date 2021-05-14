from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import pyautogui
import time
import tensorflow as tf
from gtts import gTTS

pyautogui.PAUSE = 1

def listen(audio):
    #audio passed as argument

    print(audio)
    text_to_speech = gTTS(text=audio, lang='en')
    text_to_speech.save('audio.mp3')
    os.system('mpg123 audio.mp3')


def myCommand():
    #listens for commands

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def blizzard():
    pyautogui.keyDown('winleft')
    pyautogui.keyUp('winleft')
    pyautogui.typewrite('bliz')
    pyautogui.press('enter')

def steam():
    pyautogui.keyDown('winleft')
    pyautogui.keyUp('winleft')
    pyautogui.typewrite('steam')
    pyautogui.press('enter')

def cmd():
    pyautogui.keyDown('winleft')
    pyautogui.keyUp('winleft')
    pyautogui.typewrite('cmd')
    pyautogui.press('enter')

def typeIt(command):
    #pyautogui.typewrite(command)
    reg_ex = pyautogui.typewrite(' (.+)', command)
    if reg_ex:
        domain = reg_ex.group(1)
        print('Done!')
    else:
        pass
def closeAssistant():
    os.syste('TASK KILL /F /IM wmplayer.exe')

def turnOff():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('F4')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('F4')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    
def shutdown():
    cmd();
    pyautogui.typewrite('shutdown /s')

def sleep():
    cmd();
    pyautogui.typewrite('shutdown /h')
    
def assistant(command):
    #if statements for executing commands

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        
    elif 'start battle.net' in command:
        blizzard();
        
    elif 'start cmd' in command:
        cmd();
        
    elif 'start steam' in command:
        steam();
        
    elif 'open app' in command:
        app(command);
        
    elif 'kill task' in command:
        closeAssistant();
        
    elif 'turn off' in command:
        turnOff();
        
    elif 'shut down' in command:
        shutdown();
        
    elif 'sleep' in command:
        sleep();

    elif 'print screen' in command:
        pyautogui.screenshot()
        
    elif 'open youtube' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.youtube.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'play chess' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.chess.com/play/computer'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    elif 'what time is it' in command:
        print(time())
        
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'what\'s up' in command:
        listen('The sky')
    elif 'tell me a joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            listen(str(res.json()['joke']))
        else:
            listen('OH NO!!I ran out of jokes!!')

    elif 'email' in command:
        listen('Who is the recipient?')
        recipient = myCommand()

        if 'Conor' in recipient:
            listen('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('Conor Logsdon', 'logsdonconor@gmail.com', content)

            #end mail connection
            mail.close()

            listen('Email sent.')

        else:
            listen('I don\'t know what you mean!')


listen('I am ready for your command')

def main():
#loop to continue executing multiple commands
        assistant(myCommand())
while True:
    main()
