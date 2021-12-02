import os
import csv
from os.path import join, dirname
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# * Global variables
dotenv_path = join(dirname(__file__), '.env')
csv_path = join(dirname(__file__), 'accounts.csv')
load_dotenv(dotenv_path)
accounts = []

URL = os.environ.get('URL')
# driver = webdriver.Chrome()


# def click_element_by_xpath(path):
#     element = WebDriverWait(driver, 10).until(
#         lambda x: x.find_element_by_xpath(path))
#     element.click()


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


if __name__ == "__main__":
    print(URL)
    load_csv_as_dict(csv_path)
    print(accounts[0])
