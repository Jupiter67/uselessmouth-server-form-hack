import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from settings import Settings


def init_driver(path: str):
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=option)

    driver.get("http://www.google.com/")

    return driver


def ahlshtl_vote(driver, link: str = '') -> None:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
    print('Open tab!')

    driver.get(link)

    # region Vote
    # Смайл года
    driver.find_element(By.XPATH, '//*[@id="i305"]').click()
    # Селфи года
    driver.find_element(By.XPATH, '//*[@id="i33"]').click()
    # Клоун года
    driver.find_element(By.XPATH, '//*[@id="i52"]').click()
    # Игра года
    driver.find_element(By.XPATH, '//*[@id="i77"]').click()
    # Сериал года
    driver.find_element(By.XPATH, '//*[@id="i111"]').click()
    # Музыкальный альюом года
    driver.find_element(By.XPATH, '//*[@id="i154"]').click()
    # Контентмейкер года
    driver.find_element(By.XPATH, '//*[@id="i180"]').click()
    # Админ года
    driver.find_element(By.XPATH, '//*[@id="i199"]').click()
    # Канал года
    driver.find_element(By.XPATH, '//*[@id="i255"]').click()
    # Вайфу года
    driver.find_element(By.XPATH, '//*[@id="i286"]').click()
    # Мем года
    driver.find_element(By.XPATH, '//*[@id="i305"]').click()
    # Новичок года
    driver.find_element(By.XPATH, '//*[@id="i330"]').click()
    # Нововведение года
    driver.find_element(By.XPATH, '//*[@id="i380"]').click()
    # endregion

    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div').click()
    print('Voted!')

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')
    print('Close tab!')


if __name__ == '__main__':
    s = Settings()

    dirname = os.getcwd()
    path = os.path.join(dirname, 'chromedriver.exe')
    driver = init_driver(path)
    for i in range(s.retry_count):
        ahlshtl_vote(driver, link=s.form_url)
