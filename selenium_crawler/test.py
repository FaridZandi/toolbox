from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



display = Display(visible=0, size=(1920, 1080)).start()
service = Service("/usr/bin/chromedriver")
browser = webdriver.Chrome(service=service)
browser.get("https://google.com")
print (browser.title)

