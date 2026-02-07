import speech_recognition as sr

def take_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    print("Recognizing...")
    try:
        query = r.recognize_google(audio, language='en-in')
    except Exception:
        query = ""
    print(f"User said: {query}\n")
    return query
