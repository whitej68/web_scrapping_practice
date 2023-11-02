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
    driver.get("https://automated.pythonanywhere.com")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(":")[1])
    return output


def write_file(text):
    """Write input text into a text file"""
    date = time.strftime("%Y-%m-%d.%H-%M-%S.txt")
    with open(date, 'w') as file:
        file.write(text)


def main():
    driver = get_driver()

    while True:
        time.sleep(2)
        element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        write_file(text)


main()