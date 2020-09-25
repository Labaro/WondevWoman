from selenium import webdriver
import time
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Load email and password of codingames from .pass_codingames file
file = open('/home/merlin/.pass_codingames', 'r')
email = file.readline()
password = file.readline()
file.close()

# Load driver
driver = webdriver.Firefox(executable_path="/home/merlin/.local/share/WebDriverManager/gecko/v0.27.0/geckodriver-v0.27.0-linux64/geckodriver")
driver.maximize_window()
# Navigate to condingames/wondev_woman
driver.get("https://www.codingame.com/ide/puzzle/wondev-woman")
# Login with email and password
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'cg-register-form_already-registered'))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'email'))).send_keys(email)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys(password)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'cg-login-form_submit-button'))).click()

# Sleep in order to wait main-button to be clickable (EC.element_to_be_clickable doesn't work)
time.sleep(3)
# Close login frames
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'main-button'))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'got-it'))).click()

# Copy/Paste the code
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'view-lines'))).click()
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
fo = open('/home/merlin/Documents/Centrale/refresher_cs/WondevWoman/Wondev_Woman.py', 'r')
line = fo.readline()
while line != '':
    pyperclip.copy(line)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    line = fo.readline()
fo.close()
# Launch a game
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'play'))).click()
