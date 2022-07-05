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

