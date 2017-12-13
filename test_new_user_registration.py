# -*- coding: utf-8 -*-
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

reload(sys)
sys.setdefaultencoding('utf-8')

# binary = FirefoxBinary('C:\\Python27\\selenium\\webdriver\\firefox\\geckodriver.exe')
# browser = webdriver.Firefox(firefox_binary=binary)
browser = webdriver.Firefox()

n = 1
# Navigate to kodibg.org/forum
browser.get('https://kodibg.org/forum/')
assert 'Коди Фен Форум България' in browser.title
print "%s. Kodi landing page loaded" % n

modal = browser.find_element_by_id("quick_login")
assert modal.value_of_css_property("display") == "none"
n += 1
print "%s. Login modal box is not visible" % n

elems = browser.find_elements_by_xpath('//*[contains(text(), "Вход")]')  # Find the search box
elems[0].click()
n += 1
print "%s. Found \"Вход\" button".encode("utf-8") % n

sleep(3)

modal = browser.find_element_by_id("quick_login")
assert modal.value_of_css_property("display") != "none"
n += 1
print "%s. Login modal box is visible" % n

element_username = browser.find_element_by_id("quick_login_username")
element_username.clear()
element_username.send_keys("dummy")

element_password = browser.find_element_by_id("quick_login_password")
element_password.clear()
element_password.send_keys("pass");

n += 1
print "%s. Filled out username and password" % n

element_password.send_keys(Keys.RETURN)
#browser.find_element_by_class_name("loginbutton").click()
sleep(5)

element_error = browser.find_element_by_class_name("error")
assert element_error != None
n += 1
print "%s. Successfully failed to login" % n


#hover = ActionChains(webdriver).move_to_element(elem)
#hover.perform()
#elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()