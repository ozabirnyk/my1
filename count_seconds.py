import time
import pyttsx3

engine = pyttsx3.init()
max_minutes = 10
step_seconds = 5

def say_seconds(something):    
    start_time = time.time()
    engine.say(something)
    engine.runAndWait()
    time.sleep(step_seconds - (time.time() - start_time))

for minutes in range(max_minutes + 1):
    if minutes == 0:
        minutes_str = ""
        say_seconds("Start")
    else:
        if minutes == 1:
            minutes_str = "1 minute"
        if minutes > 1:
            minutes_str = str(minutes) + " minutes"
        say_seconds(minutes_str)
    for seconds in range(step_seconds, 60, step_seconds):
        say_seconds(minutes_str + " " + str(seconds) + " seconds")

engine.say(str(max_minutes) + " minutes")
engine.runAndWait()
