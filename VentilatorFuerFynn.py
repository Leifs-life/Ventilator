from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import sched, time

but = '//*[@id="root"]/div/section/div/div[4]/div/section[1]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[4]/button'
url = 'https://www.mtvema.com/de-de/wahl/'

driver = webdriver.Firefox()
driver.get(url)

time.sleep(10)

element = driver.find_element_by_xpath(but)
while True:
    ActionChains(driver).click(element).perform()
    time.sleep(6)