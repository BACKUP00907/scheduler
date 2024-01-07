from selenium import webdriver
import time

url = 'https://strmltpym1.streamlit.app/'
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
browser = webdriver.Chrome(options=options)
page = browser.get(url)
time.sleep(40)
browser.quit()
