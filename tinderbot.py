
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.keys import Keys
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://tinder.com")

sleep(2)
decline=driver.find_element(By.XPATH,value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button')
decline.click()

sleep(2)
login=driver.find_element(By.LINK_TEXT,value="Log in")
login.click()

sleep(5)
fb=driver.find_element(By.XPATH,value='//*[@id="s2018968691"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div')
fb.click()

sleep(2)
base_window=driver.window_handles[0]
fb_login_window=driver.window_handles[1]
driver.switch_to.window(fb_login_window)

sleep(2)
fb_user=driver.find_element(By.XPATH,value='//*[@id="email"]')
fb_user.click()
fb_user.send_keys("9652880429")
fb_pass=driver.find_element(By.XPATH,value='//*[@id="pass"]')
fb_pass.click()
fb_pass.send_keys("Sai@2607")
log_in=driver.find_element(By.XPATH,value='//*[@id="loginbutton"]')
log_in.click()

sleep(2)
driver.switch_to.window(base_window)

sleep(10)
allow=driver.find_element(By.XPATH,value='//*[@id="s2018968691"]/main/div/div/div/div[3]/button[1]')
allow.click()

sleep(1)
enable=driver.find_element(By.XPATH,value='//*[@id="s2018968691"]/main/div/div/div/div[3]/button[1]')
enable.click()
sleep(20)
swipe=driver.find_element(By.XPATH,value='//*[@id="s-547617529"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')
swipe.click()


