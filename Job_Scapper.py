from lib2to3.pgen2 import driver
from matplotlib.pyplot import get
from requests import options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

def get_jobs(keyword, num_job, verbose, path, slp_time):

    #Function to scrape the data from glassdoor and convert the data into a dataframe.

    #Initializing the webdriver
    options = webdriver.ChromeOptions()

    #For scraping without open a new Chrome window every time:
    #options.add_argument('headless')

    #Adjust the path of chromedrive to your main directory.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size()
    url = "https://www.glassdoor.co.in/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword"+keyword+"&typedLocation=&locT=&locId=&jobType=&context=Jobs&sc.keyword="+keyword+"&dropdown=0"

    driver = get(url)
    job = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(4)

        #Test for the "Sign Up" prompt and get rid of it.
        try:
            driver.find_element_by_class_name("selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)

        try:
            driver.find_element_by_class_name("ModalStyle__xBtn___29PT9").click()  #clicking to the X.
        except NoSuchElementException:
            pass
