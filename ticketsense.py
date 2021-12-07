from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

#Enter BookMyShow and TicketNew theater links here inside single quotes seperated by comma

links = ['https://in.bookmyshow.com/buytickets/carnival-downtown-thalassery/cinema-thay-CDTH-MT/20211216',
'https://in.bookmyshow.com/buytickets/aura-cinema-mattannur/cinema-matt-ACMR-MT/20211216',
'https://www.ticketnew.com/Carnival-Downtown--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/12539/20211216',
'https://www.ticketnew.com/Liberty-Paradise-Complex--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/1203/20211216',
'https://www.ticketnew.com/Mallika-Plex-Dolby-Atmos--Calicut-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/10264/20211216',
'https://in.bookmyshow.com/buytickets/carnival-arti-suncity-mall-barasat/cinema-kolk-ACBK-MT/20211216'
]


browser = webdriver.Firefox() #opens web browser -> firefox

main_DATE = '16' # DATE of booking


def senseticket_bms(arg):
    
    browser.get(arg)
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
            print('-'.center(80, '-'))
        else:
            print(f'Bookmyshow: {venue.text} not yet open')
            print('-'.center(80, '-'))
        return showsB
    except:
        print('Was not able to find an element with that name.')
        print('-'.center(80, '-'))


def senseticket_tnew(arg):
    browser.get(arg)
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
            print('-'.center(80, '-'))
        else:
            print(f'Ticket New: {venue.text} not yet open')
            print('-'.center(80, '-'))
        return showsT
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

loopy(bms_links)
loopy(tnew_links)

browser.quit()
