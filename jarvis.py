import pyjokes
import os
import requests
from bs4 import BeautifulSoup
import datetime
import speech_recognition as sr
from mutagen.mp3 import MP3
import json
import time
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
import cv2
from beeply.notes import *
from pytube import YouTube
import pafy
import numpy as np
from PIL import Image
import urllib.request
import re
import pyautogui
from queue import Queue
import threading
def tts(mytext):
    authenticator = IAMAuthenticator('L61r99rxsZl4wWsdvfM2XTsboYtXncJDOI-X_9waqxnu')
    text_to_speech = TextToSpeechV1(authenticator=authenticator)
    text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/b826ceb9-0db3-485a-ba4f-3f21e5933311')
    with open('hello_world.wav', 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(mytext,voice='en-GB_KateV3Voice',accept='audio/wav').get_result().content)
    os.popen(cmd="hello_world.wav",mode="r",buffering=-1)
def takeVoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    print("Recognizing...")
    try:
        query = r.recognize_google(audio, language ='en-in')
    except:
        query=""
    print(f"User said: {query}\n")
    return query
def wiki_search(kite):
    try:
        url="https://en.wikipedia.org/wiki/"
        thing=kite.replace(" ","_")
        url=url+thing
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        mytext =soup.find(id="bodyContent").find_all("p")[1].get_text()
        return(mytext)
    except:
        return("no results found")
def weather():
    city="hyderabad"
    api_key = "66c28b29bcbee3e14525e8f4774b091e"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    city_name = city
    complete_url = base_url + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
    forcast="temperature in " + city_name +" is " + str(round(current_temperature-273)) + " degrees celcius and humidity is " + str(current_humidity) + " percent and today's weather is " + str(weather_description)
    return forcast
def joke():
   return pyjokes.get_joke(language='en',category='neutral')
def date(a):
    if a==1:
        year=str(time.strftime('%d'))+"-"+str(time.strftime('%m'))+"-"+str(time.strftime('%Y'))
    if a==2:
        now = datetime.datetime.now()
        year = now.strftime("%H:%M:%S")
    if a==3:
        year=str(time.strftime('%Y'))+"-"+str(time.strftime('%m'))+"-"+str(time.strftime('%d'))
    return year
def talkibm(tm):
    authenticator = IAMAuthenticator('P6byBnjOSisAqrMFV0wNQEwCntFmtiOlOrIlh_ct1N1F')
    assistant = AssistantV2(version='2021-07-27',authenticator = authenticator)

    assistant.set_service_url('https://api.us-east.assistant.watson.cloud.ibm.com')

    response = str(assistant.create_session(assistant_id='e7d0059f-687f-442e-bb0b-b484513bde49').get_result())
    response=response.replace('{\'session_id\': \'','')
    response=response.replace('\'','')
    response=response.replace('}','')
    response = assistant.message(assistant_id='e7d0059f-687f-442e-bb0b-b484513bde49',session_id=response,input={'message_type': 'text','text': tm }).get_result()
    a=str(dict(dict(dict(response.get('output',"None")).get('generic',"none"))))
    c=str(dict(response.get('output',"None")).get('generic',"none"))
    z=a.replace('}','') + ","+" \'text\': "
    c=c.replace('[','')
    c=c.replace(']','')
    c=c.replace(z,'')
    c=c.replace('}','')
    c=c.replace('\'','')
    return (c)
"""def toneanal(text):
    authenticator = IAMAuthenticator('y2zFSczx4EffgCgolaS7yt7GvxkB-HkstIOwCQIK3Tow')
    tone_analyzer = ToneAnalyzerV3(
        version='2021-07-29',
        authenticator=authenticator
    )
    tone_analyzer.set_service_url('https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/94270624-9a40-417b-a439-f88e879bba4f')
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    a=list(str(dict(tone_analysis.get('document_tone',"None")).get('tones',"None")).replace("{","").replace("}","").replace("[","").replace("]","").replace("\'","").replace("\"","").replace("tone_id","").replace(":","").replace("tone_name","").replace("score","").split(','))
    try:
        return(a[1])
    except:
        return("none")"""
def eyes(cam):
    eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'harrcascade_eye.xml')
    gray=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
    faces=eye_cascade.detectMultiScale(gray,1.3,5)
    x,y,w,h=faces
    if x*y*w*h>0:
        return True
    else:
        return False
def youtube(a):
    yt = YouTube(a)  
    video = yt.streams.filter(only_audio=True).first()  
    out_file = video.download(output_path='.')  
    base, ext = os.path.splitext(out_file)
    os.rename(out_file, 'song.mp3')
    videoy = pafy.new(a)
    os.popen(cmd="song.mp3",mode="r",buffering=-1)
    time.sleep((videoy.length)+2)
    os.remove('song.mp3')
def save_face(a):    
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_id = a
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    time.sleep(2)
    count = 0
    #start detect your face and take 30 pictures
    while(True):

        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1# Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff
        if k == 27:
            break
        elif count >= 100:
            break

    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
def train():
    path = 'C:/Users/Rithik/prog/dataset'

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("C:/Users/Rithik/prog/haarcascade_frontalface_default.xml")

    # function to get the images and label data
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples,ids
    print ("\n [INFO] Training faces. It will take a few seconds.")
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))
    recognizer.write('C:/Users/Rithik/prog/trainer.yml') 
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
def recog(q):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('C:/Users/Rithik/prog/trainer.yml')
    cascadePath = "C:/Users/Rithik/prog/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX
    id = 1
    names = ['','Rithik','Preethika','Sneha']
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) 
    cam.set(4, 480)
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret, img =cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )
        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 85):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            q.put(id)
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        cv2.imshow('camera',img) 
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    print("\nExiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
def songs(sk):
    sk=sk.replace(" ","+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+sk)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    youtube("https://www.youtube.com/watch?v="+video_ids[0])
def search(s,a):
    b=s.find(a)
    if b!=-1:
        s=s.replace(s[b:b+len(a)+1],"")
        return(s)
    else:
        return(str(b))
def search_name(s,a):
    b=s.find(a)
    if b!=-1:
        s=s.replace(s[b:len(s)],"")
        return(s)
    else:
        return(str(b))
def friday(w):
    b=0
    t=False
    delta=["mummy","daddy","chinnu","praneeth","vaishu","preethika"]
    while True:
        pbm=w.get()
        a=str(takeVoice().lower())
        b=a.find("friday")
        if a=="":
            continue
        elif b!=-1 or t:
            if b!=-1:
                a=a.replace(a[0:b+7],"")
            t=True
            for i in delta:
                alpha=search_name(a,i)
                if alpha!="-1":
                    t=False
                    a=alpha
                    break
        if t:
            print("|"+a+"|")
            if search(a,"play")!="-1":
                songs(search(a,"play"))
            elif search(a,"define")!="-1":
                tts(wiki_search(search(a,"define")))
            if search(a,"youtube")!="-1":
                songs(search(a,"youtube"))
            elif search(a,"wiki")!="-1":
                tts(wiki_search(search(a,"wiki")))
            elif search(a,"wikipedia")!="-1":
                tts(wiki_search(search(a,"wikipedia")))
            elif search(a,"joke")!="-1":
                tts(joke())
            elif search(a,"date")!="-1":
                tts(date(1))
            elif search(a,"time")!="-1":
                tts(date(2))
            elif search(a,"shutdown")!="-1":
                pyautogui.press('esc')
                break
            elif search(a,"weather")!="-1":
                tts(weather())
            else:
                z=talkibm(a)
                if z!="9":
                    tts(z)
q=Queue()
t1 = threading.Thread(target=friday, args=(q,))
t2 = threading.Thread(target=recog, args=(q,))
t1.start()
t2.start()