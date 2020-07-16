from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

browser.get(url)

sleep(.5)

title = browser.find_element_by_tag_name('h1')

d2 = {}
d1 = {title.text: d2}
    
p_list = browser.find_elements_by_tag_name('p')

for i in range(len(p_list)):
    d2.update({f'texto{i+1}' : p_list[i].text})

print(d1)

sleep(.2)
browser.quit()