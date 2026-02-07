import requests
from bs4 import BeautifulSoup
import pyjokes
import time
import datetime

def wiki_search(query):
    try:
        url = "https://en.wikipedia.org/wiki/" + query.replace(" ", "_")
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        mytext = soup.find(id="bodyContent").find_all("p")[1].get_text()
        return mytext
    except Exception:
        return "no results found"

def joke():
    return pyjokes.get_joke(language='en', category='neutral')

def date(a):
    if a == 1:
        return time.strftime('%d-%m-%Y')
    if a == 2:
        return datetime.datetime.now().strftime("%H:%M:%S")
    if a == 3:
        return time.strftime('%Y-%m-%d')
