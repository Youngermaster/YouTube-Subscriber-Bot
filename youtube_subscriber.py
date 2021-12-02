import os
import csv
import time
from os.path import join, dirname
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver.v2 as uc

# * Global variables
dotenv_path = join(dirname(__file__), '.env')
csv_path = join(dirname(__file__), 'accounts.csv')
load_dotenv(dotenv_path)
accounts = []

subscribe_button_xpath = '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a/tp-yt-paper-button'

URL = os.environ.get('URL')
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-web-security")
# chrome_options.add_argument("--allow-running-insecure-content")
# driver = webdriver.Chrome(chrome_options=chrome_options)


def click_element_by_xpath(path):
    element = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath(path))
    element.click()


def print_csv_file(csv_path):
    with open(csv_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def load_csv_as_dict(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            accounts.append((row['account'], row['password']))


def subscribe_to_the_channel(email, password):
    driver.get(URL)
    # time.sleep(5)
    click_element_by_xpath(subscribe_button_xpath)

    time.sleep(3)
    google_email_form = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')

    google_email_form.send_keys(email)
    google_email_form.send_keys(Keys.ENTER)

    time.sleep(3)
    google_password_form = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')

    google_password_form.send_keys(password)
    google_password_form.send_keys(Keys.ENTER)

    time.sleep(3)
    click_element_by_xpath(
        '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string')


if __name__ == "__main__":
    print(URL)
    load_csv_as_dict(csv_path)

    for email, password in accounts:
        driver = uc.Chrome(
            executable_path="C:\\WebDriver\\bin\\chromedriver.exe")
        subscribe_to_the_channel(email, password)
        driver.close()
        driver.quit()
