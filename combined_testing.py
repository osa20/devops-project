import time

from backend_testing import backend_testings_func
from frontend_testing import frontend_testings_func


# Combined testing pulls in the backend testing and frontend testing functions
def combined_testing_func(user_id, username, creation_date):
    # Postimg any user data to the REST API using POST method
    # Submitting a GET request to make sure data equals the posted data
    # Using pymysql, checking that posted data was stored inside database (users table)
    backend_testings_func(user_id, username, creation_date)
    print()

    # Starting a Selenium Webdriver session
    # Navigating to web interface URL using an existing user id
    # Printing username (using locator) and checking that username is correct
    try:
        user_name = frontend_testings_func(user_id)
        if username == user_name:
            print('codes work well - test passed')
    except Exception as err:
        print(err, "test failed")
    time.sleep(5)


# For performing combined testing
if __name__ == '__main__':
    combined_testing_func(13, "Lanky", "2023-08-30")