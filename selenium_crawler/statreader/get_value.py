from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re 
import requests
import sys 

stats_update_url = "https://statreader.herokuapp.com/stat/update/"

chromeOptions = Options()
chromeOptions.headless = True
browser = webdriver.Chrome(options=chromeOptions)

url = sys.argv[1]
selector = sys.argv[2]
id = sys.argv[3]

try: 
    print(url, ":", end="")
    browser.get(url)
    element = browser.find_element(By.CSS_SELECTOR, selector)
    text_content = element.get_attribute("textContent")
    cleaned_text = re.sub('[^\d\.]', '', text_content)
    print(cleaned_text)

    resp = requests.post(url=stats_update_url, data={
        "password": "masalansecure", 
        "id": id,
        "value": cleaned_text,
    })

except Exception as e:
    print("failed")

browser.quit()
exit() 