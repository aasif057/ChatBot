import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import psutil
import pyautogui
import openai
from langdetect import detect
import os

api_key = os.environ['JARVIS']


class ChatBot:
    def __init__(self):
        self.engine=pyttsx3.init('sapi5')
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)
        openai.api_key = api_key
        self.r=sr.Recognizer() 
    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()
    def filter_command(self,command):
        if "Jarvis" in command:
            command=command.replace("Jarvis","")
            return command
        else:
            return command
    def take_commands(self):
        
        with sr.Microphone() as Source:
            #self.speak("please tell your query sir?")
            print("Listening...")
            self.r.pause_threshold=1
            audio=self.r.listen(source = Source, timeout= None, phrase_time_limit= 5)
        try:
            #self.speak("Recognising...")
            print("Recognising...")
            command_unf=self.r.recognize_google(audio,language='en-in')
            #print(f"User asked for  {command_unf}")
            command=self.filter_command(command_unf)
            print(f"User asked for  {command}")
            return command
        except Exception as e:
            self.speak("Say That Again Please..")
            command = self.take_commands()
            return command

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = user_input,
            max_tokens= 4000,
            temperature = 0.5
        ).choices[0].text
        return response
    
# if __name__ == "__main__":
#     chatbot = ChatBot()
#     response = chatbot.get_response("Tell me about Wipro")
#     print(response)
