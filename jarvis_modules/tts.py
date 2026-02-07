import os
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

IBM_TTS_API_KEY = os.getenv('IBM_TTS_API_KEY', 'YOUR_TTS_API_KEY')
IBM_TTS_URL = os.getenv('IBM_TTS_URL', 'YOUR_TTS_URL')

def tts(mytext):
    """Text-to-speech using IBM Watson."""
    authenticator = IAMAuthenticator(IBM_TTS_API_KEY)
    text_to_speech = TextToSpeechV1(authenticator=authenticator)
    text_to_speech.set_service_url(IBM_TTS_URL)
    with open('hello_world.wav', 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(mytext, voice='en-GB_KateV3Voice', accept='audio/wav').get_result().content)
    os.system('aplay hello_world.wav')
