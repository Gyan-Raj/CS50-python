import cowsay
import pyttsx3

engine = pyttsx3.init()
this = "This was all about python CS50"
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
