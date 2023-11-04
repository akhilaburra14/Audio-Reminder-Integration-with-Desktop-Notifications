import pandas as pd
import datetime
from plyer import notification
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def notification1(title,msg):
    notification.notify(
        title=title,
        message=msg,

        timeout=8
    )


df = pd.read_excel("C:\\Users\\Anusha Burra\\Desktop\\Python project files\\Remainder sheet1.xlsx")
today = datetime.datetime.now().strftime("%d-%m")

for index, item in df.iterrows():
    bd = item["date"]
    if today == bd:

        a = item["Remainder"]
        notification1("notifying You", ""+a+"")
        speak("Akhila,notifying You "+a+"")
