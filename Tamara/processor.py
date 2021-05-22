#!/usr/bin/env python3
from gtts import gTTS
from string import ascii_letters, digits

import playsound
import random
import speech_recognition as sr


class TamaraProcessor(object):
    """docstring for TamaraProcessor."""

    def __init__(self):
        super(TamaraProcessor, self).__init__()
        self.chars = ascii_letters + digits

    def gen_filename(self) -> str:
        # return value
        filename = ''

        length = random.randint(5, 10)
        for _ in range(length):
            char = ''
            char += random.choice(self.chars)
            filename += str(char)
        return filename

    def speak(self, text):
        filename = f'tmp/voices/{self.gen_filename()}.mp3'
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound.playsound(filename)

    # TODO: Fix PyAudio problem
    # TODO: Sound processing does not work.
    # Try on different machine.
    @staticmethod
    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""
            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                # print(e)
                pass

        return said
