
from time import sleep
from selenium.webdriver import Chrome
from urllib.parse import urlparse
from pprint import pprint

def get_anchors(browser, ref):
    '''
    Return all anchors given desired ref. and browser.
    '''
    elements = browser.find_element_by_tag_name(ref)
    anchors = elements.find_elements_by_tag_name('a')
    return anchors

def get_url_by_ref(browser, ref):
    '''
    Return url from given ref. and text.
    '''

    result = {}
    anchors = get_anchors(browser, ref)
    for anchor in anchors:
        result[anchor.text] = anchor.get_attribute('href')
    return result

def get_wrong(browser, ref): 
    '''
    REturn url behind wrong answer given a tag and browser.
    '''
    for anchor in get_url_by_ref(browser, ref).values():
        if 'diabao' not in anchor:
            return anchor
        
def get_url_by_title(browser, ref):
    '''
    Return url behind the anchor with same text as page title.
    '''
    title = browser.title
    anchors = get_anchors(browser, ref)
    for anchor in anchors:
        if anchor.text == title:
            return anchor.get_attribute('href')

def get_url_by_path(browser, ref):
    path = urlparse(browser.current_url).path
    anchors = get_anchors(browser, ref)
    for anchor in anchors:
        if anchor.text in path:
            return anchor.get_attribute('href')
    

browser = Chrome()
browser.get('https://selenium.dunossauro.live/exercicio_03.html')
sleep(2)

pag_1 = get_url_by_ref(browser, 'main') # page 1: start here
browser.get(pag_1['Começar por aqui'])
sleep(2)

pag_2 = get_wrong(browser, 'main') # page 2: wrong answer
browser.get(pag_2)

sleep(20)
pag_3 = get_url_by_title(browser, 'main') # page 3: same as title
browser.get(pag_3)

sleep(2)
pag_4 = get_url_by_path(browser, 'main') # page 4: title and text
browser.get(pag_4)

sleep(2)
browser.refresh() # refresh or damnation

sleep(10)
browser.quit()