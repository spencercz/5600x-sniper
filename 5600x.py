import time
import json
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

print("Welcome to the AMD Ryzen 5 5600x sniper by @spencer_cz")
driver = webdriver.Firefox()

def setup():
    driver.get("https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=zg_bs_229189_11?_encoding=UTF8&psc=1&refRID=46SVCMBX83Z462G6B1R7&tag=hawk-future-20&ascsubtag=anandtech-us-1765479942728721200-20") # open amazon site
    #driver.get("https://www.amazon.com/SAMSUNG-500GB-Internal-Gaming-MZ-V8P500B/dp/B08GL575DB/ref=bmx_5/132-7891775-2458233?_encoding=UTF8&pd_rd_i=B08GL575DB&pd_rd_r=c2d0184c-65d5-410f-a6f3-91a1b0c7580a&pd_rd_w=M1llc&pd_rd_wg=zl0U0&pf_rd_p=c5e1cf4b-c006-4b7a-bb44-797de0814d9a&pf_rd_r=J48YQN3V2SCJ8K40127D&psc=1&refRID=J48YQN3V2SCJ8K40127D")
    driver.find_element_by_id("nav-link-accountList").click()
    WebDriverWait(driver, 999999).until(expected_conditions.presence_of_element_located((By.ID, "add-to-wishlist-button-submit")))

def snipe_5600x():
    button_exists = False
    while not button_exists:
        driver.refresh()
        button_exists = check_exists_by_id("buy-now-button")
    beep()
    driver.find_element_by_id("buy-now-button").click()
    # ----- tries to dismiss popup, passes if no popup found -----
    try:
        driver.find_element_by_id("siNoCoverage-announce").click()
    except:
        pass
    # ----- tries to place order -----
    try:
        driver.find_element_by_id("placeYourOrder").click() # confirm order
        print("Sniped!")
        return
    except:
        pass
    # ----- tries to place order a different way -----
    try:
        driver.find_element_by_id("turbo-checkout-pyo-button").click() # confirm order
        print("Sniped!")
        return
    except:
        pass
    # ----- needs user input to finish -----
    WebDriverWait(driver, 999999).until(expected_conditions.presence_of_element_located((By.ID, "placeYourOrder"))) # waits for place order button to be present, beeps when it is
    beep2()

def beep():
    winsound.Beep(1500, 150)
    winsound.Beep(1500, 150)
    winsound.Beep(1500, 150)

def beep2():
    winsound.Beep(1500, 150)
    winsound.Beep(1500, 150)
    winsound.Beep(1500, 150)
    winsound.Beep(1500, 150)

def check_exists_by_id(id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

if __name__ == "__main__":
    setup()
    snipe_5600x()
