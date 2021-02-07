import os
from os.path import isdir
from  time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


data_dir='chrome-data'
if not isdir(data_dir):
    os.makedirs(data_dir)

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
#mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
#options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
options.add_argument("--user-data-dir=chrome-data")


driverpath = r".\driver\nt\chromedriver_88.exe"

url="https://myapplications.microsoft.com/"

if __name__=="__main__":
    if 1:
        driver = webdriver.Chrome(executable_path=driverpath,options=options)
        options.add_argument(f"user-data-dir={data_dir}")
        
        
        driver.get(url)
        time.sleep(300)  # Time to enter credentials
        driver.quit()