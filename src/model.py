import datetime
import logging

import speech_recognition as sr
import pyttsx3
import wikipedia
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
# need to run python -m spacy download en
# May need to run as admin

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)

# Instantiating the speech enginer to be used, Sapi5 is a Microsoft TTS
speech_engine = pyttsx3.init('sapi5')
voices = speech_engine.getProperty('voices')
speech_engine.setProperty('voice', voices[0].id)


def train_bot():
    my_bot = ChatBot(name='PyBot',
                     read_only=True,
                     response_selection=get_random_response,
                     logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                     'chatterbot.logic.BestMatch'])
    corpus_trainer = ChatterBotCorpusTrainer(my_bot)
    logger.info('Training Bot')
    corpus_trainer.train('chatterbot.corpus.english')
    return my_bot


chat_bot = train_bot()


class SpeechBot:
    def __init__(self, speech_engine=speech_engine, chat_bot=chat_bot):
        self.speech = speech_engine
        self.recognizer = sr
        self.chat_bot = chat_bot

    def speak(self, text):
        """Function to output speech from text"""
        self.speech.say(text)
        self.speech.runAndWait()

    def greeting(self):
        """Function to greet user"""
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.speak('Hello, Good Morning')
        elif 12 <= hour <= 18:
            self.speak('Hello, Good Afternoon')
        else:
            self.speak('Hello, Good Evening')

    def say_time(self):
        text_time = datetime.datetime.now().strftime('%H:%M:%S')
        self.speak(f'The time is {text_time}')

    def wiki_info(self, topic):
        self.speak('Let me look into that..')
        topic = topic.replace('wikipedia', '')
        results = wikipedia.summary(topic, sentences=3)
        self.speak('So what I found out is that..')
        logger.info(results)
        self.speak(results)

    def listen_command(self):
        recognizer = self.recognizer.Recognizer()
        with self.recognizer.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source)

            try:
                statement = recognizer.recognize_google(audio, language='en-SG')
                logger.info(f'user said: {statement}')
            except Exception:
                return 'None'
            return statement

    def chatbot_response(self, statement):
        return self.chat_bot.get_response(statement)

    def start(self):
        self.greeting()
        while True:
            statement = self.listen_command().lower()
            if statement == 'none':
                continue

            if 'bye' in statement or 'quit' in statement:
                self.speak('See you again!')
                break

            elif 'time' in statement:
                self.say_time()

            elif 'wikipedia' in statement:
                self.wiki_info(statement)
            else:
                self.speak(self.chatbot_response(statement))


class TextBot:
    def __init__(self, chat_bot=chat_bot):
        self.chat_bot = chat_bot

    @staticmethod
    def text_respond(text):
        """Function to output speech from text"""
        print(f'Bot: {text}')
        return text

    def greeting(self):
        """Function to greet user"""
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.text_respond('Hello, Good Morning')
        elif 12 <= hour <= 18:
            self.text_respond('Hello, Good Afternoon')
        else:
            self.text_respond('Hello, Good Evening')

    def say_time(self):
        text_time = datetime.datetime.now().strftime('%H:%M:%S')
        return str(self.text_respond(f'The time is {text_time}'))

    def wiki_info(self, topic):
        self.text_respond('Let me look into that..')
        topic = topic.replace('wikipedia', '')
        results = wikipedia.summary(topic, sentences=3)
        self.text_respond('So what I found out is that..')
        logger.info(results)
        return str(self.text_respond(results))

    def chatbot_response(self, statement):
        return str(self.chat_bot.get_response(statement))

    def start(self):
        self.greeting()
        while True:
            statement = input('Type to me...').lower()
            if statement == 'none':
                continue

            if 'bye' in statement or 'quit' in statement:
                self.text_respond('See you again!')
                break

            elif 'time' in statement:
                self.say_time()

            elif 'wikipedia' in statement:
                self.wiki_info(statement)
            else:
                self.text_respond(self.chatbot_response(statement))

    def start_api(self, msg):
        self.greeting()

        statement = msg.lower()
        if 'bye' in statement or 'quit' in statement:
            response = 'See you again!'

        elif 'time' in statement:
            response = self.say_time()

        elif 'wikipedia' in statement:
            response = self.wiki_info(statement)

        else:
            response = self.chatbot_response(statement)

        return response


if __name__ == '__main__':
    speech_bot = TextBot()
    speech_bot.start()
