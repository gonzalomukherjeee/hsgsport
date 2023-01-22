import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import os

#HSG SPORT AUTOMATION TOOL v3
#property of GONZALO MUKHERJEE


with open("config.json", "r", encoding='utf-8') as read_file:
    json_data = json.loads(read_file.read())

user_agent = json_data.get("user_agent")
google_path = json_data.get("google_path")
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("user-data-dir="+google_path)
chrome_options.add_argument(f"user-agent={user_agent}")

#THIS IS WHEN THE BOT WILL RUN AND START WORKING. RUN THE PROGRAM ANYTIME BEFORE

while True:
    while True:
        date_obj = datetime.now()
        if date_obj.hour == 3 and date_obj.minute == 00:#INSERT HOUR AND MINUTES. INSERT MINUTE BEFORE OPENING
            break
        else:
            time.sleep(1)



    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()


    driver.get("https://www.sportprogramm.unisg.ch/unisg/angebote/aktueller_zeitraum/_Fitnesstraining_Gym_-_Slot_selbstaendiges_Training.html")#THIS IS THE GYM WEBPAGE; CUSTOMISE YOURS


    rows = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, f'//table/tbody/tr')))

    for row in rows:
        tim = row.find_element_by_xpath("./td[4]").text
        if tim == "14:15-15:15": #THIS IS THE TIMESLOT YOU WISH TO ENROLL IN
            print(row.find_element_by_xpath("./td[3]").text)
            # print(row.find_element_by_xpath("./td[1]").text)
            try:
                row.find_element_by_xpath("./td/input[@class='bs_btn_buchen']").click()
            except Exception as e:
                print(e)
                print("Could not book...")
                continue
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@class='inlbutton buchen']"))).click()
                time.sleep(1)

                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, '//input[@value="M"]'))).click()

                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='BS_F1100']"))).send_keys("Gonzalo") #INSERT YOUR FIRST NAME
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='BS_F1200']"))).send_keys("Mukherjee")#INSERT YOUR LAST NAME
                drop_down = Select(WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//select[@name='statusorig']"))))
                time.sleep(1)
                drop_down.select_by_value("S-HSG")

                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='BS_F2000']"))).send_keys("example@unisg.ch")#INSERT EMAIL
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@value='1']"))).click()
                print("DO it now")
                time.sleep(2)
                element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@value='weiter zur Buchung']")))

                driver.execute_script("arguments[0].setAttribute('class','')", element)
                element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@value='weiter zur Buchung']")))

                ActionChains(driver).move_to_element(element).perform()
                time.sleep(.5)
                ActionChains(driver).click(element).perform()

                element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@value='verbindlich buchen']")))
                element.click()
                break
            except Exception as e:
                print("New page Error")
                print(e)
    time.sleep(15)
    driver.close()
    while True:
        try:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            time.sleep(1)
        except:
            break
    time.sleep(60)
