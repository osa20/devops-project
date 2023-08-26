import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import selenium.common.exceptions


def frontend_testings_func(user_id):
    global user_name
    global driver
    try:
        driver = webdriver.Chrome(service=Service())
        driver.implicitly_wait(10)

        # Navigating to web interface URL using an existing user id
        web_interface_url = f"http://127.0.0.1:5001/get_user_name/{user_id}"
        driver.get(web_interface_url)
        time.sleep(5)

        # Checking that the user name element is showing (web element exists)
        user_name = driver.find_element(By.ID, value="user").text
        # Printing username (using locator) and checking that username is correct
        print(user_name)

    except selenium.common.exceptions.WebDriverException as webDriverErr:
        print(webDriverErr)
    except selenium.common.exceptions.NoSuchWindowException as winException:
        print(winException)
    except Exception as exception:
        print(exception)
    finally:
        user_name = driver.find_element(By.ID, value="user").text
        return user_name


time.sleep(5)

# For performing frontend testing
if __name__ == '__main__':
    frontend_testings_func(1)