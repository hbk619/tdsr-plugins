#!/usr/bin/env python3
import os
import sys
import logging
import io
from elevenlabs import Voice, VoiceSettings, generate, play

api_key = os.getenv('ELEVENLABS_API')
voice_id = os.getenv('VOICE_ID')
logger = logging.getLogger("tdsr")
logger.addHandler(logging.NullHandler())
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('hbk619-plugins.log')
fh.setFormatter(formatter)
logger.addHandler(fh)

if os.getenv('HBK619_DEBUG'):
    logger.setLevel(logging.DEBUG)


def main():
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    line = input_stream.readline()
    while line:
        line = line.strip('\n')
        if line[0] == u"s" or line[0] == "l":
            l = line[1:].replace('[[', ' ')
            l = l.replace(u'\u23ce', ' ')
            say(l)
        elif line[0] == u"x":
            logger.debug("Got weird character")
        elif line[0] == u"r":
            logger.debug("Got change rate")
        elif line[0] == u"v":
            logger.debug("Got change volume")
        elif line[0] == "V":
            logger.debug("Got change voice")

        line = input_stream.readline()


def say(text):
    if not text:
        return

    logger.debug("saying " + text)

    audio = generate(
        text=text,
        api_key=api_key,
        voice=Voice(
            voice_id=voice_id,
            settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        )
    )

    play(audio)


if __name__ == '__main__':
    main()
