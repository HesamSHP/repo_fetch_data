import requests
from bs4 import BeautifulSoup
import pandas as pd
from threading import Thread
from time import sleep

def check_fee():
    counter = 0
    
    while True:
        page = requests.get("https://www.tgju.org/%d9%82%db%8c%d9%85%d8%aa-%d8%af%d9%84%d8%a7%d8%b1")
        soup = BeautifulSoup(page.content, 'html.parser')
        
        table = soup.findChildren('table')[0]
        tr = table.findChildren('tr')
        
        dollar_fee = tr[1].findChildren('td')[0].get_text()
        fetch_time = tr[1].findChildren('td')[4].get_text()

        if (counter % 10 == 0):
            print ("          %s        %s" % ('fetch time', 'dollar fee'))
        
        counter+=1
        print ("%5d        %s        %s" % (counter, fetch_time, dollar_fee))

        sleep(5)
        


if __name__ == "__main__":
    thread = Thread(target=check_fee)
    thread.start()