from selenium import webdriver
import string
import random
import time



def generate_text(num):
        
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = num))
    return ran


url = "https://translate.google.com/?sl=en&text=home"

chromeLocationFile = "D:\Ahmed Zeedan\programs\chrom driver 103.5060/chromedriver.exe"

driver = webdriver.Chrome(chromeLocationFile)

driver.get(url)


def fill_first_name():

    text = driver.find_element("xpath",'//*[@class="kO6q6e"]').get_attribute("innerHTML")
    

    driver.find_element("xpath",'//*[@aria-label="Source text"]').click()

    driver.find_element("xpath",'//*[@aria-label="Source text"]').send_keys(text)

    print(text)
    
    time.sleep(2)


fill_first_name()
