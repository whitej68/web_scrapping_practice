from selenium import webdriver
from selenium.webdriver.common.by import By
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
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

print(main())