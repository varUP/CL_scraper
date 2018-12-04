from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import sys
import time

search_url = sys.argv[1]


def ikea_finder(input_list):
    ikea_cleaned = []
    for item in input_list:
        if 'ikea' in item.lower():
            ikea_cleaned.append(item)
    print(ikea_cleaned)


def item_collector():
    try:
        time.sleep(5)
        posts = driver.find_elements_by_class_name("hdrlnk")
        ikea_list = [post.text for post in posts]
        ikea_finder(ikea_list)

    except Exception as driver_error:
        print(driver_error)
        driver.close()
        driver.quit()


def chrome_me(url):
    try:
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--windows-size=1920*1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-proxy-server")

        chrome_driver = os.getcwd() + "/binary/chromedriver"
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        driver.get(url)

    except Exception as req_error:
        print('There seems to be an issue with your input URL.')
        print(req_error)
        sys.exit(1)

    return driver


driver = chrome_me(search_url)
driver.find_element_by_xpath('''//*[@id="sss1"]/li[3]/a''').click()
cl_url = driver.current_url

while True:
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="searchform"]/div[3]/div[3]/span[2]/a[3]''')))
        # wait for elements to load
        if driver.find_element_by_xpath('''//*[@id="searchform"]/div[3]/div[3]/span[2]/a[3]'''):
            item_collector()
            print('it exists on {0}'.format(driver.current_url))
            time.sleep(5)
            # check to see if there is another link
            driver.find_element_by_xpath('''//*[@id="searchform"]/div[3]/div[3]/span[2]/a[3]''').click()
            continue

        else:
            # if no link exists via the xpath, then we break
            print('stopping on {0}'.format(driver.current_url))
    except Exception as error:
        print(error)
    break

driver.close()
driver.quit()
