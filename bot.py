# open browwser with selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



def write_message(url: str, message: str):
    # open browser headless
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('https://discord.com/channels/611132910992490506/611135278454669332')
    browser.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/section/div[2]/button[2]/div').click()
    browser.find_element(By.NAME, "email").send_keys("m@fpvgear.dk")
    browser.find_element(By.NAME, "password").send_keys("*******")
    browser.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    sleep(15)
    chat = '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/main/form/div[1]/div[1]/div/div[3]/div/div[2]'
    chat = browser.find_element(By.XPATH, chat)  
    # split string on newline
    message_split = message.splitlines()

    for line in message_split:
        print(line)
        chat.send_keys(line)
        ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        sleep(1)

    chat.send_keys(Keys.ENTER)

    sleep(5)

