# Importing Stuffs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.parse
import pickle

# This a change station. You can change link filename and everything here.
scrapingOutputFileName = "links"  # Enter the name of file to save scraped IPs.
searchTerm = '' #Enter your search term here. You must enter in exactly same pattern as in ZoomEye website.
cookieFileName = 'cookie' #Name of the cookie file.
pageLoadoutTime = 60  # This is time to wait for page to load.
totalNumberOfPages = 20 # Number of pages to scrape from.

#Links of the website
telnet = 'https://sso.telnet404.com' #Telnet website link
zoomeye = 'https://www.zoomeye.org' #Zoomeye website link.

# Opening a new Browser Window in Firefox
browser = webdriver.Firefox()
browser.set_page_load_timeout(pageLoadoutTime)
browser.get(telnet + '/cas/login?service=' + urllib.parse.quote('https://www.zoomeye.org/login'))
cookies = pickle.load(open(cookieFileName + '.pkl', "rb"))
for cookie in cookies:
    print(cookie)
    browser.add_cookie(cookie)
browser.get(zoomeye)
browser.find_element_by_class_name('header-profile-link').click()
time.sleep(3)

#Waiting for page to load
while True :
    try:
        if browser.find_element_by_class_name('profile-info-value').get_attribute('innerHTML') != 'randomtext' :
            break
    except NoSuchElementException :
        print('Waiting for the page to load! #1')
        time.sleep(1)

#Defining the ways to surf the webpage.
def pageExplorer():
    file = open(scrapingOutputFileName + ".txt", "a")
    clickLinks = browser.find_elements_by_xpath(".//a[contains(@class,'search-result-item-title')]")
    for links in clickLinks :
        ip = links.get_attribute("innerHTML")
        if ip[0:2] != '<i':
            file.write(ip+"\n")
            print(ip)
    browser.find_element_by_class_name("ant-pagination-next").click()
    time.sleep(5)

#Loading the ZoomEye Search page.
browser.get(zoomeye+ '/searchResult?q=' + urllib.parse.quote(searchTerm))

#Checking if the page has loaded. If not wait for 5 secs.
while len(browser.find_elements_by_xpath(".//i[contains(@class,'anticon anticon-right-circle')]/ancestor::a"))==0 :
    time.sleep(5)
    print('Waiting 5 more seconds!')

currentPageNumber = 1
while currentPageNumber <= totalNumberOfPages :
    pageExplorer()
    print('Page '+str(currentPageNumber)+' done!')
    currentPageNumber += 1
    if currentPageNumber == totalNumberOfPages + 1 :
        print('All done!')
        browser.quit()
        exit()