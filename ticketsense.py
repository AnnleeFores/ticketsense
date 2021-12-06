from selenium import webdriver
import time

links = []

#BMS
link1 = 'https://in.bookmyshow.com/buytickets/carnival-downtown-thalassery/cinema-thay-CDTH-MT/20211216'
link2 = 'https://in.bookmyshow.com/buytickets/aura-cinema-mattannur/cinema-matt-ACMR-MT/20211216'

#TNEW
link3 = 'https://www.ticketnew.com/Carnival-Downtown--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/12539/20211216'
link4 = 'https://www.ticketnew.com/Liberty-Paradise-Complex--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/1203/20211216'


links += [link1,link2,link3,link4]

browser = webdriver.Firefox()


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
        elem = browser.find_element_by_id('ulShowDate')
        q = (elem.text[6:])
        print(f'{q} Dec')
        if q == '16':
            print('Ticket New: Spidey day slot opened!!!')
        else:
            print('Ticket New: not yet open')
        return q
    except:
        print('Was not able to find an element with that name.')


#while True:

bms_links = links[:2]
tnew_links = links[2:4]

for i in bms_links:
    senseticket_bms(i)
    time.sleep(5)

for i in tnew_links:
    senseticket_tnew(i)
    time.sleep(5)

browser.quit()
