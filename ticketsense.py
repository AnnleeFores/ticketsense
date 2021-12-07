from selenium import webdriver
import time
import re

#Enter BookMyShow and TicketNew theater links here inside single quotes seperated by comma

links = ['https://in.bookmyshow.com/buytickets/carnival-downtown-thalassery/cinema-thay-CDTH-MT/20211216',
'https://in.bookmyshow.com/buytickets/aura-cinema-mattannur/cinema-matt-ACMR-MT/20211216',
'https://www.ticketnew.com/Carnival-Downtown--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/12539/20211216',
'https://www.ticketnew.com/Liberty-Paradise-Complex--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/1203/20211216',
'https://www.ticketnew.com/Mallika-Plex-Dolby-Atmos--Calicut-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/10264/20211216'
]


browser = webdriver.Firefox() #opens web browser -> firefox

DATE = '16'


def senseticket_bms(arg):
    
    browser.get(arg)
    try:
        date = browser.find_element_by_id('showDates')
        venue = browser.find_element_by_css_selector('a.venue-heading')
        shows = browser.find_elements_by_css_selector('a.nameSpan')
        p = (date.text[0:2])
        if p == DATE:
            print(f'Bookmyshow: {venue.text} 16th Dec slot opened!!!')
            for show in shows:
                print(f'Ticket booking started for {show.text}')
            print('')
        else:
            print(f'Bookmyshow: {venue.text} not yet open')
            print('')
        return shows
    except:
        print('Was not able to find an element with that name.')
        print('')


def senseticket_tnew(arg):
    browser.get(arg)
    try:
        elem = browser.find_element_by_css_selector('li.ui-tabs-tab.ui-corner-top.ui-state-default.ui-tab.ui-tabs-active.ui-state-active')
        q = (elem.text[4:])
        print(f'{q} Dec')
        if q == '16':
            print('Ticket New: Spidey day slot opened!!!')
        else:
            print('Ticket New: not yet open')
        return q
    except:
        print('Was not able to find an element with that name.')


def listToString(s):
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1

    
def loopy(argu):
    if bms_links == argu:
        for i in argu:
            senseticket_bms(i)
            time.sleep(5)
    else:
        for i in argu:
            senseticket_tnew(i)
            time.sleep(5)


links.sort()

liststr = listToString(links) 

mo = re.compile(r"bookmyshow")
regexelem = mo.findall(liststr)
lenvalue = len(regexelem)

bms_links = links[:lenvalue]
tnew_links = links[lenvalue:]

loopy(bms_links)
#loopy(tnew_links)

browser.quit()
