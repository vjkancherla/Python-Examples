#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import datetime

def main():
    webpage = requests.get('http://www.theguardian.com/uk')
    soup = BeautifulSoup(webpage.text, "html.parser")
    today = datetime.date.today()
    fileName = 'guardian_headlines_'+str(today)+'.txt'

    print (webpage.text)

    for title in soup.find_all(class_="fc-item__title"):
        with open(fileName, 'a') as file:
           file.write(title.text.replace("\n", " ").strip() + '\n')

main()
