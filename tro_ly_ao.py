import speech_recognition
import pyttsx3
from datetime import date,datetime
today = date.today()
time=datetime.today()

robot_brain=""
robot_ear=speech_recognition.Recognizer()
engine = pyttsx3.init()
while True:
    with speech_recognition.Microphone() as mic:

        print("Robot : I'm listening")
        audio= robot_ear.listen(mic)
    try:
        you=robot_ear.recognize_google(audio)
    except:
        you="..............."
    print("You :"+you)
    if you=="":
        robot_brain="I can't hear you , try again "

    elif "hello" in you:
        robot_brain="Helo Nguyen Dongggg ... I amm Leooo"
    elif "today" in you:
        robot_brain=today.strftime("%B %d, %Y")
    elif "time" in you:
        robot_brain=time.strftime("%H hours %M minutes %S seconds")
    elif "fly" in you:
        robot_brain="you wan't fly ... come on 1900"
    elif "bye" in you:
        robot_brain="Bye nguyennn dongggg"
        print(robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
        break
    else:
        robot_brain="I'm fine thank you and you ..."
    print(robot_brain)

    engine.say(robot_brain)
    engine.runAndWait()