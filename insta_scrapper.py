# imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import csv

# specify the path to chromedriver.exe
# here we have the driver in the same directory with our file
driver = webdriver.Chrome('chromedriver.exe')
# open insta webpage
driver.get('https://www.instagram.com/')

# target username
user_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# enter username and password
user_name.clear()
username = input('Enter your User name')
user_name.send_keys(username)

password.clear()
passw = input('Enter your password')
password.send_keys(passw)

# target the login button and click it
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
# We are logged in!

# pressing "Not Now" button
time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
alert_2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# put the link of the required page
link = input("input required link")
driver.get(link + 'tagged/')

# choose file name
name = input("Choose the file name for saved links")


# scroll down x times
# increase n_scrolls to sroll more
n_scrolls = 3
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    
# target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]

# narrow down all links to tagged links only
anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

a_tags = set()
# follow each link and extract the tagged link and put it in a set
for a in anchors:
    driver.get(a)
    time.sleep(10)
    title = driver.find_elements_by_class_name('_aap6')
    for j in title:
        try:
            atag = j.find_element_by_xpath(".//a")
            a_tags.add(atag.get_attribute('href'))
        except:
            pass

# write the links to a csv file

head = ["link"]
a = [[x] for x in a_tags]

# write 
with open(name + ".csv", 'w') as file:
    file.writer = csv.writer(file)
    file.writer.writerow(head)
    file.writer.writerows(a)    
