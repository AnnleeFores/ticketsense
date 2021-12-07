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


def senseticket_bms(arg):
    
    browser.get(arg)
    try:
        elem = browser.find_element_by_id('showDates')
        p = (elem.text[0:2])
        print(f'{p} Dec')
        if p == '16':
            print('Bookmyshow: Spidey day slot opened!!!')
        else:
            print('Bookmyshow: not yet open')
        return p
    except:
        print('Was not able to find an element with that name.')

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
    

links.sort()


liststr = listToString(links) 


mo = re.compile(r"bookmyshow")
regexelem = mo.findall(liststr)
lenvalue = len(regexelem)

bms_links = links[:lenvalue]
tnew_links = links[lenvalue:]


for i in bms_links:
    senseticket_bms(i)
    time.sleep(5)

for i in tnew_links:
    senseticket_tnew(i)
    time.sleep(5)

browser.quit()
