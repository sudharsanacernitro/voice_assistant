import pyttsx3
import time
import datetime
import pywhatkit
import wikipedia as wiki
import speech_recognition as sr
import os
from playsound import playsound
import sqlite3
from h import hai
l=hai()
listener=sr.Recognizer()
engine=pyttsx3.init()
conn=sqlite3.connect("contact.db")
cursor=conn.cursor()
#s="""CREATE TABLE contact3(sno INTEGER PRIMARY KEY,name VARCHAR(30),phone VARCHAR(15));"""
#cursor.execute(s)
'''s= [
    ("1","saran","+918438213467"),
    ("2","sakthi","+918508785621"),
    ("3","shiva","+918778733212"),
    ("4","vibudhesh","+919626513782"),
    
    ("5","sabi","+919025604172"),
    ("6","baby","+919345623077"),
    (7,"appa","+919994995008")
]'''
#s=[("8","me","+919600475008")]
#cursor.executemany("INSERT INTO contact3 VALUES (?,?,?);",s)
#conn.commit()
'''cursor.execute("UPDATE contact3 SET name='shakthi' where sno=2")
conn.commit()
conn.close()'''
l=["what","who","tell"]
a=0
h = datetime.datetime.now().strftime('%H')
m = datetime.datetime.now().strftime('%M')
def au():
    if (auth()==1):
        if(convo(h)<12):
            talk("good morning")
        else:
            talk("how was your day ")
            l=listen()

        time.sleep(2)
        talk("what can i do for you")

    else:
        a=1
def start():
    try:
        command = listen()
        if "wake up" in command:
            talk("i am in online sir")
        if "play" in command:
           play()
        if "how" in command:
            talk("do you want to continue with google or youtube")
            c=listen()
            print(command)
            if "youtube" in c:
                pywhatkit.playonyt(command)
       #Z if "show me the files" in
        if "time" in command:
            if "what" in command:
                command = command.replace("what", " ")
            time = datetime.datetime.now().strftime('%H %M %p')
            talk("sir the time is" + time)
        for i in l:
            if i in command:
                command = command.replace(i, " ")
                print("searching")
                talk("searching")
                info = wiki.summary(command, 2)
                talk(info)
        if "text" in command:
            h = datetime.datetime.now().strftime('%H')
            m = datetime.datetime.now().strftime('%M')
            h = convo(h)
            m = convo(m)
            command = command.replace("text to ", "")
            print(command)
            cursor.execute("SELECT phone FROM contact3 WHERE name=:c", {'c': command})
            r = cursor.fetchone()
            print(r[0])
            talk("what do you want to convey")
            c = listen()
            pywhatkit.sendwhatmsg(r[0], c, h, m + 2, 15, True, 2)

    except:
        pass
def msg(command):
    h = datetime.datetime.now().strftime('%H')
    m = datetime.datetime.now().strftime('%M')
    h = convo(h)
    m = convo(m)
    command = command.replace("text to ", "")
    print(command)
    cursor.execute("SELECT phone FROM contact3 WHERE name=:c", {'c': command})
    r = cursor.fetchone()
    print(r[0])
    talk("what do you want to convey")

    pywhatkit.sendwhatmsg(r[0],"hai", h, m + 2, 15, True, 2)
def play():
    talk("do you want to continue with musics or youtube")
    c = listen()
    print(c)
    song = c.replace("play", " ")
    talk("playing " + song)
    if "music" in c:
        print(os.getcwd())
        folder = r"C:\\Users\\sudharsan\\Music"
        os.chdir(folder)
        print(os.getcwd())
        a = 0
        b = 0
        for f in os.listdir():
            if f == "desktop.ini":
                continue
            playsound(f)
    os.chdir(r"C:\\Users\\sudharsan\\PycharmProjects\\pythonProject6")
    if ("youtube" in c):
        pywhatkit.playonyt(song)
def listen():
    try:
        print("listening....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        return command
    except:
        pass
def convo(h):
    l=[]
    for i in h:
        j=int(i)
        l.append(j)
        d=0
    for i in range(0,2):
        d=(d*10)+l[i]
    return d

def talk(line):
    engine.say(line)
    engine.runAndWait()
def auth():
    command=listen()
    if "wake up arsenal" in command:
        print("Booting...")
        talk("Booting")
        time.sleep(3)
        talk("please tell your password sir")
        command=listen()
        return 1
        if "sam" in command:
            talk("hello sir")
            return 1
        else:
            talk("wrong password")
            return 0
with sr.Microphone() as source:
    au()
    if (a == 0):
        while True:
            start()


