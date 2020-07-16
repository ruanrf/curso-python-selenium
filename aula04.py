# anotações e testes gerais da aula 04.
from selenium.webdriver import Chrome
from urllib.parse import urlparse
from time import sleep
from pprint import pprint

def find_by_text(browser, tag, text):
    ''' Find element with text "xpto".    
    Args:
        browser: web browser instance
        tag: tag containing the desired text
        text: content to be found 
    '''
    elements = browser.find_elements_by_tag_name(tag) #lista
    for element in elements:
        if element.text == text:
            return element

browser = Chrome()
url = 'https://selenium.dunossauro.live/aula_04.html'
browser.get(url)
sleep(1)

def get_links(browser, reference): # Get every link into given reference

    result = {}
    element = browser.find_element_by_tag_name(reference)
    anchors = element.find_elements_by_tag_name('a')
    for anchor in anchors:
        result[anchor.text] = anchor.get_attribute('href')

    return result

'''aulas'''
aulas = get_links(browser, 'aside')
pprint(aulas)

'''main'''
exercicios = get_links(browser, 'main')
browser.get(exercicios['Exercício 3'])


'''****************************encerrar****************************'''
sleep(15)
browser.quit()