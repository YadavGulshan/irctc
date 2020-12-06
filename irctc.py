from selenium import webdriver
# Used for checking if the desired html content is loaded or not.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
###
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import pyautogui as pg
# from bs4 import BeautifulSoup as bs4


# from webdriver_manager.chrome import GeckoDriverManager
# options = webdriver.FirefoxOptions()


# options.add_argument("--headless")

# driver = webdriver.Chrome(
#     ChromeDriverManager().install(), options=options)

# driver = webdriver.Firefox(executable_path='/home/gulshanyadav/geckodriver')


ok_xpath = '/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div[2]/div/form/div[2]/button'
from_xpath = '//*[@id="origin"]/span/input'
to_xpath = '//*[@id="destination"]'
date_xpath = '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input'
class_xpth = '//*[@id="journeyClass"]/div/label'
train_xpath = '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button'
fromStation = 'THANE - TNA' #always first check this in irctc website
toStation = 'JAKHANIAN - JKN'
dateOfJourney = '06-12-2020'
noOfPassengers = 3
addr = 'maharbuzurg'
noOfPassengers_xpath = '//*[@id="numberOfPassengers"]/div/label'
modifySearch_xpath = '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[6]/button'
addPassenger_xpath = '//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/div[2]/a/span'
address1_xpath = '//*[@id="aaa1"]'
checkAvailability_xpath = '//*[@id="check-availability"]'

# book now buttons
booknow_xpath = '//*[@id="ui-panel-0-content"]/div/div/div/table/tbody/tr/td[1]/div/div[3]/button'
booknow2_xpath = '//*[@id="ui-panel-0-content"]/div/div/div/table/tbody/tr/td[2]/div/div[3]/button'
############


# Test
name1 = 'Gulshan yadav'
age1 = 18
######
# credentials
username = 'Your username'
password = 'Password'
##########

driver = webdriver.Chrome(ChromeDriverManager(
    chrome_type=ChromeType.CHROMIUM).install())
driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")
assert "IRCTC" in driver.title
ok = driver.find_element_by_xpath(ok_xpath)
ok.click()


def firstpage():

    from_station = driver.find_element_by_xpath(from_xpath)
    from_station.clear()
    from_station.send_keys(fromStation.upper())

    # pg.write(fromStation)
    # pg.press("enter")

    pg.press("tab")
    pg.press("tab")

    pg.write(toStation.upper())
    pg.press("tab")
    pg.press("backspace")
    pg.write(dateOfJourney)
    # pg.press("enter")
    pg.press("tab")

    for i in range(0, 9):
        pg.press("down")
    # classCoach = driver.find_element_by_xpath(class_xpth)
    # classCoach.click()
    # classCoach.click()
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("enter")


def booknow():
    # click on check availabilty
    availabilty = driver.find_element_by_xpath(checkAvailability_xpath)
    availabilty.click()
    ####
    sleep(2)  # so that everything is being loaded

    # searching book now buttons
    booknowButton = driver.find_element_by_xpath(booknow_xpath)
    booknowButton.click()

    ###################

    # check the waiting status.
    # waiting = driver.find_element_by_class_name("waitingstatus").text
    # print(waiting)
    # if(waiting=="avaiable")
    # check if the waiting is less than 1.... or it is available.

    # <span _ngcontent-c19="" class="waitingstatus" style="color: rgb(194, 93, 4);"> PQWL58/WL43 </span>
    # div = soup.findAll('div', class_="image_container")
    # bookNowButton = soup.findAll('span', class_="waitingstatus") #using bs4 but seems a slow process to me !

    ##########################
    # You have to click on agree twice tooo!
    # 3

    # inputting credentials
    username_xpath = driver.find_element_by_xpath('//*[@id="userId"]')
    username_xpath.send_keys(username, Keys.RETURN)
    password_xpath = driver.find_element_by_xpath('//*[@id="pwd"]')
    password_xpath.send_keys(password, Keys.RETURN)
    # sleep for inputting captcha... (should be done by the user...!)
    sleep(5)
    print("sleep ended...............................................................")


# to_station = driver.find_element_by_xpath(to_xpath)
# to_station.clear()
# to_station.send_keys(toStation)
# pg.press("enter")

def passengersDetail():

    for i in range(1, noOfPassengers+1):
        passenger_xpath = f'//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/div[{i}]/div/div[2]/app-passenger/div/div[1]/div[1]/input'
        age_xpath = f'//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/div[{i}]/div/div[2]/app-passenger/div/div[1]/div[2]/input'
        # print(passenger_xpath, '\n age', age_xpath)

        passengerName1 = driver.find_element_by_xpath(passenger_xpath)
        passengerName1.send_keys(name1)

        # age

        ageOfPassenger1 = driver.find_element_by_xpath(age_xpath)
        ageOfPassenger1.send_keys(age1)
        pg.press("tab")
        pg.press("down")  # for male

        # click on add passenger
        addpassenger = driver.find_element_by_xpath(addPassenger_xpath)
        addpassenger.click()


# for filling up address details
    addressFillup1 = driver.find_element_by_xpath(address1_xpath)
    addressFillup1.send_keys(addr)


firstpage()
# sleep(15)


# waiting for check-avialabilty id to be loacded ... so that it can be clicked...
try:
    myElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'check-availability')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

    #################
    # <button _ngcontent-c19="" class="form-control btn btn-primary" id="check-availability" aria-label="Check availability &amp; fare for Train Number 05017 from THANE at 07:00 hours
    #           to JAKHANIAN on 14:41 hours for class Sleeper (SL) and quota GENERAL. Total duration for this trip is 31:41"> Check availability &amp; fare </button>

    ############

# driver.get("https://www.irctc.co.in/nget/booking/train-list")
booknow()
sleep(10)
sleep(10)
# passengersDetail()
# # driver.close()
