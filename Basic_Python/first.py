import pyjokes
import pyttsx3
print("hello world")
joke = pyjokes.get_joke()
print(joke)
engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()

#comments
# simple commet
'''ksdmcks'''
# mvdmf
# sdvksv
# dsv


import os
dirpath='/'
content = os.listdir(dirpath)

for item in content:
    print(item)