from selenium import webdriver
import time

def vote_fsu():
    driver = webdriver.Safari()

    driver.get('https://poll.fm/13033913')
    button_fsu = driver.find_element("xpath", '//*[@id="PDI_answer58512597"]')
    button_fsu.click()
    vote_button = driver.find_element("xpath", '//*[@id="pd-vote-button13033913"]')
    vote_button.click()
    time.sleep(2)
    driver.delete_all_cookies()
    driver.quit()

for _ in range(5):
    vote_fsu()
