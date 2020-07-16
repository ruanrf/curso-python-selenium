from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser.get(url)

sleep(.5)

condition = True
esperado = browser.find_elements_by_tag_name('p')[1].text[-1]
anchor = browser.find_element_by_tag_name('a')

while condition == True:
    sleep(.5)
    anchor.click()
    values = browser.find_elements_by_tag_name('p')
    # print(values[-1].text)
    if(values[-1].text[-1] == esperado):
        break

sleep(2)
browser.quit()