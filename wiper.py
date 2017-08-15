#usr/bin/python

__author__ = "Matthew Zheng"
__purpose__ = "Remove all previous filled forms -- designed with redoing webwork assignments in mind"

#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from msvcrt import getch

def __init__(self):
    #put in your own path below for your web driver of choice (use chrome for compatability with this code)
    _path = "C:\\Users\\Zhenger\\Desktop\\MLH\\Web-Wipe\\chromedriver_win32"
    self.driver = webdriver.Chrome(executable_path=_path)

def main():
    userKey = ord(getch())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://webwork.elearning.ubc.ca/webwork2/")
    if userKey == 27:
        driver.close()

if __name__ == "__main__":
    main()
