import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


while True:
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('C:\Windows\chromedriver.exe', chrome_options=options)
    driver.get("http:///admin/advanced")

    bad_text = "Failed - Not Reachable"
    good_text = "Registered"
    elem = driver.find_element_by_xpath(
        '/html/body/center/table/tbody/tr[5]/td/form/div[1]/table/tbody/tr[45]/td[2]/font')

    if elem.text == bad_text:
        print("Check")
        print("Check")
        print("Check")
        print("Check")
        print("Check")
        break
    elif elem.text == good_text:
        print("Good")
        time.sleep(5)
        driver.refresh()
    else:
        print("not sure")
        print("not sure")
        print("not sure")
        print("not sure")
        print("not sure")
        break
