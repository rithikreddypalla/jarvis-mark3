import pyautogui
from queue import Queue
import threading
from jarvis_modules.voice import take_voice
from jarvis_modules.tts import tts
from jarvis_modules.web import wiki_search, joke, date
from jarvis_modules.weather import weather
from jarvis_modules.ibm_assistant import talkibm
from jarvis_modules.face import save_face, train, recog
from jarvis_modules.media import songs
from jarvis_modules.utils import search, search_name

def friday(w):
    # Main assistant loop
    t = False
    delta = ["mummy", "daddy", "chinnu", "praneeth", "vaishu", "preethika"]
    while True:
        pbm = w.get()
        a = str(take_voice().lower())
        b = a.find("friday")
        if a == "":
            continue
        elif b != -1 or t:
            if b != -1:
                a = a.replace(a[0:b + 7], "")
            t = True
            for i in delta:
                alpha = search_name(a, i)
                if alpha != "-1":
                    t = False
                    a = alpha
                    break
        if t:
            print(f"|{a}|")
            if search(a, "play") != "-1":
                songs(search(a, "play"))
            elif search(a, "define") != "-1":
                tts(wiki_search(search(a, "define")))
            if search(a, "youtube") != "-1":
                songs(search(a, "youtube"))
            elif search(a, "wiki") != "-1":
                tts(wiki_search(search(a, "wiki")))
            elif search(a, "wikipedia") != "-1":
                tts(wiki_search(search(a, "wikipedia")))
            elif search(a, "joke") != "-1":
                tts(joke())
            elif search(a, "date") != "-1":
                tts(date(1))
            elif search(a, "time") != "-1":
                tts(date(2))
            elif search(a, "shutdown") != "-1":
                pyautogui.press('esc')
                break
            elif search(a, "weather") != "-1":
                tts(weather())
            else:
                z = talkibm(a)
                if z != "9":
                    tts(z)

# --- MAIN ---
if __name__ == "__main__":
    q = Queue()
    t1 = threading.Thread(target=friday, args=(q,))
    t2 = threading.Thread(target=recog, args=(q,))
    t1.start()
    t2.start()