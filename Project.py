import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os
import smtplib
import pyjokes
import wikipedia
import pyqrcode
import png
from pyqrcode import QRCode

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def qrCode(myLink):
    qrCode1 = pyqrcode.create(myLink)
    qrCode1.svg("myqr.svg" , scale=8)
    qrCode1.png("myqr.png" , scale=6)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def aboutme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Puskars Voice  Assistant. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    while True:

        query = takeCommand().lower()


        if 'open youtube' in query:
            print("What You Want To Watch...... ")
            ("What You Want To Watch")
            sapicifiedvidY = takeCommand().lower()
            webbrowser.open("https://www.youtube.com/results?search_query="+sapicifiedvidY)

        elif 'open google' in query:
            print("What You Want To Search...... ")
            speak("What You Want To Search")
            sapicifiedvidG = takeCommand().lower()
            gLink = "https://www.google.com/search?q=XXXX&rlz=1C1RXQR_enIN991IN991&sxsrf=ALiCzsY4L6rZdOM3G9kwCQQAnm3qgImgpA%3A1670267268419&ei=hEGOY5mYGaCVseMP98-ooA4&ved=0ahUKEwiZ6tq5luP7AhWgSmwGHfcnCuQQ4dUDCA8&uact=5&oq=fifa&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIJCCMQJxBGEP0BMgQIIxAnMgQIIxAnMgoILhCDARCxAxBDMggIABCxAxCDATILCAAQgAQQsQMQgwEyCAgAELEDEIMBMggIABCxAxCDATILCAAQgAQQsQMQgwEyCAgAELEDEIMBOgoIABBHENYEELADOgcIABCwAxBDOg0IABDkAhDWBBCwAxgBOg8ILhDUAhDIAxCwAxBDGAI6DAguEMgDELADEEMYAjoSCC4QxwEQ0QMQyAMQsAMQQxgCOgUIABCABDoHCAAQsQMQQzoECAAQQzoICAAQgAQQsQM6BwgjEOoCECc6BwguEOoCECc6DAgAEOoCELQCEEMYAzoPCC4Q1AIQ6gIQtAIQQxgDOgwILhDqAhC0AhBDGAM6CwguEIMBELEDEIAEOgcILhDUAhBDSgQIQRgASgQIRhgBUOQNWNMoYNcwaANwAXgDgAGCAYgBuQiSAQMwLjmYAQCgAQGwARTIARPAAQHaAQYIARABGAnaAQYIAhABGAjaAQYIAxABGAE&sclient=gws-wiz-serp"
            gLink2 = gLink.replace("XXXX",sapicifiedvidG)
            webbrowser.open(gLink2)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open all too well' in query:
            codePath ="E:\\MultiMedia\\Videos\All Too Well (10 Minute Version) (Taylors Version) (From The Vault) (Lyric Video).3gpp"
            os.startfile(codePath)

        elif 'open riot games' in query:
            codePath ="C:\\Users\\Public\\Desktop\\VALORANT.lnk"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("To whom should the email be sent?")
                emailE = takeCommand().lower()
                speak("What should I say?")
                to = emailE   
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")   

        elif 'joke' in query:
            a = pyjokes.get_joke("en","all")   
            speak(a)
        elif 'wikipedia' in query:
            speak("What to search on Wikipedia?")
            wikiVal = takeCommand().lower()
            speak('Searching Wikipedia...')
            results = wikipedia.summary(wikiVal, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'make scanner code' in query:
            speak("Enter An Link or Text For making Qr Code")    
            print("Enter An Link or Text For making Qr Code")   
            #u can also do qrLink = input("Enter Link Or Text - ") 
            qrLink = takeCommand().lower()
            qrCode(qrLink)
            speak("Your Qr Code Is Generated ,,,,,Opening QR Code")
            print("Your Qr Code Is Generated ,Opening QR Code")
            codePath = "C:\\Users\\puska\\myqr.png" #u can add ur path
            os.startfile(codePath)
        elif 'stop' in query:
            speak("Bye Bye sir, see you soon")
            break
            

