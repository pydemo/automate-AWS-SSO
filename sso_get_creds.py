import os, sys
from os.path import join, isdir, isfile, dirname
from  time import sleep
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint  as pp
e=sys.exit

chrome_options = Options()


data_dir=r'C:\Users\alex_\mygit\py_ortho\chrome-data'


options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
if 0:
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    #options.add_argument("--disable-gpu")
    #options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("--no-proxy-server")
    #options.add_argument("--disable-infobars")
    #options.add_argument("--disable-extensions")
    #options.add_argument("--disable-setuid-sandbox")
    options.add_argument('--remote-debugging-port=9222')
    

    

options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
options.add_argument("--user-data-dir=chrome-data")


driverpath = r".\driver\nt\chromedriver_88.exe"

url="https://myapplications.microsoft.com/"

def save_creds(fn, data):
    dn=dirname(fn)
    if not isdir(dn):
        os.makedirs(dn)
    if isfile(fn):
        os.remove(fn)
    with open(fn, 'w') as fh:
        fh.write(data)
    
if __name__=="__main__":
    if 1:
        driver = webdriver.Chrome(executable_path=driverpath,options=options)
    
    driver.get(url)
    sleep(1)
    driver.set_window_size(1000, 1000)
    sleep(1)
    Print('MS "All Apps"')
    a=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div[3]/div/div/div/div/a')

    aws_url = a.get_attribute('href')
    print(aws_url)
    if 1:
        driver.get(aws_url)
        #sleep(2000)
    if 1:
        
        while True:
            sleep(2)
            print('Accounts')
            try:
            
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/portal-application').click() 
                break
            except:
                print('Trying...')
        sleep(0.5)
        

        if 1: 
            env='DEV'
            print(f'Trying "{env}"')
            driver.find_element_by_xpath('//*[@id="ins-6e94a0c3ed76b196"]/div/div/div/div[2]').click()
            sleep(0.5)
            print('Command line or programmatic access')
            driver.find_element_by_xpath('//*[@id="temp-credentials-button"]').click()
            sleep(0.5)
            if 1: 
                print('"Windows" url')
                driver.find_element_by_xpath('//*[@id="p-51c7c7674ed91244"]/sso-modal/div/div/div[2]/modal-content/div/div[3]/sso-tabs/ul/li[2]/a').click()
                sleep(0.5)
                print('Hove/Click/Copy')
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[1]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/creds-modal/sso-modal/div/div/div[2]/modal-content/div/div[3]/sso-tabs/sso-tab[2]/div/div/div[2]/hover-to-copy/div').click()
                sleep(0.5)
                print(env)
                data=pyperclip.paste()
                if 1:
                    fn=join('.creds',f'{env}.txt')
                    save_creds(fn, data)
                    print(f'"{env}" keys are save to "{fn}"')
                print('Close popup')
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[1]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/creds-modal/sso-modal/div/div/div[1]/span').click()
                sleep(0.5)
        
        if 1: 
            env='QA'
            print(f'Trying "{env}"')
            driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[2]/portal-instance/div/div/div/div[2]').click()
            sleep(0.5)
            print('Command line or programmatic access')
            driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[2]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/a').click()
            sleep(0.5)
            if 1:
                print('"Windows" url')
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[2]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/creds-modal/sso-modal/div/div/div[2]/modal-content/div/div[3]/sso-tabs/ul/li[2]/a').click()
                sleep(0.5)
                print('Hove/Click/Copy')
                driver.find_element_by_xpath('/html/body/app/portal-ui/div/portal-dashboard/portal-application-list/sso-expander/portal-instance-list/div[2]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/span[2]/creds-modal/sso-modal/div/div/div[2]/modal-content/div/div[3]/sso-tabs/sso-tab[2]/div/div/div[2]/hover-to-copy/div').click()
                sleep(0.5)
                print(env)
                data=pyperclip.paste()
                if 1:
                    fn=join('.creds',f'{env}.txt')
                    save_creds(fn, data)
                    print(f'"{env}" keys are save to "{fn}"')
            
    driver.quit()