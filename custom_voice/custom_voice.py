import os
from elevenlabs import Voice, VoiceSettings, generate, play
from ..pytest_parser import parse_pytest

api_key = os.getenv('ELEVENLABS_API')
voice_id = os.getenv('VOICE_ID')


def parse_output(lines):

    pytest_results = parse_pytest.parse_output(lines)

    audio = generate(
        text=" ".join(pytest_results),
        api_key=api_key,
        voice=Voice(
            voice_id=voice_id,
            settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        )
    )

    play(audio)

    return []

