from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver


def main():
    driver = get_driver()

    # Fills in username and password
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)

    # Clicks on home page
    driver.find_element(by=By.XPATH, value="/html/body/nav/div/a").click()
    time.sleep(2)

    # Scrapes the temperature value
    element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/h1[2]")
    element = float(element.text.split(": ")[1])
    print(element)

