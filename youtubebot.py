#pip install selenium

from selenium import webdriver
from time import sleep

# For This You Have To Download Chrome Driver

driver1 = webdriver.Chrome(executable_path="C:\\Users\\Nagendra\\Downloads\\Chromedriver\\chromedriver")
driver2 = webdriver.Chrome(executable_path="C:\\Users\\Nagendra\\Downloads\\Chromedriver\\chromedriver")
driver3 = webdriver.Chrome(executable_path="C:\\Users\\Nagendra\\Downloads\\Chromedriver\\chromedriver")
driver4 = webdriver.Chrome(executable_path="C:\\Users\\Nagendra\\Downloads\\Chromedriver\\chromedriver")

# Browser

driver1.get("https://youtu.be/P-rk9FdxdTY")
driver2.get("https://youtu.be/P-rk9FdxdTY")
driver3.get("https://youtu.be/P-rk9FdxdTY")
driver4.get("https://youtu.be/P-rk9FdxdTY")

while True:
    sleep(20)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
