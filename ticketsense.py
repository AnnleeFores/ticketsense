#ticketsense.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from time import sleep

#Enter BookMyShow and TicketNew theater links here inside single quotes seperated by comma - Make sure to remove date from the end

links = ['https://in.bookmyshow.com/buytickets/carnival-downtown-thalassery/cinema-thay-CDTH-MT',
'https://in.bookmyshow.com/buytickets/aura-cinema-mattannur/cinema-matt-ACMR-MT',
'https://www.ticketnew.com/Carnival-Downtown--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/12539',
'https://www.ticketnew.com/Liberty-Paradise-Complex--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/1203',
'https://www.ticketnew.com/Mallika-Plex-Dolby-Atmos--Calicut-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/10264',
'https://in.bookmyshow.com/buytickets/carnival-arti-suncity-mall-barasat/cinema-kolk-ACBK-MT',
'https://in.bookmyshow.com/buytickets/pvr-lulu-kochi/cinema-koch-PVKC-MT'
]


browser = webdriver.Firefox() #opens web browser -> firefox

# DATE of booking
main_DATE = '16' 
Mon = '12'
Year = '2021'

filmname = 'spider' #first word of film name


def senseticket_bms(arg):
    
    browser.get(arg + f'/{Year}{Mon}{main_DATE}')
    try:
        date = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'showDates')))

        venue = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.venue-heading')))

        showsB = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.nameSpan')))

        p = (date.text[0:2])
        if p == main_DATE:
            print(f'Bookmyshow: {venue.text} {main_DATE}th Dec slot opened!!!')
            for show in showsB:
                print(f'Ticket booking started for {show.text}')
                if filmname in show.text.lower():
                    print('Found Spidey')
            print('-'.center(80, '-'))
        else:
            print(f'Bookmyshow: {venue.text} not yet open')
            print('-'.center(80, '-'))
    except:
        print('Was not able to find an element with that name.')
        print('-'.center(80, '-'))


def senseticket_tnew(arg):
    browser.get(arg + f'/202112{main_DATE}')
    try:
        venue = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="divTheatreInfo"]/h2')))

        showsT = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'tn-entity-details')))

        date = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'li.ui-tabs-tab.ui-corner-top.ui-state-default.ui-tab.ui-tabs-active.ui-state-active')))

        q = (date.text[4:])
        if q == main_DATE:
            print(f'Ticket New: {venue.text} {main_DATE}th Dec slot opened!!!')
            for show in showsT[1:]:
                print(f'Ticket booking started for {show.text}')
                if filmname in show.text.lower():
                    print('Found Spidey')
            print('-'.center(80, '-'))
        else:
            print(f'Ticket New: {venue.text} not yet open')
            print('-'.center(80, '-'))

    except:
        print(f'Ticket New:{venue.text} Was not able to find an element with that name.')
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

while True:
    loopy(bms_links)
    loopy(tnew_links)
    sleep(30)

""" loopy(bms_links)
loopy(tnew_links) """


browser.quit()
