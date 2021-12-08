#ticketsense.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import os
import telebot
from dotenv import load_dotenv


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service




#Enter BookMyShow and TicketNew theater links here inside single quotes seperated by comma - Make sure to remove date from the end

links = [
    'https://in.bookmyshow.com/buytickets/carnival-downtown-thalassery/cinema-thay-CDTH-MT',
    'https://in.bookmyshow.com/buytickets/aura-cinema-mattannur/cinema-matt-ACMR-MT',
    'https://www.ticketnew.com/Carnival-Downtown--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/12539',
    'https://www.ticketnew.com/Liberty-Paradise-Complex--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/1203',
    'https://www.ticketnew.com/Mallika-Plex-Dolby-Atmos--Calicut-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/10264',
    'https://in.bookmyshow.com/buytickets/carnival-arti-suncity-mall-barasat/cinema-kolk-ACBK-MT',
    'https://in.bookmyshow.com/buytickets/pvr-lulu-kochi/cinema-koch-PVKC-MT',
    'https://www.ticketnew.com/Apsara-Theatre-4K--Calicut-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/10515',
    'https://www.ticketnew.com/Crown-Theatre-Dolby-Atmos--Calicut-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/213'
]

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("-headless")
chrome_options.add_argument("--disable-dev-shm-usage")


try:
  ser = Service('./chromedriver')
  browser = webdriver.Chrome(service=ser,options=chrome_options)  #opens web browser -> firefox
except:
  browser = webdriver.Chrome(options=chrome_options)  #opens web browser -> firefox


# Date of booking

DATE = '16'
MON = '12'
YEAR = '2021'

filmname = 'spider'  #first word of film name

#Telegram bot code
load_dotenv()

API_KEY = os.getenv('API_KEY')
USER_ID = os.getenv('USER_ID')
bot = telebot.TeleBot(API_KEY)

def message(msg):
    bot.send_message(USER_ID, msg)


def senseticket_bms(arg):

    browser.get(arg + f'/{YEAR}{MON}{DATE}')
    try:
        date = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'showDates')))

        venue = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a.venue-heading')))

        showsB = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, 'a.nameSpan')))

        po = re.compile(r"\d\d")
        pp = po.search(date.text)
        p = pp.group()

        if p == DATE:
            print(f'Bookmyshow: {venue.text} {DATE}th Dec slot opened!!!')
            for count, show in enumerate(showsB, start=1):
                print(count, f'- Ticket booking started for {show.text}')
                if filmname in show.text.lower():
                    print(f'Found Spidey - {arg}/{YEAR}{MON}{DATE}')
                    message(f'Found Spidey - {arg}/{YEAR}{MON}{DATE}')

            print('-'.center(80, '-'))
        else:
            print(f'Bookmyshow: {venue.text} not yet open')
            print('-'.center(80, '-'))
    except:
        print('Bookmyshow: Was not able to find an element with that name.')
        print('-'.center(80, '-'))


def senseticket_tnew(arg):
    browser.get(arg + f'/{YEAR}{MON}{DATE}')
    try:
        venue = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="divTheatreInfo"]/h2')))

        showsT = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'tn-entity-details')))

        date = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                'li.ui-tabs-tab.ui-corner-top.ui-state-default.ui-tab.ui-tabs-active.ui-state-active'
            )))

        # q = (date.text[4:])

        qo = re.compile(r"\d\d")
        qp = qo.search(date.text)
        q = qp.group()

        if q == DATE:
            print(f'Ticket New: {venue.text} {DATE}th Dec slot opened!!!')
            for count, show in enumerate(showsT[1:], start=1):
                print(count, f'- Ticket booking started for {show.text}')
                if filmname in show.text.lower():
                    print(f'Found Spidey - {arg}/{YEAR}{MON}{DATE}')
                    message(f'Found Spidey - {arg}/{YEAR}{MON}{DATE}')
            print('-'.center(80, '-'))
        else:
            print(f'Ticket New: {venue.text} not yet open')
            print('-'.center(80, '-'))

    except:
        print(f'Ticket New: Was not able to find an element with that name.')
        print('-'.center(80, '-'))


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def loopy(argu):
    if bms_links == argu:
        print('\n')
        print('Starting - BookMyShow'.center(80, '-'))
        print('')
        for i in argu:
            senseticket_bms(i)
    else:
        print('\n')
        print('Starting - Ticket New'.center(80, '-'))
        print('')
        for i in argu:
            senseticket_tnew(i)


links.sort()

liststr = listToString(links)

mo = re.compile(r"bookmyshow")
regexelem = mo.findall(liststr)
lenvalue = len(regexelem)

bms_links = links[:lenvalue]
tnew_links = links[lenvalue:]

loopy(bms_links)
loopy(tnew_links)
