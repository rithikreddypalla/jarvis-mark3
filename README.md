# Jarvis Mark-3

Jarvis Mark-3 is a personal assistant system that combines voice recognition, face recognition, web search, jokes, music playback, and more. It uses IBM Watson for text-to-speech and conversation, OpenCV for face recognition, and various APIs for weather and jokes.

## Features
- Voice command recognition (speech-to-text)
- Text-to-speech responses (IBM Watson)
- Wikipedia and web search
- Weather information (OpenWeatherMap)
- Jokes (pyjokes)
- YouTube music playback
- Face recognition and training (OpenCV)
- Multi-threaded: runs face recognition and assistant loop in parallel

## Setup
1. Install dependencies:
	- `pip install -r requirements.txt` (see below for main packages)
2. Set up API keys as environment variables:
	- `IBM_TTS_API_KEY`, `IBM_TTS_URL` (IBM Watson Text-to-Speech)
	- `IBM_ASSISTANT_API_KEY`, `IBM_ASSISTANT_URL`, `IBM_ASSISTANT_ID` (IBM Watson Assistant)
	- `OPENWEATHER_API_KEY` (OpenWeatherMap)
3. Download required Haar cascades (e.g., `haarcascade_frontalface_default.xml`) and place in the project directory
4. Run the assistant: `python jarvis.py`

## Usage
- Speak commands after the assistant is listening
- Supported commands: play music, tell a joke, get weather, Wikipedia search, date/time, etc.
- Face recognition runs in parallel for user identification

## Security Notes
- **Do not** hardcode API keys in the code. Use environment variables or a config file excluded from version control.
- Webcam and microphone access are required; use with trusted hardware only.

## Main Dependencies
- `opencv-python`, `pytube`, `pafy`, `pyjokes`, `mutagen`, `speechrecognition`, `ibm-watson`, `beeply`, `numpy`, `Pillow`, `pyautogui`, `requests`, `bs4`

## Author
Rithik (2026)

---
*This is a fallback and experimental version of the Jarvis personal assistant system.*
