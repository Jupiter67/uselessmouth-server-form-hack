import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def init_driver(path: str):
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=option)

    driver.get("http://www.google.com/")

    return driver


def ahlshtl_vote(driver) -> None:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
    print('Open tab!')

    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfH-HOQ1eYWZyDQu1PGbGbSSwOpIjvCK_4us5_O00hiGnuhpQ/viewform')

    ahlshtl_radio = driver.find_element(By.XPATH, '//*[@id="i199"]')
    ahlshtl_radio.click()

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div')
    submit.click()
    print('Voted!')

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')
    print('Close tab!')


if __name__ == '__main__':
    dirname = os.getcwd()
    path = os.path.join(dirname, 'chromedriver.exe')
    driver = init_driver(path)
    for i in range(100):
        ahlshtl_vote(driver)
