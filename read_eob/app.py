# Based on
# https://github.com/mozilla/geckodriver/releases
# https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
# https://www.quora.com/How-can-I-write-a-Python-script-to-open-a-webpage-and-login-to-a-website-in-the-background-automatically-as-soon-as-I-connect-to-LAN

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import os
import sys
import json

now = datetime.now()
timestamp = str(now).replace(' ', '_').replace(':', '-').replace('.', '-')
os.chdir(os.path.dirname(__file__))

max_date = datetime(2020, 6, 15)

screenshot_dir = r'E:\Development\private\daily_logins'

with open(r"E:\Development\private\daily_logins.json") as f:
    data = json.load(f)
    dummy_breakpoint = 1


def logon_EOBs():
    browser = webdriver.Firefox(executable_path=r'./geckodriver.exe')
    print("Logging into EOBs")
    # browser = webdriver.Firefox()

    username = data['eobs']['username']
    password = data['eobs']['password']

    try:
        browser.get('https://my.cigna.com/web/secure/my/claims/eob-statements?parent=claims')

        username_box = browser.find_element_by_id('username')
        username_box.send_keys(username)
        time.sleep(1)
        password_box = browser.find_element_by_id('password')
        password_box.send_keys(password)
        time.sleep(1)
        login_button = browser.find_element_by_id('loginbutton')
        login_button.click()
        # time.sleep(1)
        # browser.get_screenshot_as_file(screenshot_dir + '/GameFAQs' + timestamp + '.png')

        time.sleep(20)

        tables = browser.find_elements_by_xpath("//*[@data-columnpick-table-num='0']")
        table = tables[0]

        for idx, row in enumerate(table.find_elements_by_xpath(".//tr")):
            if len(row.find_elements_by_xpath(".//td")) != 6:
                continue

            cells = row.find_elements_by_tag_name('td')
            date_string = cells[0].text

            if datetime.strptime(date_string, '%m/%d/%Y') >= max_date:
                continue

            link = cells[5].find_element_by_tag_name('a')
            url = link.get_attribute('href')
            out_file = date_string[6:] + date_string[0:2] + date_string[3:5] + '-' + str(idx).zfill(3) + '.pdf'

            time.sleep(2)
            # https://stackoverflow.com/questions/37559480/how-to-convert-selenium-webdriver-get-cookies-to-cookie-text-file-for-use-with
            cookies_list = browser.get_cookies()
            cookies_dict = []
            for cookie in cookies_list:
                cookies_dict.append([cookie['name'], cookie['value']])
            cookies_dict = dict(cookies_dict)

            import requests
            r = requests.get(url, allow_redirects=True, cookies=cookies_dict)
            with open(out_file, 'wb') as f:
                f.write(r.content)

        a = 1
        time.sleep(8)
    except Exception as e:
        print("An error occurred while trying to access EOBs", e)
    finally:
        browser.close()
        print('DONE with EOBs')


if __name__ == '__main__':
    logon_EOBs()
    # logon_stackoverflow()
