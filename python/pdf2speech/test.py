#!/bin/env python3
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voix="french"
boucle = True
#print(voices.name)
if boucle is False:
   for voice in voices:
      print(f"voice name: {voice.name}, voice id : {voice.id}, genre: {voice.gender}")
      engine.setProperty('voice', voice.id)
      engine.say('Bonjour comment allez vous ?')
      engine.runAndWait()
   #engine.say('The quick brown fox jumped over the lazy dog.')

#engine.setProperty('gender', "female")
engine.setProperty('voice', voix)
print(dir(engine))
print(f"voice : {engine.getProperty('voice')}")
engine.say(u'Bonjour comment allez vous ?')
engine.runAndWait()