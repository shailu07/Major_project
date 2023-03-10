import ctypes
import datetime
import json
import os
import shutil
import smtplib
import subprocess
import time
import tkinter
import webbrowser
from tkinter import *
from urllib.request import urlopen
import ecapture as ec
import points as points
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha
from speedtest import Speedtest

voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)


def speak(text):
    voiceEngine.say(text)
    voiceEngine.runAndWait()


def wish():
    print("Wishing.")
    hour = int(datetime.datetime.now().hour)
    global uname, asname
    if 0 <= hour < 12:
        speak("Good Morning sir or madam!")

    elif hour < 18:
        speak("Good Afternoon sir or madam!")

    else:
        speak("Good Evening sir or madam!")

    asname = "ELZA"
    speak("I am your Voice Assistant,")
    speak(asname)
    print("I am your Voice Assistant,", asname)


def getName():
    global uname
    speak("Can I please know your name?")
    uname = takeCommand()
    print("Name:", uname)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(uname)


def takeCommand():
    global showCommand
    showCommand.set("Listening....")
    cmdLabel.config(textvariable=points)
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        userInput = recog.listen(source)

    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language='en-in')
        print(f"Command is: {command}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"

    return command


def sendEmail(to, content):
    print("Sending mail to ", to)
    dct = {"sailaja": "sailushiny7@gmail.com", "sweety": "sailaja.jakkula777@gmail.com",
           "gautam": "ksaigoutham2829@gmail.com", "Dinesh": "dineshkalcheti296@gmail.com"}
    mail_id = dct[to]
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # paste your email id and password in the respective places
    server.login('elzaassistant@gmail.com', 'abnrvqyzlfqntbbt')
    server.sendmail('elzaassistant@gmail.com', mail_id, content)
    server.close()


def fun_talk(audio):
    voiceEngine.say(audio)
    voiceEngine.runAndWait()


def computational_intelligence(question):
    try:
        client = wolframalpha.Client("HLPQQH-67TV6P4425")
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None


def callVoiceAssistant():
    uname = ''
    asname = ''
    os.system('cls')
    wish()
    getName()
    print(uname)

    while True:

        command = takeCommand().lower()
        print(command)

        if "elza" in command:
            wish()

        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, ")
            speak(uname)

        elif "good morning" in command or "good afternoon" in command or "good evening" in command:
            speak("A very" + command)
            speak("Thank you for wishing me! Hope you are doing well!")

        elif 'fine' in command or "good" in command:
            speak("It's good to know that your fine")

        elif "who are you" in command:
            speak("I am your virtual assistant.")

        elif "change my name to" in command:
            speak("What would you like me to call you ?")
            uname = takeCommand()
            speak('Hello again,')
            speak(uname)

        elif "change name" in command:
            speak("What would you like to call me? ")
            assname = takeCommand()
            speak("Thank you for naming me!")

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H : %M :%S")
            speak(f"sir the time is {strTime}")
            print(f"sir the time is {strTime}")

        elif 'wikipedia' in command:
            speak('Searching Wikipedia')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("These are the results from Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            speak("Here you go, the Youtube is opening\n")
            webbrowser.open("https:\\youtube.com")
            time.sleep(10)

        elif 'open google' in command:
            speak("Opening Google\n")
            webbrowser.open("https:\\google.com")
            time.sleep(10)

        elif 'open code' in command:
            codepath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Here you go, the VS code is opening\n")
            os.startfile(codepath)
            time.sleep(10)

        elif 'close visual studio code' in command:
            speak("closing vs code..")
            os.system("TASKKILL /F /IM Code.exe")

        elif 'open stack overflow' in command:
            speak("Opening stack overflow\n")
            webbrowser.open("https:\\stackoverflow.com")
            time.sleep(10)

        elif 'play music' in command or "play song" in command:
            speak("Enjoy the music!")
            music_dir = "C:\\Users\\Lenovo\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))  # if possible add random fun
            time.sleep(10)

        elif 'powerpoint presentation' in command:
            speak("opening Power Point presentation")
            power = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft " \
                    "Powerpoint 2010"
            os.startfile(power)
            time.sleep(10)

        elif 'open notepad' in command:
            speak("Here you go..")
            os.startfile("C:\\WINDOWS\\system32\\notepad.exe")
            time.sleep(5)

        elif 'close notepad' in command:
            os.system("TASKKILL /F /IM notepad.exe")

        elif 'price of' in command:
            query = command.replace('price of', '')
            query = "https://www.amazon.in/s?k=" + query[1:]
            webbrowser.open(query)
            time.sleep(10)

        elif 'joke' in command:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif "open gmail" in command:
            webbrowser.open_new_tab("https:\\gmail.com")
            speak("Google mail open now")
            time.sleep(10)

        elif 'mail' in command:
            try:
                speak("Whom should I send the mail")
                to = takeCommand()
                speak("What is the body?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent successfully !")
                print("Email has been sent successfully !")
            except Exception as e:
                print(e)
                speak("I am sorry, not able to send this email")

        elif "will you be my gf" in command or "will you be my bf" in command:
            speak("I'm not sure about that, may be you should give me some time")

        elif "i love you" in command:
            speak("Thank you! But, It's a pleasure to hear it from you.")

        elif 'month' in command or 'month is going' in command:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                fun_talk(month)

            tell_month()

        elif 'day' in command or 'day today' in command:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                fun_talk(day)

            tell_day()

        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open(command)
            time.sleep(10)

        elif "calculate" in command:
            question = command
            answer = computational_intelligence(question)
            speak(answer)

        elif "what is" in command or "who is" in command:
            question = command
            answer = computational_intelligence(question)
            speak(answer)

        elif 'what you want to do' in command:
            fun_talk("I want to help people to do certain tasks on their single voice commands.")

        elif 'alexa' in command:
            fun_talk("I don't know Alexa, but I've heard of Alexa. If you have Alexa, "
                     "I may have just triggered Alexa. If so, sorry Alexa.")

        elif 'google assistant' in command:
            fun_talk("He was my classmate, too intelligent guy. We both are best friends.")

        elif 'siri' in command:
            fun_talk("Siri, She's a competing virtual assistant on   a competitor's phone. "
                     "Not that I'm competitive or anything.")

        elif 'cortana' in command:
            fun_talk("I thought you'd never ask. So I've never thought about it.")

        elif 'python assistant' in command:
            fun_talk("Are you joking. You're coming in loud and clear.")

        elif 'what language you use' in command:
            fun_talk("I am written in Python and I generally speak english.")

        elif 'news' in command:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey"
                                  "=d52ba6d835c842bd86c560d3a5d7291f")
                data = json.load(jsonObj)
                i = 1
                speak("here are your top news from times of india")
                print('''==========TIMES OF INDIA==========''' + '\n')
                for item in data['articles']:
                    print(str(i) + '.' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '.' + item['title'] + '\n')

            except Exception as e:
                print(str(e))

        elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
            ec.capture(0, "elza camera", "img.jpg")
            speak("The screenshot has been successfully captured")

        elif 'lock windows' in command:
            speak("locking windows")
            ctypes.windll.user32.lockWorkStation()

        elif 'shutdown windows' in command or 'log off' in command:
            speak("shutting down windows")
            os.system("shutdown /s /t 1")
            time.sleep(3)

        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])
            time.sleep(3)

        elif "write a note" in command:
            speak("what should i write")
            note = takeCommand()
            file = open('data.txt', 'w')
            speak("sir should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(note)
                speak("written your note successfully !!")
            else:
                file.write(note)
                speak("written your note")

        elif "show me my notes" in command or "read notes" in command:
            fun_talk("Reading Notes")
            file = open("data.txt", "r")
            data_note = file.readline()
            print(data_note)
            fun_talk(data_note)

        elif 'internet speed' in command:
            st = Speedtest()
            print("Wait!! I am checking your Internet Speed...")
            fun_talk("Wait!! I am checking your Internet Speed...")
            dw_speed = st.download()
            up_speed = st.upload()
            dw_speed = dw_speed / 1000000
            up_speed = up_speed / 1000000
            print('Your download speed is', round(dw_speed, 3), 'Mbps')
            print('Your upload speed is', round(up_speed, 3), 'Mbps')
            fun_talk(f'Your download speed is {round(dw_speed, 3)} Mbps')
            fun_talk(f'Your upload speed is {round(up_speed, 3)} Mbps')

        elif 'bye' in command:
            speak("Thanks for giving me your time")
            exit()

        else:
            speak("Sorry, I am not able to understand you")


# Creating the main window
wn = tkinter.Tk()
wn.title("ELZA voice Assistant")
wn.geometry('700x300')
wn.config(bg='LightBlue1')

Label(wn, text='Welcome to meet the Voice Assistant "ELZA" ', bg='LightBlue1',
      fg='black', font=('Courier', 15)).place(x=50, y=10)

# Button to convert PDF to Audio form
Button(wn, text="Start", bg='gray', font=('Courier', 15),
       command=callVoiceAssistant).place(x=290, y=100)

showCommand = StringVar()
cmdLabel = Label(wn, textvariable=showCommand, bg='LightBlue1',
                 fg='black', font=('Courier', 15))
cmdLabel.place(x=250, y=150)

# Runs the window till it is closed
wn.mainloop()

'''
elif 'email to shailu' in command:
     try:
         speak("What should I say?")
         content = takeCommand()
         to = "sailushiny7@gmail.com"
         sendEmail(to, content)
         speak("Email has been sent !")
     except Exception as e:
         print(e)
         speak("I am not able to send this email")
'''
