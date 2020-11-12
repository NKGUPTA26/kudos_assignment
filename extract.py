import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64
from image_processing import *
from data_processing import html_data_processing

def main(search_key_input):
    driver = webdriver.Chrome(executable_path=r"chromedriver")
    driver.maximize_window()
    driver.get("https://unifiedportal-epfo.epfindia.gov.in/publicPortal/no-auth/misReport/home/loadEstSearchHome")
    search_key_input = str(search_key_input)
    driver.find_element_by_xpath("//input[@id='estName']").send_keys(search_key_input)
    img_data = driver.find_element_by_xpath("//img[@id='capImg']").screenshot_as_base64
    img_data = bytes(img_data,'utf-8')
    with open("captcha.png", "wb") as fh:
        fh.write(base64.decodebytes(img_data))
    captcha = driver.find_element_by_xpath("//input[@id='captcha']")
    input_image_path = "captcha.png"
    text = image_to_text(input_image_path)
    print("Please check the captcha, is it correctly processed or not? You have 30 second to check and fix it.")
    captcha.send_keys(text)
    time.sleep(30)
    driver.find_element_by_xpath("//input[@id='searchEmployer']").click()
    information_of_data = driver.find_element_by_xpath('//body/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]').text
    number_of_data = information_of_data.split().pop()
    number_of_data = int(number_of_data)
    data = []
    counter = 1
    while True:
        scrapped_html = driver.find_element_by_xpath("//div[@id='collapseTwo']").get_attribute('innerHTML')
        per_page_data,number_of_data,flag,counter = html_data_processing(scrapped_html,number_of_data,counter)
        data.append(per_page_data)
        if flag == False:
            break
        time.sleep(10)
        driver.find_element_by_xpath("//a[@id='example_next']").click()
        
    return data
    driver.close()
