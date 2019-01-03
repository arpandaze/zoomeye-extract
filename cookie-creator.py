# Importing Stuffs
from selenium import webdriver
import pickle

cookieFileName = "cookie"  # Name of cookie file.
telnet = "https://sso.telnet404.com/cas/login"  # Telnet Login Link
pageLoadoutTime = 60  # This is time to wait for page to load.

# Opening a new Browser Window
browser = webdriver.Firefox()
browser.set_page_load_timeout(pageLoadoutTime)
browser.get(telnet)
while True :
    imp = input("Enter a command: ")
    if imp == 'capture' :
        print('Capturing cookie from TelNet')
        pickle.dump(browser.get_cookies(), open(cookieFileName+'.pkl', "wb"))
    elif imp == 'exit' :
        browser.quit()
        exit()
    else :
        print('Invalid Command')