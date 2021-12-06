from selenium import webdriver
import time

link1 = 'https://in.bookmyshow.com/buytickets/carnival-downtown-thalassery/cinema-thay-CDTH-MT/20211216'
link2 = 'https://in.bookmyshow.com/buytickets/aura-cinema-mattannur/cinema-matt-ACMR-MT/20211216'
link3 = 'https://www.ticketnew.com/Carnival-Downtown--Thalassery-Book-My-Movie-Show-Tickets/Online-Ticket-Booking/12539'

browser = webdriver.Firefox()

def senseticket_bms(arg):
    browser.get(arg)
    try:
        elem = browser.find_element_by_id('showDates')
        p = (elem.text[0:2])
        print(p)
        if p == '16':
            print('16th slot opened')
        else:
            print('not yet open')
        return p
    except:
        print('Was not able to find an element with that name.')

    


ticket = senseticket_bms(link1)
print(ticket)

time.sleep(5)

ticket = senseticket_bms(link2)
print(ticket)

time.sleep(5)

ticket = senseticket_bms(link3)
print(ticket)



browser.quit()

""" while True:
    browser.refresh()
    try:
        elem = browser.find_element_by_id('showDates')
        print(str(elem.text))
    except:
        print('Was not able to find an element with that name.')
    time.sleep(5) """





