
import pyttsx3


engine = pyttsx3.init()

text = "Would you like to play a game?"

engine.say(text)
engine.runAndWait()
