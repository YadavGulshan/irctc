# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import pyautogui as pg
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import pyautogui as pg
driver = webdriver.Chrome(ChromeDriverManager(
    chrome_type=ChromeType.CHROMIUM).install())
# from selenium import webdriver

# from webdriver_manager.chrome import GeckoDriverManager
# options = webdriver.FirefoxOptions()


# options.add_argument("--headless")

# driver = webdriver.Chrome(
# ChromeDriverManager().install(), options=options)

# driver = webdriver.Firefox(executable_path='/home/gulshan/geckodriver')
ok_xpath = '/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div[2]/div/form/div[2]/button'
from_xpath = '//*[@id="origin"]/span/input'
to_xpath = '//*[@id="destination"]'
date_xpath = '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input'
class_xpth = '//*[@id="journeyClass"]/div/label'
train_xpath = '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button'
fromStation = 'THANE - TNA'
toStation = 'JAKHANIAN - JKN'
dateOfJourney = '26-11-2020'
noOfPassengers = 3
noOfPassengers_xpath = '//*[@id="numberOfPassengers"]/div/label'
modifySearch_xpath = '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[6]/button'
username = 'your username' #case sensitive
password = 'your paasword' #case sensitive
driver.get("https://www.irctc.co.in/nget/train-search")
assert "IRCTC" in driver.title
ok = driver.find_element_by_xpath(ok_xpath)
ok.click()


def firstpage():

    from_station = driver.find_element_by_xpath(from_xpath)
    from_station.clear()
    from_station.send_keys(fromStation)
    pg.press("tab")
    pg.press("tab")

    pg.write(toStation)
    pg.press("tab")
    pg.press("backspace")
    pg.write(dateOfJourney)
    pg.press("tab")

    for i in range(0, 9):
        pg.press("down")
    
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("enter")


def booknow():
    username_xpath = driver.find_element_by_xpath('//*[@id="userId"]')
    username_xpath.send_keys(username, Keys.RETURN)
    password_xpath = driver.find_element_by_xpath('//*[@id="pwd"]')
    password_xpath.send_keys(password, Keys.RETURN)

    sleep(10)
    print("sleep ended...............................................................Now rest of the things can only be done by you..!")


firstpage()
print("Please click agree and ok !")
sleep(15)
booknow()
sleep(10)
print("fill captcha")
# driver.close()
