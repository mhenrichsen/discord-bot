# open browwser with selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



def write_message(url: str, message: str):
    # open browser headless
    browser = webdriver.Chrome('/Users/mads/Desktop/discord-bot/chromedriver')
    browser.get('https://discord.com/channels/840898407022460948/844470172001894400')
    browser.find_element(By.NAME, "email").send_keys("m@fpvgear.dk")
    browser.find_element(By.NAME, "password").send_keys("********")
    browser.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    sleep(15)
    chat = '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]'
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

