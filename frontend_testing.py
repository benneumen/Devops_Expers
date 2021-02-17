import time
from selenium import webdriver

try:
    # Start Selenium Web Driver Session
    driver = webdriver.Chrome(executable_path="/Users/benn/Desktop/chromedriver")
    driver.get("http://127.0.0.1:5001/")
    driver.get("http://127.0.0.1:5001/users/get_user_data/123")
    name = driver.find_element_by_id("user").text
    # print locator text
    print(name)
    time.sleep(3)

    driver.quit()
except:
    print("test failed")
